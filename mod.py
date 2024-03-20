[2024-03-20 11:57:07 +0530] [2908129] [INFO] Starting gunicorn 21.2.0
[2024-03-20 11:57:07 +0530] [2908129] [INFO] Listening at: http://0.0.0.0:5000 (2908129)
[2024-03-20 11:57:07 +0530] [2908129] [INFO] Using worker: sync
[2024-03-20 11:57:07 +0530] [2908132] [INFO] Booting worker with pid: 2908132
[2024-03-20 11:57:07 +0530] [2908133] [INFO] Booting worker with pid: 2908133
[2024-03-20 11:57:07 +0530] [2908134] [INFO] Booting worker with pid: 2908134
[2024-03-20 11:57:07 +0530] [2908135] [INFO] Booting worker with pid: 2908135
[2024-03-20 11:57:08 +0530] [2908133] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
                ^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
                    ^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
           ^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/util.py", line 424, in import_app
    app = app(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/app.py", line 36, in create_app
    pg_host = os.environ["PGHOST"]
              ~~~~~~~~~~^^^^^^^^^^
  File "<frozen os>", line 685, in __getitem__
KeyError: 'PGHOST'
[2024-03-20 11:57:08 +0530] [2908133] [INFO] Worker exiting (pid: 2908133)
[2024-03-20 11:57:08 +0530] [2908132] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
                ^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
                    ^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
           ^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/util.py", line 424, in import_app
    app = app(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/app.py", line 36, in create_app
    pg_host = os.environ["PGHOST"]
              ~~~~~~~~~~^^^^^^^^^^
  File "<frozen os>", line 685, in __getitem__
KeyError: 'PGHOST'
[2024-03-20 11:57:08 +0530] [2908132] [INFO] Worker exiting (pid: 2908132)
[2024-03-20 11:57:08 +0530] [2908134] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
                ^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
                    ^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
           ^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/util.py", line 424, in import_app
    app = app(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/app.py", line 36, in create_app
    pg_host = os.environ["PGHOST"]
              ~~~~~~~~~~^^^^^^^^^^
  File "<frozen os>", line 685, in __getitem__
KeyError: 'PGHOST'
[2024-03-20 11:57:08 +0530] [2908134] [INFO] Worker exiting (pid: 2908134)
[2024-03-20 11:57:08 +0530] [2908135] [ERROR] Exception in worker process
Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 609, in spawn_worker
    worker.init_process()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 134, in init_process
    self.load_wsgi()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/workers/base.py", line 146, in load_wsgi
    self.wsgi = self.app.wsgi()
                ^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/base.py", line 67, in wsgi
    self.callable = self.load()
                    ^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 58, in load
    return self.load_wsgiapp()
           ^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 48, in load_wsgiapp
    return util.import_app(self.app_uri)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/util.py", line 424, in import_app
    app = app(*args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/app.py", line 36, in create_app
    pg_host = os.environ["PGHOST"]
              ~~~~~~~~~~^^^^^^^^^^
  File "<frozen os>", line 685, in __getitem__
KeyError: 'PGHOST'
[2024-03-20 11:57:08 +0530] [2908135] [INFO] Worker exiting (pid: 2908135)
[2024-03-20 11:57:08 +0530] [2908129] [ERROR] Worker (pid:2908132) exited with code 3
[2024-03-20 11:57:08 +0530] [2908129] [ERROR] Worker (pid:2908133) exited with code 3
[2024-03-20 11:57:08 +0530] [2908129] [ERROR] Worker (pid:2908134) was sent SIGTERM!
[2024-03-20 11:57:08 +0530] [2908129] [ERROR] Worker (pid:2908135) was sent SIGTERM!
Traceback (most recent call last):
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 209, in run
    self.sleep()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 360, in sleep
    ready = select.select([self.PIPE[0]], [], [], 1.0)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 242, in handle_chld
    self.reap_workers()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 530, in reap_workers
    raise HaltServer(reason, self.WORKER_BOOT_ERROR)
gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot.' 3>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/gtrivedi/.local/bin/gunicorn", line 8, in <module>
    sys.exit(run())
             ^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/wsgiapp.py", line 67, in run
    WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]").run()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/base.py", line 236, in run
    super().run()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/app/base.py", line 72, in run
    Arbiter(self).run()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 229, in run
    self.halt(reason=inst.reason, exit_status=inst.exit_status)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 342, in halt
    self.stop()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 396, in stop
    time.sleep(0.1)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 242, in handle_chld
    self.reap_workers()
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/gunicorn/arbiter.py", line 530, in reap_workers
    raise HaltServer(reason, self.WORKER_BOOT_ERROR)
gunicorn.errors.HaltServer: <HaltServer 'Worker failed to boot.' 3>
 ✘ gtrivedi@gtrivedi-thinkpadt14sgen1  ~/git/gitlab/opl-ui   master  
