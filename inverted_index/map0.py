#!/usr/bin/env python3
"""Map 0."""
import csv
import sys

csv.field_size_limit(sys.maxsize)
for row in csv.reader(sys.stdin):
    # doc_id, doc_title, doc_content = row
    print("stupid\tcode")

    # job1- reads from csv
    # then standard.in for the rest
