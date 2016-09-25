# -*- coding: UTF-8 -*-
from math import sqrt


# 1
def series_sum(v):
    return [sum(v[:i]) for i in xrange(len(v) + 1)]


# 2
def series_norm(v, a, b):
    return [a if v[i] < a else b if v[i] > b else v[i] for i in xrange(len(v))]


# 4
def inverse_str_formated(s, ch='_'):
    return ''.join([ch if (s[i] == ch) else \
                        '{}' if ((i == 0 or s[i - 1] == ch) and (i == len(s) - 1 or s[i + 1] == ch)) else \
                            '{' if (i == 0 or s[i - 1] == ch) else \
                                '}' if (i == len(s) - 1 or s[i + 1] == ch) else \
                                    '' for i in xrange(len(s))]).format(*[w for w in s.split(ch)[::-1] if w != ''])


# 6
def factorize(n):
    result = []
    for i in xrange(2, int(sqrt(n)) + 1):
        pwr = 0
        while n % i == 0:
            pwr += 1
            n /= i
        if pwr > 0:
            result.append([i, pwr])
    if n > 1:
        result.append([n, 1])
    return result
