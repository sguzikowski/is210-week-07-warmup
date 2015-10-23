#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Optional and required things."""

def fibonacci(maxint):
    """
    FILL THIS IN
    """
    a, b = 0, 1
    numbers = []
    if maxint >= 0:
        while a <= maxint and a >= 0:
            numbers.append(a)
            a, b = b, a+b

    
    return numbers
