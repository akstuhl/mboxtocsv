# mboxtocsv
scripts to parse mbox file, convert to csv

## Converting your .mbox email collection into a .csv data file:
1. Copy this repository to your computer by opening Terminal and entering `git clone https://github.com/akstuhl/mboxtocsv.git`
2. Still in Terminal, move into the repository's directory by entering `cd mboxtocsv`
3. Copy your mbox file into the mboxtocsv directory
4. Open mbox_parser.py in a text editor and in the line `for message in mailbox.mbox('Spam.mbox'):` replace Spam.mbox with the name of your mbox file
5. Again in the terminal, enter `python mbox_parser.py`
6. You should see a file appear in the mboxtocsv directory called clean_email.csv, which you can open in Excel, etc.
