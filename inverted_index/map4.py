#!/usr/bin/env python3
"""Map 4: print output."""

import sys

for line in sys.stdin:
    word, idf, doc_id, tfd, di = line.strip().split()
    key = int(doc_id) % 3
    print(f"{key}\t{word} {idf} {doc_id} {tfd} {di}")
