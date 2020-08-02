## shared constants and helpers between client and server

HOST = ""  # put your IP address here if playing on multiple computers
PORT = 50003
BACKLOG = 4

DATA_SEP = "_"
MSG_SEP = "\n"
MSG_LEN = 128

def dbInf(*whatever):
	debug = False
	if debug:
		print(*whatever)

def dbSock(*whatever):
	debug = True
	if debug:
		print(*whatever)