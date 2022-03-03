#!/bin/sh
python3.10 -m py_compile ./src/*.py
mv ./src/__pycache__/yt-dlp-helper-v2-1.cpython-310.pyc ./yt-dlp-helper-v2-1.pyc
mv ./src/__pycache__/yt-dlp-helper-win.cpython-310.pyc ./yt-dlp-helper-win.pyc
# mv ./src/__pycache__/yt-dlp-helper-v2-3.cpython-310.pyc ./yt-dlp-helper.pyc
mv ./src/__pycache__/yt-dlp-helper-v2-3.cpython-310.pyc "./yt-dlp-helper-v2.3.1.pyc"
rm -rf ./src/__pycache__/
