import socket
def get_html():
    with socket.socket() as s:
        s.connect(('127.0.0.1',5000))
        s.sendall((b'GET /?a=1&b=3 HTTP/1.0\n\n'))
        returnvalues=''
        while True:
            response=s.recv(4096)
            if response:
                returnvalues=response
                print(response)
            else:
                break
        return returnvalues.decode()
import time
start=time.time()
print('get_html',get_html())
print('get_html',get_html())
print(time.time()-start)
