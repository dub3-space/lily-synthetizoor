import os
import shutil
from venv import logger


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
    # TODOS:
    #   Get a file from IPFS NO!
    #   get file from inputs folder instead
    #   parse file 
    #   output the file content
    # Replace 'QmbGyyFwHGg7yutRXxGUcErgdhe97xwNdxSU6E26SHbmEn' with the actual hash
    # file_hash = 'QmS6mcrMTFsZnT3wAptqEb8NpBPnv1H6WwZBMzEjT8SSDv'
    # download_from_ipfs_gateway(file_hash)


    # I created a file named cane.txt in 
    for file in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file)
        print(f'Moving file: {file_path}')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        destination_path = os.path.join(output_dir, file)
        shutil.move(file_path, destination_path)
        print(f'File moved to: {destination_path}')
        logger.info(f'File moved to: {destination_path}')





if __name__ == '__main__':
    main()
