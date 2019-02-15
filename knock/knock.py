# -*- coding: utf-8 -*-

"""Main module.
SOURCE: https://stackoverflow.com/questions/19196105/python-how-to-check-if-a-network-port-is-open-on-linux
CREDIT: Michael @ answered Feb 12 '16 at 18:46
"""
from contextlib import closing
import socket


def port_is_open(host, port, timeout=2, max_errors=10):

    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(timeout)
        if sock.connect_ex((host, port)) == 0:
            return True
        else:
            return False
