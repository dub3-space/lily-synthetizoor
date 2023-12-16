import sys
from venv import logger
import wave


input_dir = "/inputs"
output_dir = "/outputs"

def main():
    print("The app started")
    file_path = f"{input_dir}/{sys.argv[1]}"
    print("file_path", file_path)
    

    try:
        with wave.open(file_path, "rb") as wave_file:
            
            #  audio frame and channels
            frame_rate = wave_file.getframerate()
            print(f"Frame rate of input audio: {frame_rate}")
            num_channels = wave_file.getnchannels()
            print(f"num_channels: {num_channels}")

    except Exception as e:
            logger.error(f"Cannot detect frame rate from input audio.... Error: {e}")

    



if __name__ == '__main__':
    main()
