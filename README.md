# Synthetizoor
This is a project to replicate what we [did here with cartesi](https://github.com/dub3-space/dub3-hackthon-project/tree/main/cartesi). it's a module to synthetize voices giving an input

It uses [this repo](https://github.com/dub3-space/base-lily-module) as a template


## Running docker locally

```
mkdir /tmp/output_synth
mkdir /tmp/input_synth
docker run  -v /tmp/output_synth:/outputs -v/tmp/input_synth:/inputs bringhi/synt:0.x 
```
At the end you'll have something in your `/tmp/output_synth` folder

## Running it Lilypad

```
lilypad run github.com/dub3-space/lily-synthetizoor:xxxxx -i URL=https://xxxx.ipfs.w3s.link/
```


## List of commits  and docker image to to attach to commands above
| git tag | docker image |
|-----------------|-----------------|
| 0a57dc9cc4e37a11644bcdecb4107a20eba833d8   | bringhi/synt:0.6    |
| xxx    | xxx    |
| xxx    | xxx    |
