# Synthetizoor
This is a project to replicate what we [did here with cartesi](https://github.com/dub3-space/dub3-hackthon-project/tree/main/cartesi). it's a module to synthetize voices giving an input

It uses [this repo](https://github.com/dub3-space/base-lily-module) as a template


## Running with docker locally

```
mkdir /tmp/output_synth
mkdir /tmp/input_synth
# need to copy a .wav file in input_synth
docker run  -v /tmp/output_synth:/outputs -v/tmp/input_synth:/inputs bringhi/synt:2.0  xxx.wav "ciao come stai?" it /inputs /outputs 
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
`command coming soon`


## List of commits  and docker image to to attach to commands above
| git tag | docker image | command
|-----------------|-----------------|-----------------|
| 0a57dc9cc4e37a11644bcdecb4107a20eba833d8   | bringhi/synt:0.6    | lilypad run github.com/dub3-space/lily-synthetizoor:0a57dc9cc4e37a11644bcdecb4107a20eba833d8 -i URL=https://bafkreiafqxh2jlmzjiuaoytga7ntu36gghww3y2bc6mrelbbg2nfijnz2u.ipfs.w3s.link/    |
| xxx    | xxx    |
| xxx    | xxx    |



