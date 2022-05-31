#!/bin/bash

#VAR
INPUT=$1

#FUNC
print_help() {
    echo -e "Usage : ./make.sh [input]"
    echo -e "Example : './make.sh yt-dlp-helper-v2-5.py' (one file only.)"
}

main() {
    if [ -z "$INPUT" ]
    then
        echo -e "ERROR : Input not specified."
    else
        python3.10 -m py_compile ./src/$INPUT
        mv ./src/__pycache__/* ./yt-dlp-helper.pyc
        rm -rf ./src/__pycache__/
    fi
}

main
# python3.10 -m py_compile ./src/*.py
# mv ./src/__pycache__/yt-dlp-helper-v2-1.cpython-310.pyc ./yt-dlp-helper-v2-1.pyc
# mv ./src/__pycache__/yt-dlp-helper-win.cpython-310.pyc ./yt-dlp-helper-win.pyc
# mv ./src/__pycache__/yt-dlp-helper-v2-4.cpython-310.pyc ./yt-dlp-helper.pyc
# #mv ./src/__pycache__/yt-dlp-helper-v2-3.cpython-310.pyc "./yt-dlp-helper-v2.3.1.pyc"
