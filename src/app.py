import sys
from venv import logger
import wave


# don't do that, bacalhau jobs don't have access to interent
# should get the file from the input folder
# def download_from_ipfs_gateway(hash):
#     url = f'https://ipfs.eth.aragon.network/ipfs/{hash}?filename=exitCode'

#     print("URL:",url)

#     output_dir = "./outputs"
#     # input_dir = "/inputs"

#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
    
#     response = requests.get(url)

#     if response.status_code == 200:
#         file_path = f'{output_dir}/downloaded_file_{hash}'
#         with open(file_path, 'wb') as f:
#             f.write(response.content)
        
#         print(f'File downloaded to: {file_path}')
#     else:
#         print('Error downloading file. Status code: {response.status_code}')


input_dir = "/inputs"
output_dir = "/outputs"

def main():
    print("The app started")
    file_path = f"{input_dir}/{sys.argv[1]}"
    print("file_path", file_path)
    


    # opening a file and pasting to /outputs folder
    # for file in os.listdir(input_dir):
    #     file_path = os.path.join(input_dir, file)
    #     print(f'Moving file: {file_path}')
    #     if not os.path.exists(output_dir):
    #         os.makedirs(output_dir)
    #     destination_path = os.path.join(output_dir, file)
    #     shutil.move(file_path, destination_path)
    #     print(f'File moved to: {destination_path}')
    #     logger.info(f'File moved to: {destination_path}')

    try:
        with wave.open(file_path, "rb") as wave_file:
            print("in try")
            
            frame_rate = wave_file.getframerate()
            print("in try")
            print(f"Frame rate of input audio: {frame_rate}")
            num_channels = wave_file.getnchannels()
            print(f"num_channels: {num_channels}")

    except Exception as e:
            logger.error(f"Cannot detect frame rate from input audio.... Error: {e}")

    



if __name__ == '__main__':
    main()
