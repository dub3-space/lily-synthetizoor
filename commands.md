### complete command to run this
```
lilypad run github.com/dub3-space/test-lily-module:e54535a77729d1731d5e5874073aedc56217b86f -i GREET=ciao --module-repo https://github.com/dub3-space/test-lily-module --module-hash e54535a77729d1731d5e5874073aedc56217b86f --module-path ./lilypad_module.json.tmpl
```
### simplified command
```
lilypad run github.com/dub3-space/test-lily-module:e54535a77729d1731d5e5874073aedc56217b86f -i GREET=ciao 
```

### having more logs
`export LOG_LEVEL=debug`

### export web3pk
`export WEB3_PRIVATE_KEY=xxxxx`


### access content on ipfs
accessing content https://ipfs.eth.aragon.network/ipfs/

### install lilypad
```
OSARCH=$(uname -m | awk '{if ($0 ~ /arm64|aarch64/) print "arm64"; else if ($0 ~ /x86_64|amd64/) print "amd64"; else print "unsupported_arch"}') && export OSARCH;

OSNAME=$(uname -s | awk '{if ($1 == "Darwin") print "darwin"; else if ($1 == "Linux") print "linux"; else print "unsupported_os"}') && export OSNAME;

curl -sSL -o lilypad https://github.com/bacalhau-project/lilypad/releases/download/v2.0.0-701b8cb/lilypad-$OSNAME-$OSARCH

chmod +x lilypad
sudo mv lilypad /usr/local/bin/lilypad

# then
lilypad run github.com/username/repo:v0.0.2 -i Message=moo
```



