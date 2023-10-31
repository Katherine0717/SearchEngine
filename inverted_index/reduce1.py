#!/usr/bin/env python3
"""Reducer 1."""
import sys
import itertools
import math


def reduce_one_group(key, group):
    """Inverse document frequency."""
    # Get N
    with open('total_document_count.txt', 'r', encoding="utf8") as file:
        total_n = int(file.read())

    # nk: number of documents that contain term tk
    dic = {}
    for line in group:
        _, doc_id = line.strip().split()
        if doc_id not in dic:
            dic[doc_id] = 1
        else:
            dic[doc_id] += 1

    idf = math.log((total_n/len(dic)), 10)
    for doc_id, id_ in dic.items():
        print(f"{doc_id} {key}\t{idf} {id_}", end='\n')


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
