
import socket     
import select
import redis          

s = socket.socket()         
host = "0.0.0.0" 
port = 12345                
s.bind((host, port))        
userlist = []

s.listen(5)
CONNECTION_LIST = []
CONNECTION_LIST.append(s)                 
while True:
   read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
   
   for sock in read_sockets:
        #New connection
        if sock == s:
            # Handle the case in which there is a new connection recieved through server_socket
            c, addr = s.accept()
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
