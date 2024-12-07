import socket

HOST = (socket.gethostname(), 10000)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(HOST)
s.listen()
print('I am listening your connections')


while True:
    conn, addr = s.accept()
    print(f'Connected - {addr}')
    res = b'Hello, my friend'
    conn.send(res)

    # https://www.youtube.com/watch?v=9ZxeUaOqRUM&list=PLe-iIMbo5JOLBc4ioQv0-mHH2vX7Y6zZk&index=2