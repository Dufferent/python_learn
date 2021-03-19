#!/usr/bin/python3

# TCP Servers & Client

import socket as skt

def create_client():
    client = skt.socket()
    toip = "192.168.0.108"
    port = 16999
    client.connect((toip,port))
    print (client.recv(1024))

create_client()