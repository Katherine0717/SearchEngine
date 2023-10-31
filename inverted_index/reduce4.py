#!/usr/bin/env python3
"""Reducer 4."""
import sys
import itertools


def reduce_one_group(_, group):
    """Print out output."""
    dic = {}
    count = 0
    for line in group:
        _, word, idf, doc_id, tfd, di_ = line.strip().split()
        if word not in dic:
            dic[word] = word
            if count != 0:
                print()
            print(f"{word} {idf}", end=" ")
        print(f"{doc_id} {tfd} {di_}", end=" ")
        count += 1

    print()


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
