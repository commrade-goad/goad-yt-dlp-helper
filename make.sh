#!/bin/sh
python3 -m py_compile ./src/yt-dlp-helper.py
python3 -m py_compile ./src/yt-dlp-helper-win.py
mv ./src/__pycache__/yt-dlp-helper.cpython-310.pyc ./yt-dlp-helper.pyc
mv ./src/__pycache__/yt-dlp-helper-win.cpython-310.pyc ./yt-dlp-helper-win.pyc
rmdir ./src/__pycache__/

