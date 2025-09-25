# Burn CD from CUEfile
### How to do
- list devices
    ```sh
    cdrecord -scanbus
    ```
- place music files into specific directory
- edit cuesheet.cue
- run burning test
    ```sh
    cdrecord -dummy -v -dao -pad speed=8 cuefile=cuesheet.cue dev=<device>
    ```
- burn CD
    ```sh
    cdrecord -eject -v -dao -pad speed=8 cuefile=cuesheet.cue dev=<device>
    ```

### References
- cdrecord
    - [cdrecord manual](https://cdrtools.sourceforge.net/private/man/cdrecord/cdrecord.1.html)
- cuesheet
    - [CUE sheet file format spec](https://wyday.com/cuesharp/specification.php)
    - [CUE sheet Example](https://ordinarysound.com/cue-sheet/)
- cd-text
    - [GENRE](https://www.gnu.org/software/libcdio/cd-text-format.html#table_003agenres)

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
