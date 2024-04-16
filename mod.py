 File "/home/gtrivedi/.local/lib/python3.12/site-packages/werkzeug/serving.py", line 326, in execute
    write(data)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/werkzeug/serving.py", line 301, in write
    self.wfile.write(data)
  File "/usr/lib64/python3.12/socketserver.py", line 840, in write
    self._sock.sendall(b)
  File "/usr/lib64/python3.12/ssl.py", line 1211, in sendall
    v = self.send(byte_view[count:])
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.12/ssl.py", line 1180, in send
    return self._sslobj.write(data)
           ^^^^^^^^^^^^^^^^^^^^^^^^
ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:2406)
