import sys
from venv import logger
import wave
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import numpy as np
from scipy.io.wavfile import write

# command: app.py sample_file_name sentence output lang

# to run it from local just make folders mkdir /inputs and then past the sample file

def main():
    print("The app started")
    file_name = sys.argv[1]
    speech_data = sys.argv[2]
    output_lang = sys.argv[3]
    input_dir = sys.argv[4]
    output_dir = sys.argv[5]
    
    print("file_name", file_name)
    print("speech_data",speech_data)
    print("output_lang", output_lang)
    print("input_dir",input_dir)
    print("output_dir",output_dir)
    
    sample_audio_file_path = f"{input_dir}/{file_name}"
    print("sample_audio_file_path", sample_audio_file_path)
    

    # Just leaving this for debugging reasons
    try:
        with wave.open(sample_audio_file_path, "rb") as wave_file:
            
            #  audio frame and channels
            frame_rate = wave_file.getframerate()
            print(f"Frame rate of input audio: {frame_rate}")
            num_channels = wave_file.getnchannels()
            print(f"num_channels: {num_channels}")

    except Exception as e:
            logger.error(f"Cannot detect frame rate from input audio.... Error: {e}")
            
            
    config = XttsConfig()
    # model_path = os.path.join(os.path.dirname(__file__), 'model/config.json')
    # print("model_path",model_path)
    config.load_json("model/config.json")
    model = Xtts.init_from_config(config)
    model.load_checkpoint(config, checkpoint_dir="model/", eval=True)
    print("model is loaded, my brotha")
    
    try:
        outputs = model.synthesize(
            speech_data,
            config,
            speaker_wav=sample_audio_file_path,
            language=output_lang
        )
        print("almost done, audio file is sythetized")

        scaled = np.int16(outputs['wav'] * 32767)

        sample_rate = 22500
        output_sample_rate = sample_rate 

        write(f'{output_dir}/output.wav', output_sample_rate, scaled)
        print("FILE IS READY BABY",{output_dir},"output.wav")

        try: # Just leaving this for debugging reasons
            with wave.open(f'{output_dir}/output.wav', "rb") as wave_file:
                frame_rate = wave_file.getframerate()
                print(f"Frame rate of input audio: {frame_rate}")
                num_channels = wave_file.getnchannels()
                print(num_channels)
        except Exception as e:
            print(f"Cannot detect frame rate from input audio.... Error: {e}")

    except Exception as e:
            print("ERROR",e)




if __name__ == '__main__':
    if len(sys.argv) < 6:  # Change 3 to the expected number of arguments
        logger.error("Missing some argument: run app.py sample_file_name sentence output_lang[it,eng,de,es,js,pt,tr] input_folder output_folder")
        logger.error("for instance run:")
        logger.error("python src/app.py fabri.wav \"ciao come stai?\" it inputs outputs")
        # in lilypad need to pass /inputs /outputs
        sys.exit(1)
    print("APP is starting....")
    main()
