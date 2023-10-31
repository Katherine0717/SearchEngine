#!/usr/bin/env python3
"""Reducer 3."""
import sys
import itertools
import math


def reduce_one_group(_, group):
    """Term frequency in each document."""
    total_wik = 0
    group = list(group)
    for line in group:
        _, word, tfd, idf, wik = line.strip().split()
        total_wik = total_wik + math.pow(float(wik), 2)

    for line in group:
        doc_id, word, tfd, idf, wik = line.strip().split()
        print(f"{word}\t{idf} {doc_id} {tfd} {total_wik}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
