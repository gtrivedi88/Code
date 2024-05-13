 gtrivedi@gtrivedi-thinkpadt14sgen1  ~/git/gitlab/opl-ui   master  flask -e environment run --cert=adhoc
Traceback (most recent call last):
  File "/home/gtrivedi/.local/bin/flask", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/cli.py", line 1064, in main
    cli.main()
  File "/usr/lib/python3.12/site-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/click/core.py", line 1688, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/click/decorators.py", line 92, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/cli.py", line 912, in run_command
    raise e from None
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/cli.py", line 898, in run_command
    app = info.load_app()
          ^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/cli.py", line 313, in load_app
    app = locate_app(import_name, None, raise_if_not_found=False)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/cli.py", line 236, in locate_app
    return find_best_app(module)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask/cli.py", line 64, in find_best_app
    app = app_factory()
          ^^^^^^^^^^^^^
  File "/home/gtrivedi/git/gitlab/opl-ui/app.py", line 47, in create_app
    flask_saml.FlaskSAML(app)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask_saml.py", line 104, in __init__
    self.init_app(app)
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask_saml.py", line 112, in init_app
    'metadata': _get_metadata(
                ^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/flask_saml.py", line 27, in _get_metadata
    response = requests.get(metadata_url)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/requests/adapters.py", line 517, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='sso-taxman.apps.ccstaxman.lab.psi.pnq2.redhat.com', port=443): Max retries exceeded with url: /auth/realms/RHTest/protocol/saml/descriptor (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1000)')))
