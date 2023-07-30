#!/usr/bin/env python3


def prime(random_num):
    k = 0
    for i in range(2, random_num // 2 + 1):
        if (random_num % i == 0):
            k = k + 1
    if (k <= 0):
        return "yes"
    else:
        return "no"
