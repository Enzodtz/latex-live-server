import logging
import socketio

sio = socketio.Server(cors_allowed_origins="*")
sio_app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    logging.info("New connection created")


@sio.event
def disconnect(sid):
    logging.info("Connection closed")
