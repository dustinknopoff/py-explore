# How to get it to work.

NOTE: This is mac only.

1. Go to Finder.
2. Press CMD+SHIFT+G.
3. Type `~/Library/Application Scripts/com.apple.mail`.
4. Open `saveByRule.scpt` and change `theFolder` to where you'd like emails to be saved.
5. Copy and Paste `saveByRule.scpt` into `~/Library/Application Scripts/com.apple.mail`.
6. Go to Mail>Preferences>Rules>Add Rule.
7. Enter some filter for your rule and choose *Run Applescript* as action to perform. Use *saveByRule* as option.
8. Click Ok.

For converting to PDF and HTML.
1. In the terminal, run `sudo pip install mail-parser` and `brew install Caskroom/cask/wkhtmltopdf`.
1. Open `toPDF.sh` and alter *location* to match the directory your saved emails are located. (Keep \*.eml)
2. In the terminal, run `bash toPDF.sh`.

For Automating conversion to HTML/PDF.
1. Create new>Folder Action in Automator.
2. Set folder to watch to folder where emails are saved.
3. Add `run shell script` action.
4. Copy and paste contents of toPDF.sh into textarea of *run shell script*.
5. Save.

NOTE: saveByRule.scpt is almost entirely copied from StackOverflow.
