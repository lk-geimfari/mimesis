# -*- coding: utf-8 -*-

"""Provides all the data for Structure."""

CSS_PROPERTIES = {
    'background-color': 'color',
    'border-color': 'color',
    'color': 'color',
    'display': [
        'block',
        'none',
        'inline',
    ],
    'font-size': 'size',
    'font-style': [
        'inherit',
        'initial',
        'italic',
        'normal',
        'oblique',
    ],
    'position': [
        'absolute',
        'fixed',
        'inherit',
        'initial',
        'relative',
        'static',
    ],
    'margin-bottom': 'size',
    'margin-left': 'size',
    'padding-right': 'size',
    'padding-top': 'size',
    'pointer': [
        'crosshair',
        'help',
        'pointer',
        'progress',
    ],
    'text-align': [
        'center',
        'inherit',
        'initial',
        'justify',
        'left',
        'right',
    ],
    'width': 'size',
}

CSS_SELECTORS = [
    '.',
    '#',
]

CSS_SIZE_UNITS = [
    'em',
    'pt',
    'px',
]

HTML_CONTAINER_TAGS = {
    'a': {
        'class': 'word',
        'href': 'url',
        'id': 'word',
        'style': 'css',
        'target': [
            '_blank',
            '_parent',
            '_top',
        ],
    },
    'div': {
        'class': 'word',
        'id': 'word',
        'style': 'css',
    },
    'p': {
        'class': 'word',
        'id': 'word',
        'style': 'css',
    },
    'span': {
        'class': 'word',
        'id': 'word',
        'style': 'css',
    },
}

HTML_MARKUP_TAGS = [
    'b',
    'em',
    'i',
    'small',
    'strong',
]
