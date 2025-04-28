import os
import sys

INPUT = sys.argv[1]
OUTPUT = sys.argv[2]
MAX_DEPTH = int(sys.argv[3])
# print(INPUT, OUTPUT, MAX_DEPTH)
for root, dirs, files in os.walk(INPUT):
    path = root.split(os.sep)
    cp = "/".join(path[1:])
    for file in files:
        if len(path) - 1 <= MAX_DEPTH:
            if not os.path.isdir(f'{OUTPUT}/{cp}'):
                os.system(f"mkdir {OUTPUT}/{cp}")
            os.system(f"cp {INPUT}/{cp}/{file} {OUTPUT}/{cp}/{file}")
        else:
            os.system(f"cp {INPUT}/{cp}/{file} {OUTPUT}/")
