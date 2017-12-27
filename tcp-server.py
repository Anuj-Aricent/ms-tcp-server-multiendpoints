
import socket
import redis

redis_db = redis.StrictRedis(host=str(os.environ['REDIS_SERVICE_HOST']), port=str(os.environ['REDIS_SERVICE_PORT']))
s = socket.socket()         
host = "0.0.0.0" 
port = 12345
redis_db.set('TCP_HOST', host)
redis_db.set('TCP_PORT', port)
s.bind((host, port))        
userlist = []

s.listen(5)                 
while True:
   c, addr = s.accept()
   if c not in userlist:
       userlist.append(c)     
   print 'Got connection from', addr
   buf = c.recv(1024)
   print "Recieving: " + buf
   print userlist
   for client in userlist:
       client.send(buf)
       print "Sending: " + buf 
   #c.send('Thank you for connecting')
   continue
   c.close()    
