#!/usr/bin/env python
# -*- encoding: utf8 -*-

import socket
import fcntl
import struct

def get_ip_address(ifname):
    """ 获取本机ip """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建udp套接字
    return socket.inet_ntoa(
        fcntl.ioctl(
            s.fileno(),
            0x8915,
            struct.pack('256s', ifname[:15])
        )[20:24]
    )


# print get_ip_address("eth0")
# print get_ip_address("lo")
