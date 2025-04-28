import os
import sys

INPUT = sys.argv[1]
OUTPUT = sys.argv[2]
MAX_DEPTH = int(sys.argv[3])
# print(INPUT, OUTPUT, MAX_DEPTH)
for root, dirs, files in os.walk(INPUT):
    root = root.replace(INPUT, "")
    path = root.split(os.sep)
    sb = ""
    for i in path[max(0, len(path) - MAX_DEPTH):]:
        sb += i + '/'
        if not os.path.isdir(f'{OUTPUT}/{sb}'):
            os.system(f"mkdir {OUTPUT}/{sb}")
    for file in files:
        print("/".join(path[max(0, len(path) - MAX_DEPTH):]))
        os.system(f"cp {INPUT}/{"/".join(path)}/{file} {OUTPUT}/{"/".join(path[max(0, len(path) - MAX_DEPTH):])}/")

