#!/usr/bin/env python3
"""Map 2."""

import sys

# reads the output of reduce1
for line in sys.stdin:
    doc_id, word, idf, freq = line.strip().split()
    print(doc_id, "\t", word, idf, freq)
