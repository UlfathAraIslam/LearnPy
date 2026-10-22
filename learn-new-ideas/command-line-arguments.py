import sys
print(sys.argv)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("--times", type=int, default=1)
args = parser.parse_args(["Rahim", "--times", "2"])
print(args.name, args.times)