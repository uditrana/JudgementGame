import socket
import threading
import random
from judgement import *
from queue import Queue

HOST = ""  # put your IP address here if playing on multiple computers
PORT = 50003
BACKLOG = 4

dataSep = "_"
msgSep = "\n"

def dbInf(*whatever):
	debug = False
	if debug:
		print(*whatever)

def dbSock(*whatever):
	debug = True
	if debug:
		print(*whatever)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((HOST,PORT))
server.listen(BACKLOG)
print("looking for connection")

def handleClient(client, serverChannel, cID, clientele): # handles rcvd messages from a specific client
	client.setblocking(1)
	msg = ""
	while True:
		try:
			msg += client.recv(128).decode("UTF-8")
			command = msg.split(msgSep) 
			while (len(command) > 1): #if we have at least one complete command
				readyMsg = command[0] 
				msg = msgSep.join(command[1:]) #the rest is shit that begins the next msg
				serverChannel.put(str(cID) + dataSep + readyMsg) # send msg str for processing
				command = msg.split(msgSep) #go to next command (if there is one)
		except: 
			clientele.pop(cID)
			return

def serverThread(clientele, serverChannel): #processes messages recieved from all clients
	peopleReady = 0
	while True:
		msg = serverChannel.get(True, None) 
		dbSock("msgRcvd-->", msg) 
		senderID, msgList = int(msg.split(dataSep)[0]), msg.split(dataSep)[1:] #separates id from msg
		if (msg):
			action = msgList[0]
			if action=="forward":
				dbInf ("Player" + str(senderID) + " moved forward!")
				for cID in clientele: #for each client
					if cID != senderID: #if client not the sender
						sendMsg = "forward:"+str(senderID)+dataSep+msgSep #create message to all other players!
						clientele[cID].send(sendMsg.encode()) #encode and send
			elif action=="backward":
				dbInf ("Player_" + str(senderID) + " moved backward!")
				for cID in clientele: #for each client
					if cID != senderID: #if client not the sender
						sendMsg = "backward:"+str(senderID)+dataSep+msgSep #create message to all other players!
						clientele[cID].send(sendMsg.encode()) 
		serverChannel.task_done()

def sendStart():
	msg = "start:"+msgSep
	for cID in clientele:
		clientele[cID].send(msg.encode())

clientele = {}
currID = 0

serverChannel = Queue(100) #initialize Q
threading.Thread(target = serverThread, args = (clientele, serverChannel)).start()
#start_new_thread(serverThread, (clientele, serverChannel))

while True: #loop for adding clients
	client, address = server.accept()
	# dbInf(currID) #curr client ID
	x,y,ang = position(currID) #get the position of new tank
	print(x)
	print (y)
	print (ang)
	client.send(("player:%d:%d:%d:%d"+msgSep %(currID,x,y,ang)).encode()) #send player info!
	for cID in clientele: #tell all other peoples that there is a new player!
		print (repr(cID), repr(currID))
		clientele[cID].send(("newPlayer:%d:%d:%d:%d"+msgSep %(currID,x,y,ang)).encode()) #send new player info!
		x,y,ang = position(cID) #get the position of other tanks
		client.send(("newPlayer:%d:%d:%d:%d"+msgSep %(cID,x,y,ang)).encode()) #tell the new player about all the old players
	clientele[currID] = client #adds a client object to dict?
	print("connection received")
	threading.Thread(target = handleClient, args =  #create a new thread for this new client
												(client ,serverChannel, currID, clientele)).start()
	currID += 1