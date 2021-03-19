#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# TCP Servers & Client

import socket as skt

def create_tcp_socket():
    svr = skt.socket(skt.AF_INET,skt.SOCK_STREAM)
    host_ip = "192.168.0.108"
    port = 16999
    svr.bind((host_ip,port))
    svr.listen(1)
    cfd,client_ip = svr.accept()
    print ("客户端地址:=>",client_ip)
    str = "hellow client!"
    cfd.send(str.encode(encoding="utf-8"))
    cfd.close()

create_tcp_socket()
