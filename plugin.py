import sys
import platform
import subprocess
import os
import shutil
import tkinter
from tkinter import messagebox  # noqa: F401
from tkinter import filedialog  # noqa: F401


print('Adobe Flash Player')
print('https://adobe.com')
print("Copywrite © 1996-2020 Adobe. All Rights Reserved")
print('Adobe and Flash are either trademarks or registered trademarks in the United States and/or other countries')  # noqa: E501
print("Flash Player has been depriciated. Run flash files at your own risk")

d = os.path.dirname(os.path.abspath(__file__))
hasRan = os.path.join(d, '.has_ran.txt')

os.makedirs(os.path.join(d, 'bin'), exist_ok=True)

flashPath = ''
if platform.system() == 'Linux':
    flashPath = os.path.join(d, 'bin', 'flashplayer_32')
elif platform.system() == 'Windows':
    flashPath = os.path.join(d, 'bin', 'flashplayer_32.exe')
elif platform.system() == 'Darwin':
    flashPath = os.path.join(d, 'bin', 'flashplayer_32.dmg')

if not os.path.exists(flashPath) or not os.path.isfile(flashPath):
    message = tkinter.messagebox.askyesno(
        title='Disclaimer',
        message="Flash player has been depriciated.\n" +
        "We will not be responsible for any problems caused by running Adobe Flash Player/Projector\n" +  # noqa: E501
        "You will have to provide a copy of Adobe Flash Projector 32 yourself.\n" +  # noqa: E501
        "We cannot provide Adobe Flash Player for you.\n" +
        "Do you understand and agree to these terms?",
    )
    if message is False:
        exit()

    filename = tkinter.filedialog.askopenfilename(
        initialdir=os.path.expanduser('~'),
        title="Select a Flash Player Projector 32 executable",
    )
    if os.path.exists(filename) and os.path.isfile(filename):
        if '.' in os.path.basename(filename):
            if os.access(filename, os.X_OK):
                shutil.copy(filename, os.path.join(d, 'bin', 'flashplayer_32'))
            else:
                tkinter.messagebox.showerror(
                    title='ERROR',
                    message='File must be an linux executable'
                )
                exit()
        elif '.exe' in os.path.basename(filename):
            shutil.copy(filename, os.path.join(d, 'bin', 'flashplayer_32.exe'))
        elif '.dmg' in os.path.basename(filename):
            shutil.copy(filename, os.path.join(d, 'bin', 'flashplayer_32.dmg'))
        else:
            tkinter.messagebox.showerror(
                title='ERROR',
                message='File must be an linux executable, exe file, or dmg file'  # noqa: E501
            )
            exit()
    else:
        tkinter.messagebox.showerror(
            title='ERROR',
            message='You must select a executable file'
        )
        exit()


flash = flashPath
print(sys.argv[-1])
assert len(sys.argv) != 0
f = sys.argv[-1]
assert os.path.exists(f)
assert os.path.isfile(f)
assert f.endswith('.swf')
# TODO: sandbox flash
if flash and flash != '':
    print(subprocess.run(f'{flash} "{os.path.abspath(f)}"', shell=True))
else:
    raise Exception('No flash player libraries are installed')
