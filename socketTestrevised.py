import socket, sys, _thread, time
def recvDat(client):
    global dat
    while True:
        while True:
            data = client.recv(1024)
            if not data:
                break
            dat = [data, time.time()]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 5005))
#print "Server IP: %s" %socket.gethostbyname(socket.gethostname())
s.listen(5)
(clientsocket, address) = s.accept()
#print "Accepted connection from %s" %address
dat = [None, time.time()]
_thread.start_new_thread(recvDat, (clientsocket,))

while True:
    data = dat[0]
    stamp = dat[1]
    if not data:
        print("Not recieved anything yet!")
    else:
        if time.time() - stamp > 1.5:
            print("Data stale! (More than 1.5 seconds since we recieved data)")
        else:
            print(data)
            print("data age: %s seconds" %(time.time() - stamp))
    time.sleep(1)
def end_program(*args):
    s.close()
