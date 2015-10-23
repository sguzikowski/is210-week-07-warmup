#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Optional and required things."""
import decimal

def lexicographics(to_analyze):
    """fill this in later xi
    """
    LINES = to_analyze.split('\n')
    ALIST = []
    for line in LINES:
        words = line.split(' ')
        ALIST.append(len(words))
    return tuple([max(ALIST), min(ALIST), decimal.Decimal(sum(ALIST)/decimal.Decimal(len(ALIST)))])
