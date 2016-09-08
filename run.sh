#!/usr/bin/env sh

# Absolute path to this script. /home/user/bin/foo.sh
SCRIPT=$(readlink -f $0)
# Absolute path this script is in. /home/user/bin
SCRIPTPATH=`dirname $SCRIPT`
cd $SCRIPTPATH

mkdir -p build
rm -rf build/*
cd build

#generate cmake project in the "build" folder
cmake ..

#build and run
make && ../build/fpmtop -u http://127.0.0.1/nginx_status

