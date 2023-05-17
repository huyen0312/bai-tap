import sys
import getopt

argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, "k=", ["ky_tu="])
    print(opts)
    print(args)
except:
    print("Error")