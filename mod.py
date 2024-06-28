 timestamp = signer.unsign(
                         ^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/itsdangerous/timed.py", line 95, in unsign
    result = super().unsign(signed_value)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/gtrivedi/.local/lib/python3.12/site-packages/itsdangerous/signer.py", line 239, in unsign
    if self.sep not in signed_value:
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: argument of type 'CSRFTokenField' is not iterable
