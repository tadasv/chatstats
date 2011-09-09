#!/bin/bash
pushd ~ubuntu/src/chatstats
sudo -u ubuntu git pull && sudo nginx -t && sudo nginx -s reload && sudo killall python
popd
