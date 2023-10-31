#!/usr/bin/env python3
"""Map 3."""

import sys

for line in sys.stdin:
    doc_id, word, tfd, idf, wik = line.strip().split()
    print(doc_id, "\t", word, tfd, idf, wik)
