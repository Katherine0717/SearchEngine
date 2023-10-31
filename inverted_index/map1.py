#!/usr/bin/env python3
"""Map 1."""
import csv
import sys
import re


# so you wanna combine the document and the input by one
csv.field_size_limit(sys.maxsize)
for row in csv.reader(sys.stdin):
    document_id, document_title, document_body = row
    text = document_title + " " + document_body
    text = re.sub(r"[^a-zA-Z0-9 ]+", "", text)
    text = text.casefold()
    text = text.split(" ")
    # stop_words = []
    with open('stopwords.txt', 'r', encoding="utf8") as file:
        stop_words = file.read().split("\n")
        for word in text:
            if word not in stop_words:
                print(f'{word}\t{document_id}')
