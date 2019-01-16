# -*- coding: utf-8 -*-

"""Provides all the data related to science."""

MATH_FORMULAS = [
    'A = (ab)/2',
    'A = a2',
    'A = ab',
    'A = (h(a + b))/2',
    'V = (Ah)/3',
    'xn + xm = x(n + m)',
    '(xn)/(xm) = x^n - m',
    '(x/y)^n = (x^n)/(y^n)',
    'x^n*y^n = (xy)^n',
    'ax2 + bx + c = 0.',
    '(a/b)/(c/d) = (a/b) * (d/c)',
    'π = pi = 3.1415',
    'A = πr^2',
    'P = 4l',
    'V = πr^2*h',
    'V - E + F = 2',
]

SI_PREFIXES = {
    'negative': [
        'deci',
        'centi',
        'milli',
        'micro',
        'nano',
        'pico',
        'femto',
        'atto',
        'zepto',
        'yocto',
    ],
    'positive': [
        'yotta',
        'zetta',
        'exa',
        'peta',
        'tera',
        'giga',
        'mega',
        'kilo',
        'hecto',
        'deca',
    ],
}

SI_PREFIXES_SYM = {
    'negative': ['d', 'c', 'm', 'μ', 'n',
                 'p', 'f', 'a', 'z', 'y'],
    'positive': ['Y', 'Z', 'E', 'P', 'T',
                 'G', 'M', 'k', 'h', 'da'],
}
