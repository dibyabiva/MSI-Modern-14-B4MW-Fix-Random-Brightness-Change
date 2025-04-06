filename = "/usr/share/X11/xorg.conf.d/10-quirks.conf"

fix_segment = """
# Fix random brightness change
Section "InputClass"
        Identifier "Spooky Ghosts"
        MatchProduct "Video Bus"
        Option "Ignore" "on"
EndSection
"""

with open(filename, "r") as fobj:
    data = fobj.read()

if fix_segment not in data:
    print("Applying fix...")
    with open(filename, "a") as fobj:
        fobj.write(fix_segment)
    print("Done")
else:
    print("Fix already present.")