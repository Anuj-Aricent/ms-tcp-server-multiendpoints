
import socket     
import select         

s1 = socket.socket()
s2 = socket.socket()
host = "0.0.0.0" 
port1 = 12345
port2 = 12346
s1.bind((host, port1))
s2.bind((host, port2))
userlist = []

s1.listen(5)
s2.listen(5)
CONNECTION_LIST = []
CONNECTION_LIST.append(s1)
CONNECTION_LIST.append(s2)
while True:
   read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
   
   for sock in read_sockets:
        #New connection
        if sock == s1:
            # Handle the case in which there is a new connection recieved through server_socket
            c, addr = s1.accept()
            CONNECTION_LIST.append(c)
            print "Client (%s, %s) connected" % addr
            if c not in userlist:
                userlist.append(c)
        elif sock == s2:
            # Handle the case in which there is a new connection recieved through server_socket
            c, addr = s2.accept()
            CONNECTION_LIST.append(c)
            print "Client (%s, %s) connected" % addr
            if c not in userlist:
                userlist.append(c)
                 
        else:
            # Data recieved from client, process it
            try:
                data = sock.recv(1024)
                if data:
                    for client in userlist:
                        client.send(data)
                        print "Sending: " + data
                 
            except:
                print "Client (%s, %s) is offline" % addr
                sock.close()
                CONNECTION_LIST.remove(sock)
                continue
