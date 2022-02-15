#!/bin/sh
python3.10 -m py_compile ./src/*.py
mv ./src/__pycache__/yt-dlp-helper-v2.cpython-310.pyc ./yt-dlp-helper.pyc
mv ./src/__pycache__/yt-dlp-helper-win.cpython-310.pyc ./yt-dlp-helper-win.pyc
mv ./src/__pycache__/yt-dlp-helper-v2-1.cpython-310.pyc ./yt-dlp-helper-v2-1.pyc
rmdir ./src/__pycache__/
