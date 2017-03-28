import socket


def is_connected():
    try:
        host = socket.gethostbyname('https://github.com/')
        socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False
