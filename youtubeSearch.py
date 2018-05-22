#  https://www.youtube.com/results?search_query=make+joke+of

import sys  , webbrowser
sys.argv

print (sys.argv)

if len(sys.argv)> 1:
    toSearch = '+'.join(sys.argv[1:])
    address = " https://www.youtube.com/results?search_query={}".format(toSearch)
    webbrowser.open(address)
