import socket
import threading
import random
import judgement as J
from queue import Queue
from util import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((HOST,PORT))
server.listen(BACKLOG)
print("looking for connection")

def sendClientMsg(cID, *msg):
	msg = DATA_SEP.join(msg) + MSG_SEP
	clientele[cID].send(msg.encode())
	
def broadcastMsg(*msg):
	for id, client in clientele:
		sendClientMsg(id, *msg)

def getSingleMsg(cID):
	client = clientele[cID]
	client.setblocking(1)
	msg = ""
	while True:
		try:
			msg += client.recv(MSG_LEN).decode("UTF-8")
			msgs = msg.split(MSG_SEP) 
			if (len(msgs) > 1): #if we have at least one complete command
				return msgs[0]


# def handleClient(client, serverChannel, cID, clientele): # handles rcvd messages from a specific client
# 	client.setblocking(1)
# 	msg = ""
# 	while True:
# 		try:
# 			msg += client.recv(MSG_LEN).decode("UTF-8")
# 			command = msg.split(MSG_SEP) 
# 			while (len(command) > 1): #if we have at least one complete command
# 				readyMsg = command[0] 
# 				msg = MSG_SEP.join(command[1:]) #the rest is shit that begins the next msg
# 				serverChannel.put(str(cID) + DATA_SEP + readyMsg) # send msg str for processing
# 				command = msg.split(MSG_SEP) #go to next command (if there is one)
# 		except: 
# 			clientele.pop(cID)
# 			return

# def serverThread(clientele, serverChannel): #processes messages recieved from all clients
# 	peopleReady = 0
# 	while True:
# 		msg = serverChannel.get(True, None) 
# 		dbSock("msgRcvd-->", msg) 
# 		senderID, msgList = int(msg.split(DATA_SEP)[0]), msg.split(DATA_SEP)[1:] #separates id from msg
# 		if (msg):
# 			command = msgList[0]
# 			# case command on all stateful server actions
# 			# if command=="forward":
# 			# 	dbInf ("Player" + str(senderID) + " moved forward!")
# 			# 	for cID in clientele: #for each client
# 			# 		if cID != senderID: #if client not the sender
# 			# 			sendClientMsg(cID, "forward", str(senderID)) #encode and send message to all other players!

# 		serverChannel.task_done()

clientele = {}
currID = 0

# serverChannel = Queue(100) 
# threading.Thread(target = serverThread, args = (clientele, serverChannel)).start()

while True: #loop for adding clients
	client, address = server.accept()
	
	clientele[currID] = client 
	J.new_player(cID)
	print("connection received")
	# threading.Thread(target = handleClient, args =  #create a new thread to listen on this client
	# 											(client ,serverChannel, currID, clientele)).start()
	currID += 1