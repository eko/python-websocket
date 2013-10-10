Python WebSocket server
=======================

This is a simple Python websocket server

Installation
------------

Clone the project by typing

```bash
$ git clone git@github.com:eko/python-websocket.git
```

Then simply run:

```bash
$ python run.py
```

Output should be like this:

```bash
$ python run.py
Starting server on port 9998. Waiting for connections...
('New client connected', ('127.0.0.1', 50993))
('New client connected', ('127.0.0.1', 50994))
('Data from', ('127.0.0.1', 50994), ':', '\x81\x86\x08W\x88\xad@2\xe4\xc1gv')
('Data from', ('127.0.0.1', 50993), ':', '\x81\x86\x01\x02\xa3\xe1Ig\xcf\x8dn#')
```