# CUEfile example
### How to use
- list devices
    ```sh
    cdrecord -scanbus
    ```
- place music files into `files/` directory
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
- [cdrecord manual](https://cdrtools.sourceforge.net/private/man/cdrecord/cdrecord.1.html)
- [CUE sheet file format spec](https://wyday.com/cuesharp/specification.php)
