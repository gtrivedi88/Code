File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/projects/app.py", line 10, in <module>
    from routes.view_routes import view_routes
  File "/projects/routes/view_routes.py", line 6, in <module>
    from cache_config import cache
  File "/projects/cache_config.py", line 1, in <module>
    from flask_caching import Cache
ModuleNotFoundError: No module named 'flask_caching'
[2024-07-01 21:43:52 +0000] [9] [INFO] Worker exiting (pid: 9)
[2024-07-01 21:43:52 +0000] [1] [ERROR] Worker (pid:8) exited with code 3
Traceback (most recent call last):
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/arbiter.py", line 209, in run
    self.sleep()
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/arbiter.py", line 360, in sleep
    ready = select.select([self.PIPE[0]], [], [], 1.0)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/arbiter.py", line 242, in handle_chld
    self.reap_workers()
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/arbiter.py", line 530, in reap_workers
    raise HaltServer(reason, self.WORKER_BOOT_ERROR)
gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot.' 3>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/app-root/bin/gunicorn", line 8, in <module>
    sys.exit(run())
             ^^^^^
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/app/wsgiapp.py", line 67, in run
    WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]", prog=prog).run()
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/app/base.py", line 236, in run
    super().run()
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/app/base.py", line 72, in run
    Arbiter(self).run()
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/arbiter.py", line 229, in run
    self.halt(reason=inst.reason, exit_status=inst.exit_status)
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/arbiter.py", line 342, in halt
    self.stop()
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/arbiter.py", line 396, in stop
    time.sleep(0.1)
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/arbiter.py", line 242, in handle_chld
    self.reap_workers()
  File "/opt/app-root/lib64/python3.11/site-packages/gunicorn/arbiter.py", line 530, in reap_workers
    raise HaltServer(reason, self.WORKER_BOOT_ERROR)
gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot.' 3>
