# sys module

#['google','galaxy','note','5']


import sys  , webbrowser
sys.argv

print (sys.argv)

if len(sys.argv)> 1:
    toSearch = '+'.join(sys.argv[1:])
    address = "https://www.google.co.in/search?q={}".format(toSearch)
    webbrowser.open(address)
