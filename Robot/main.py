#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

ev3 = EV3Brick()
ev3.speaker.beep()

server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)

# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')

# In this program, the server waits for the client to send the first message
# and then sends a reply.
mbox.wait()
print(mbox.read())
mbox.send('hello to you!')

