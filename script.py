import os
import sys

INPUT = sys.argv[1]
OUTPUT = sys.argv[2]

for root, dirs, files in os.walk(INPUT):
    path = root.split(os.sep)
    cp = "/".join(path)
    for file in files:
        os.system(f"cp {cp}/{file} {OUTPUT}/")
