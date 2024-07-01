[2024-07-01 14:39:45 +0000] [1] [INFO] Starting gunicorn 22.0.0
[2024-07-01 14:39:45 +0000] [1] [INFO] Listening at: https://0.0.0.0:5000 (1)
[2024-07-01 14:39:45 +0000] [1] [INFO] Using worker: sync
[2024-07-01 14:39:45 +0000] [8] [INFO] Booting worker with pid: 8
[2024-07-01 14:39:45 +0000] [9] [INFO] Booting worker with pid: 9
[2024-07-01 14:39:45 +0000] [10] [INFO] Booting worker with pid: 10
[2024-07-01 14:39:45 +0000] [11] [INFO] Booting worker with pid: 11
[2024-07-01 14:40:11 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:11 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:20 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:20 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:20 +0000] [8] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:20 +0000] [11] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:20 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:20 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:20 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:21 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:21 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:21 +0000] [11] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:21 +0000] [8] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:26 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:26 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:36 +0000] [8] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:36 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:36 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:36 +0000] [11] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:36 +0000] [8] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:36 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:40:36 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:41:42 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:8)
[2024-07-01 14:41:42 +0000] [8] [ERROR] Error handling request (no URI read)
Traceback (most recent call last):
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/workers/sync.py", line 134, in handle
    req = next(parser)
          ^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/parser.py", line 42, in __next__
    self.mesg = self.mesg_class(self.cfg, self.unreader, self.source_addr, self.req_count)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/message.py", line 257, in __init__
    super().__init__(cfg, unreader, peer_addr)
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/message.py", line 60, in __init__
    unused = self.parse(self.unreader)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/message.py", line 269, in parse
    self.get_data(unreader, buf, stop=True)
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/message.py", line 260, in get_data
    data = unreader.read()
           ^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/unreader.py", line 37, in read
    d = self.chunk()
        ^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/unreader.py", line 64, in chunk
    return self.sock.recv(self.mxchunk)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/ssl.py", line 1296, in recv
    return self.read(buflen)
           ^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/ssl.py", line 1169, in read
    return self._sslobj.read(len)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/workers/base.py", line 203, in handle_abort
    sys.exit(1)
SystemExit: 1
[2024-07-01 14:41:42 +0000] [8] [INFO] Worker exiting (pid: 8)
[2024-07-01 14:41:42 +0000] [14] [INFO] Booting worker with pid: 14
Route accessed with method: GET
[2024-07-01 14:44:28 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:11)
[2024-07-01 14:44:28 +0000] [11] [ERROR] Error handling request (no URI read)
Traceback (most recent call last):
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/workers/sync.py", line 134, in handle
    req = next(parser)
          ^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/parser.py", line 42, in __next__
    self.mesg = self.mesg_class(self.cfg, self.unreader, self.source_addr, self.req_count)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/message.py", line 257, in __init__
    super().__init__(cfg, unreader, peer_addr)
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/message.py", line 60, in __init__
    unused = self.parse(self.unreader)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/message.py", line 269, in parse
    self.get_data(unreader, buf, stop=True)
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/message.py", line 260, in get_data
    data = unreader.read()
           ^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/unreader.py", line 37, in read
    d = self.chunk()
        ^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/http/unreader.py", line 64, in chunk
    return self.sock.recv(self.mxchunk)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/ssl.py", line 1296, in recv
    return self.read(buflen)
           ^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/ssl.py", line 1169, in read
    return self._sslobj.read(len)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/workers/base.py", line 203, in handle_abort
    sys.exit(1)
