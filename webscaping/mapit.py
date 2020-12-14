# mapit.py - launches a map in a
# browser using an address from the command line

import webbrowser, sys
import pyperclip
# If there are arguments, use args as address
# If there are no arguments, grab from clipboard

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
    prefix = "https://www.google.com/maps/place/"

else:
    address = pyperclip.paste()

webbrowser.open(prefix + address)



