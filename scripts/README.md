# Helper Scripts
- convert audio files to PCM quality and normalize loudness in one-liner
```sh
scripts/convert_to_wav.sh files wavs && pipenv run normalize wavs normalized && rm -rf wavs
```
### convert files to WAV
- place audio files into a directory
- exec
```sh
scripts/convert_to_wav.sh <input_dir_contains_audio_files> <output_dir>
scripts/convert_to_wav.sh files wavs
```
### normalize loudness
- place audio files(.wav) into a directory
- exec
```sh
pipenv run normalize <input_dir_contains_audio_files> <output_dir>
pipenv run normalize wavs normalized
```

### shift pitch
- exec
```sh
pipenv run shift <target_wav_file> <shift_width: +/-(int)>
```