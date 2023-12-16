from os import environ
import logging
import os
from dotenv import load_dotenv
import requests
import json
import wave
import numpy as np
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
from scipy.io.wavfile import write
from pinatapy import PinataPy

load_dotenv()
 
logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")

def str2hex(str):
    """
    Encodes a string as a hex string
    """
    return "0x" + str.encode("utf-8").hex()

def handle_advance(data):
    try: 
        logger.info(f"Received advance request data {data}")
        logger.info(data["payload"])

        payload = bytes.fromhex(data["payload"][2:]).decode('utf-8')

        logger.info('decoded payload\n' + payload)

        parsed_data = json.loads(payload)

        sample_url = parsed_data["sample"]

        logger.info(sample_url)

        response = requests.get(sample_url)

        if response.status_code == 200:
        # Get the content of the response
            audio_content = response.content
            
            file_path = "downloaded_audio.wav"  # Change the file extension if the audio is in a different format
            
            # Save the downloaded file
            with open(file_path, "wb") as file:
                file.write(audio_content)

            logger.info(f"File saved as '{file_path}'")

            try:
                with wave.open(file_path, "rb") as wave_file:
                    frame_rate = wave_file.getframerate()
                    logger.info(f"Frame rate of input audio: {frame_rate}")
                    num_channels = wave_file.getnchannels()
                    logger.info(num_channels)
            except Exception as e:
                logger.error(f"Cannot detect frame rate from input audio.... Error: {e}")

        else:
            logger.error("Failed to download the file.")

        speech_data = parsed_data['speech']
        output_lang = parsed_data['output_lang']

        logger.info('This is a speech ' + speech_data)

        config = XttsConfig()
        config.load_json("model/config.json")
        model = Xtts.init_from_config(config)
        model.load_checkpoint(config, checkpoint_dir="model/", eval=True)

        try:
            outputs = model.synthesize(
                speech_data,
                config,
                speaker_wav="downloaded_audio.wav",
                language=output_lang
            )

            scaled = np.int16(outputs['wav'] * 32767)

            sample_rate = 44100
            output_sample_rate = sample_rate // 2

            write('output.wav', output_sample_rate, scaled)

            try:
                with wave.open('output.wav', "rb") as wave_file:
                    frame_rate = wave_file.getframerate()
                    logger.info(f"Frame rate of input audio: {frame_rate}")
                    num_channels = wave_file.getnchannels()
                    logger.info(num_channels)
            except Exception as e:
                logger.error(f"Cannot detect frame rate from input audio.... Error: {e}")

        except Exception as e:
            logger.error(e)

        api_key = os.environ.get("PINATA_API_KEY")
        secret_key = os.environ.get("PINATA_SECRET_API_KEY")
        if api_key and secret_key:
            pinata = PinataPy(api_key, secret_key)
            resp = pinata.pin_file_to_ipfs(f'output.wav')
            print(resp['IpfsHash'])

        payloadToSent = resp['IpfsHash']
        response = requests.post(rollup_server + "/notice", json={"payload": str2hex(payloadToSent)})
        logger.info(f"Received notice status {response.status_code} body {response.content}")

        return "accept"
    except Exception as e:
        logger.error(e)

def handle_inspect(data):
    logger.info(f"Received inspect request data {data}")
    return "accept"

handlers = {
    "advance_state": handle_advance,
    "inspect_state": handle_inspect,
}

finish = {"status": "accept"}

def main_loop():
    finish = {"status": "accept"}
    rollup_address = None

    while True:
        logger.info("Sending finish")
        response = requests.post(rollup_server + "/finish", json=finish)
        logger.info(f"Received finish status {response.status_code}")
        if response.status_code == 202:
            logger.info("No pending rollup request, trying again")
        else:
            rollup_request = response.json()
            data = rollup_request["data"]
            if "metadata" in data:
                metadata = data["metadata"]
                if (metadata["epoch_index"] == 0
                        and metadata["input_index"] == 0):
                    rollup_address = metadata["msg_sender"]
                    logger.info(f"Captured rollup address: {rollup_address}")
                    continue
            handler = handlers[rollup_request["request_type"]]
            finish["status"] = handler(rollup_request["data"])

if __name__ == '__main__':
    main_loop()