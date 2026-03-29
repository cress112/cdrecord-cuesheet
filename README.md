# Burn CD from CUEfile
### How to do
- list devices
    ```sh
    cdrecord -scanbus
    ```
- confirm device spec(available speed/raw mode/...)
    ```sh
    cdrecord -prcap dev=<device>
    ```
- place music files into specific directory
- edit cuesheet.cue
- run burning test
    ```sh
    cdrecord -dummy -eject -v -raw -pad speed=<speed:int> cuefile=cuesheet.cue dev=<device>
    ```
- burn CD
    ```sh
    cdrecord -eject -v -raw -pad speed=<speed:int> cuefile=cuesheet.cue dev=<device>
    ```

### References
- cdrecord
    - [cdrecord manual](https://cdrtools.sourceforge.net/private/man/cdrecord/cdrecord.1.html)
- cuesheet
    - [CUE sheet file format spec](https://wyday.com/cuesharp/specification.php)
    - [documentation](https://github.com/libyal/libodraw/blob/main/documentation/CUE%20sheet%20format.asciidoc)
# Rip CD
### How to do
- list devices
    ```sh
    cdrecord -scanbus
    ```
- exec ripping
    ```sh
    # -x: max quality, -B: seperate tracks into other files, -O: output format
    cdda2wav dev=<device> speed=4 -x -B -O wav
    ```

### References
- [cdda2wav](https://cdrtools.sourceforge.net/private/man/cdda2wav-2.0.html)
