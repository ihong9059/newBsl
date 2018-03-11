
import sys
search = tuple
with open("dict.txt","w") as archi:
    t = sys.stdout
    sys.stdout = archi
    help(dict)
    sys.stdout = t
