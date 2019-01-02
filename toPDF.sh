#!/bin/sh

# if [ -z $(pip list | grep -F "mail-parser" ) ]; then
#     pip install mail-parser || sudo pip install mail-parser
# fi

# if [ -z $(brew cask list | grep -F "wkhtmltopdf" ) ]; then
#     brew install Caskroom/cask/wkhtmltopdf
# fi
location=~/Downloads
for file in $location/*.eml;
do
    echo $file
    name=${file##*/}
    noeml=${name%.eml}
    echo "$noml"
    mailparser -f $file -b > $location/$noeml.html
    x=$noeml.html
    wkhtmltopdf $location/$x $location/$noeml.pdf
done

# Uncomment any these if you'd prefer not to keep a file type.
# rm -f *.eml
# rm -f *.html
# rm -f *.pdf
