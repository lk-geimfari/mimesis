"""Provides platforms."""

# https://docs.python.org/3.5/library/sys.html?highlight=sys#sys.platform
PLATFORMS = {
    'LINUX': {
        'name': 'linux',
        'path_separator': '/',
        'root': '/',
        'home': '/home/',
    },
    'MACOS': {
        'name': 'darwin',
        'path_separator': '/',
        'root': '/',
        'home': '/home/',
    },
    'WINDOWS': {
        'name': 'win32',
        'path_separator': '\\',
        'root': 'C:\\',
        'home': 'C:\\Users\\',
    },
    'WINDOWS64': {
        'name': 'win64',
        'path_separator': '\\',
        'root': 'C:\\',
        'home': 'C:\\Users\\',
    },
}