SystemExit: 1
[2024-07-01 14:44:28 +0000] [11] [INFO] Worker exiting (pid: 11)
[2024-07-01 14:44:28 +0000] [17] [INFO] Booting worker with pid: 17
[2024-07-01 14:44:30 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:44:30 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:44:30 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:44:33 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:44:33 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:44:33 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:44:33 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:44:34 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:44:34 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:44:34 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:35 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:35 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
Route accessed with method: GET
[2024-07-01 14:45:41 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:45 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:45 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:45 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:45 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:45 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:45 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:46 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:46 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:46 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:46 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:46 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:47 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:47 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:47 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:47 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:47 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:47 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:47 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:47 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:48 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:48 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:48 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:48 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:50 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:50 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:53 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:53 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:53 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:53 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:53 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:53 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:53 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:45:53 +0000] [14] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
Route accessed with method: GET
[2024-07-01 14:46:19 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:22 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:22 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:22 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:23 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:23 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:23 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:23 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:27 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:27 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:29 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:29 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:29 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:29 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:29 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:29 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:46:29 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
Route accessed with method: POST
New Aliases Data: {}
[2024-07-01 14:47:08 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:08 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
Route accessed with method: GET
/projects/routes/edit_routes.py:272: SAWarning: Identity map already had an identity for (<class 'models.ProductReferences'>, ('cbb35c75-1425-4f98-9241-21d3b0eb0e17',), None), replacing it with newly flushed object.   Are there load operations occurring inside of an event handler within the flush?
  existing_component_ids = [component.component_id for component in product.components]
[2024-07-01 14:47:21 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:21 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:21 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:21 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:21 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:21 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:21 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:21 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:22 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:22 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:22 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:22 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:22 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:22 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:22 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:22 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:23 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:47:27 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:14)
[2024-07-01 14:47:27 +0000] [14] [ERROR] Error handling request /opl/edit-product/cbb35c75-1425-4f98-9241-21d3b0eb0e17
Traceback (most recent call last):
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/workers/sync.py", line 135, in handle
    self.handle_request(listener, req, client, addr)
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/workers/sync.py", line 178, in handle_request
    respiter = self.wsgi(environ, resp.start_response)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/flask/app.py", line 2486, in __call__
    return self.wsgi_app(environ, start_response)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/flask/app.py", line 2463, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/flask/app.py", line 1758, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/flask/app.py", line 1734, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/flask_principal.py", line 199, in _decorated
    rv = f(*args, **kw)
         ^^^^^^^^^^^^^^
  File "/projects/routes/edit_routes.py", line 344, in edit_product_details
    product_references = ProductReferences.query.filter_by(product_id=product_id).all()
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/orm/query.py", line 2773, in all
    return self._iter().all()
           ^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/orm/query.py", line 2916, in _iter
    result = self.session.execute(
             ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/orm/session.py", line 1717, in execute
    result = conn._execute_20(statement, params or {}, execution_options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/base.py", line 1710, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/sql/elements.py", line 334, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/base.py", line 1577, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/base.py", line 1953, in _execute_context
    self._handle_dbapi_exception(
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/base.py", line 2138, in _handle_dbapi_exception
    util.raise_(exc_info[1], with_traceback=exc_info[2])
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/util/compat.py", line 211, in raise_
    raise exception
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/base.py", line 1910, in _execute_context
    self.dialect.do_execute(
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/default.py", line 736, in do_execute
    cursor.execute(statement, parameters)
  File "/opt/app-root/lib64/python3.11/site-packages/redshift_connector/cursor.py", line 239, in execute
    self._c.execute(self, "begin transaction", None)
  File "/opt/app-root/lib64/python3.11/site-packages/redshift_connector/core.py", line 1990, in execute
    self.handle_messages(cursor)
  File "/opt/app-root/lib64/python3.11/site-packages/redshift_connector/core.py", line 2178, in handle_messages
    buffer = self._read(5)
             ^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/socket.py", line 706, in readinto
    return self._sock.recv_into(b)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/ssl.py", line 1315, in recv_into
    return self.read(nbytes, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/ssl.py", line 1167, in read
    return self._sslobj.read(len, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/workers/base.py", line 203, in handle_abort
    sys.exit(1)
SystemExit: 1
[2024-07-01 14:47:27 +0000] [14] [INFO] Worker exiting (pid: 14)
[2024-07-01 14:47:28 +0000] [19] [INFO] Booting worker with pid: 19
[2024-07-01 14:49:00 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:00 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:00 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:00 +0000] [19] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:02 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:06 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:17 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:17 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:17 +0000] [19] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:17 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:17 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:17 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:17 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:18 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:18 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:18 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:18 +0000] [19] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:47 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:47 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
Route accessed with method: GET
[2024-07-01 14:49:58 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [19] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [19] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [19] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:58 +0000] [10] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:49:59 +0000] [17] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:50:05 +0000] [9] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
[2024-07-01 14:50:05 +0000] [19] [WARNING] Invalid request from ip=10.128.2.2: [SSL: SSLV3_ALERT_CERTIFICATE_UNKNOWN] sslv3 alert certificate unknown (_ssl.c:2580)
Route accessed with method: POST
New Aliases Data: {}
[2024-07-01 14:50:35 +0000] [1] [CRITICAL] WORKER TIMEOUT (pid:19)
[2024-07-01 14:50:35 +0000] [19] [ERROR] Error handling request /opl/edit-product/fc884b2d-6ff8-40e8-a75e-0f937e5a885c
Traceback (most recent call last):
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/workers/sync.py", line 135, in handle
    self.handle_request(listener, req, client, addr)
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/workers/sync.py", line 178, in handle_request
    respiter = self.wsgi(environ, resp.start_response)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/flask/app.py", line 2486, in __call__
    return self.wsgi_app(environ, start_response)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/flask/app.py", line 2463, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/flask/app.py", line 1758, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/flask/app.py", line 1734, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/flask_principal.py", line 199, in _decorated
    rv = f(*args, **kw)
         ^^^^^^^^^^^^^^
  File "/projects/routes/edit_routes.py", line 347, in edit_product_details
    form.product_id.choices = [('', 'Select')] + [(str(prod.product_id), prod.product_name) for prod in Product.query.order_by(Product.product_name).all()]
                                                                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/orm/query.py", line 2773, in all
    return self._iter().all()
           ^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/orm/query.py", line 2916, in _iter
    result = self.session.execute(
             ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/orm/session.py", line 1717, in execute
    result = conn._execute_20(statement, params or {}, execution_options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/base.py", line 1710, in _execute_20
    return meth(self, args_10style, kwargs_10style, execution_options)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/sql/elements.py", line 334, in _execute_on_connection
    return connection._execute_clauseelement(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/base.py", line 1577, in _execute_clauseelement
    ret = self._execute_context(
          ^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/base.py", line 1953, in _execute_context
    self._handle_dbapi_exception(
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/base.py", line 2138, in _handle_dbapi_exception
    util.raise_(exc_info[1], with_traceback=exc_info[2])
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/util/compat.py", line 211, in raise_
    raise exception
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/base.py", line 1910, in _execute_context
    self.dialect.do_execute(
  File "/opt/app-root/lib64/python3.11/site-packages/sqlalchemy/engine/default.py", line 736, in do_execute
    cursor.execute(statement, parameters)
  File "/opt/app-root/lib64/python3.11/site-packages/redshift_connector/cursor.py", line 241, in execute
    self._c.execute(self, operation, args)
  File "/opt/app-root/lib64/python3.11/site-packages/redshift_connector/core.py", line 1990, in execute
    self.handle_messages(cursor)
  File "/opt/app-root/lib64/python3.11/site-packages/redshift_connector/core.py", line 2194, in handle_messages
    self.message_types[code](self._read(data_len - 4), cursor)
                             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/socket.py", line 706, in readinto
    return self._sock.recv_into(b)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/ssl.py", line 1315, in recv_into
    return self.read(nbytes, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/ssl.py", line 1167, in read
    return self._sslobj.read(len, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/workers/base.py", line 203, in handle_abort
    sys.exit(1)
SystemExit: 1
[2024-07-01 14:50:35 +0000] [19] [INFO] Worker exiting (pid: 19)
[2024-07-01 14:50:35 +0000] [21] [INFO] Booting worker with pid: 21
