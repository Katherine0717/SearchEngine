#!/usr/bin/env python3
"""
Template reducer.

https://github.com/eecs485staff/madoop/blob/main/README_Hadoop_Streaming.md
"""
import sys


COUNT = 0
for line in sys.stdin:
    COUNT += 1
print(COUNT)
