# Modern-14-B4MW-Fix-Random-Brightness-Change

### This is a small script to add a fix for random brightness changes in this specific laptop model in Ubuntu 22.04.5

* Execute `sudo crontab -e`
* Add `@reboot python3 '/path/to/fix.py' > /dev/null 2>&1` at the end of the file
* Press `CTRL` + `X` to save changes
* Reboot

