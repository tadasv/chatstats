#!/bin/bash
pushd ~ubuntu/src/chatstats
sudo -u ubuntu git pull && sudo killall python
popd
