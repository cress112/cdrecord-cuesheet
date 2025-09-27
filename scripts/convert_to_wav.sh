#!/usr/bin/env bash

### * convert files in $1/* to $2/*.wav

### check arg1, arg2 is dir
if [ ! -e "$1" ] && [ ! -d "$1" ]; then
    echo "$1 does not exist"
    exit 1
fi
if [ ! -e "$2" ]; then
    echo "$2 does not exist, creating..."
    mkdir -p "$2"
fi

### convert audio files into wav (PCM quality)
# https://qiita.com/yuba/items/489fadb350246b5c94e7
while read -d $'\0' file; do
    # pass if it is directory or dot files (.DS_Store, .gitignore, ...)
    if [ -d "$file" ] || [[ "$file" =~ ^.*\/\.[^/]*$ ]] || [[ "$file" =~ ^\.[^/]*$ ]]; then
        echo "skipping $file ..."
        continue
    fi
    file_name=$(echo $file | sed -r 's/^([^/]*\/)*(.*)\.[^.]+$/\2/')
    target_file="$2/converted_${file_name}.wav"
    echo "convert '$file' to '$target_file'"
    ffmpeg -i "$file" -nostdin -vn -ac 2 -ar 44100 -acodec pcm_s16le "$target_file"
done < <(find "$1" -mindepth 1 -maxdepth 1 -print0)

