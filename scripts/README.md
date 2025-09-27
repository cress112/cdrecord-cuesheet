# Helper Scripts
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
pipenv run start <input_dir_contains_audio_files> <output_dir>
pipenv run start wavs normalized
```