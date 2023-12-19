# Synthetizoor
This is a project to replicate what we [did here with cartesi](https://github.com/dub3-space/dub3-hackthon-project/tree/main/cartesi). it's a module to synthetize voices giving an input

It uses [this repo](https://github.com/dub3-space/base-lily-module) as a template


## Running with docker locally

create venv with python 3.10.10
```
pip pip install -r requirements.txt
mkdir /tmp/output_synth
mkdir /tmp/input_synth
# need to copy a .wav file in input_synth

# for linux/amd arch
docker run  -v /tmp/output_synth:/outputs -v /tmp/input_synth:/inputs bringhi/synt:v6.1-amd64 'Ok, sono nato! buon giorno a tutti, mi chaimo dub3!' it /inputs /outputs

# for linux/arm64/v8
docker run  -v /tmp/output_synth:/outputs -v /tmp/input_synth:/inputs bringhi/synt:v6.1-arm 'Ok, sono nato! buon giorno a tutti, mi chaimo dub3!' it /inputs /outputs
```
You need to put some file in /tmp/input_synth
At the end you'll have something in your `/tmp/output_synth` folder

## Running it Lilypad
Lilypad maps the input and output folders.
In the module, you can pass lilypad a URL where your sample file is stored (a file on IPFS ). lily will download it and put it in the folder
```
 "inputs": [
          {
              "URL": {{.URL}},
              "Name": "xxx.wav",
              "StorageSource": "urlDownload",
              "path": "/inputs"
          }
      ],
```
to retrieve the input, you need to get the file from the os, looping thru the input folder.


## List of commits  and docker image to to attach to commands above
| git tag | docker image | command
|-----------------|-----------------|-----------------|
| 0a57dc9cc4e37a11644bcdecb4107a20eba833d8   | bringhi/synt:0.6    | lilypad run github.com/dub3-space/lily-synthetizoor:0a57dc9cc4e37a11644bcdecb4107a20eba833d8 -i URL=https://bafkreiafqxh2jlmzjiuaoytga7ntu36gghww3y2bc6mrelbbg2nfijnz2u.ipfs.w3s.link/    |
|  b4d2e078c3447e1df12588ee854360087ce7f081  (CPU) | bringhi/synt:v6.0-arm (or amd)    |lilypad run github.com/dub3-space/lily-synthetizoor:b4d2e078c3447e1df12588ee854360087ce7f081 -i URL=https://bafybeif3qp2sd7qb67kjhds65b6qr5ecerib76cjclyo625ovledffabfu.ipfs.w3s.link/ -i SENTENCE='Ok, sono nato! buon giorno a tutti, mi chiamo dab three!' -i LANGUAGE=it  -i INPUT_FOLDER=/inputs -i OUTPUT_FOLDER=/outputs |
|  a9b9916270879be6275ad297edd4c595c54a6536 (GPU)   | bringhi/synt:v6.0-arm (or amd)    |lilypad run github.com/dub3-space/lily-synthetizoor:a9b9916270879be6275ad297edd4c595c54a6536 -i URL=https://bafybeif3qp2sd7qb67kjhds65b6qr5ecerib76cjclyo625ovledffabfu.ipfs.w3s.link/ -i SENTENCE='Ok, I am live now! Good morning, everyone. call me dub three!' -i LANGUAGE=it  -i INPUT_FOLDER=/inputs -i OUTPUT_FOLDER=/outputs |




