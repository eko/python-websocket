from websocket import config, wsserver

# Runs server
print 'Starting server on port %s. Waiting for connections...' % config.socket_port
wsserver.Server().run()