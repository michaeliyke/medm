#!/usr/bin/env bash
for video in files/*.mkv ; do
    python -m medm convert "$video"
done
