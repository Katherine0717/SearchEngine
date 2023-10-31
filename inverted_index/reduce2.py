#!/usr/bin/env python3
"""Reducer 2."""
import sys
import itertools


def reduce_one_group(key, group):
    """Term frequency in each document."""
    dic = {}
    dic_idf = {}
    for line in group:
        _, word, idf, freq = line.strip().split()
        if word not in dic:
            dic[word] = int(freq)
            dic_idf[word] = float(idf)
        else:
            dic[word] += int(freq)

    total_number = 0
    for _, freq in dic.items():
        total_number += freq

    for word, freq in dic.items():
        tf_ = freq
        wik = tf_ * (dic_idf[word])
        print(f"{key} {word}\t{tf_} {dic_idf[word]} {wik}")


def keyfunc(line):
    """Return the key from a TAB-delimited key-value pair."""
    return line.partition("\t")[0]


def main():
    """Divide sorted lines into groups that share a key."""
    for key, group in itertools.groupby(sys.stdin, keyfunc):
        reduce_one_group(key, group)


if __name__ == "__main__":
    main()
