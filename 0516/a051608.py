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
                # print(response)
            else:
                break
        return returnvalues.decode()
import time
start=time.time()
import threading
t1=threading.Thread(target=get_html)
t1.start()
t1.join()
t2=threading.Thread(target=get_html)
t2.start()

t2.join()
print(time.time()-start)
