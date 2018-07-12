#!/usr/bin/env python3.6
import subprocess

with open('/Users/Dustin/.zshrc', 'r') as f:
    zsh = f.read()
    with open('/Users/Dustin/Documents/Dropbox/Config Files/zshrc.txt', 'w+') as out:
        out.write(zsh)

brews = subprocess.run(['brew', 'list'], stdout=subprocess.PIPE)
with open('/Users/Dustin/Documents/Dropbox/Config Files/brew.txt', 'wb') as out2:
    out2.write(brews.stdout)

codeext = subprocess.run(['code', '--list-extensions'], stdout=subprocess.PIPE)
with open('/Users/Dustin/Documents/Dropbox/Config Files/vscodeextensions.txt', 'wb') as out3:
    out3.write(codeext.stdout)
