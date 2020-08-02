#############################
# Sockets Client Demo
# by Rohan Varma
# adapted by Kyle Chin
# updated by Ping-Ya Chao
#############################

import socket
import threading
from queue import Queue

from cmu_112_graphics import *
from tkinter import *
import random
from util import *


##########################################
# customize the functions within MyApp
##########################################

class MyApp(App):
    ## 2 new functions specific to sockets! ##
    @staticmethod
    def setUpServer():

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((HOST, PORT))
        print("connected to server")

        serverMsg = Queue(100)
        threading.Thread(target=MyApp.handleServerMsg, args=(server, serverMsg)).start()

        return server, serverMsg

    @staticmethod
    def handleServerMsg(server, serverMsg):
        server.setblocking(1)
        msg = ""
        command = ""
        while True:
            msg += server.recv(128).decode("UTF-8")
            command = msg.split(MSG_SEP)
            while len(command) > 1:
                readyMsg = command[0]
                msg = MSG_SEP.join(command[1:])
                serverMsg.put(readyMsg)
                command = msg.split(MSG_SEP)
    
    @staticmethod
    def sendServerMsg(msg):
        msg += MSG_SEP
        self.server.send(msg.encode())

    ## You've seen the remaining function structure in the 112 animation framework! ##
    def appStarted(self):
        self.server, self.serverMsg = self.setUpServer()
        ## client side state storage

    ## update game state based on events and send client events to server
    def keyPressed(self, event):
        pass

    def mousePressed(self, event):
        pass

    # timerFired receives instructions and executes them
    def timerFired(self):
        while self.serverMsg.qsize() > 0:
            msg = self.serverMsg.get(False)
            try:
                print("received: " + msg)
                msg = msg.split(DATA_SEP)
                command = msg[0]

                ## update model based on commands recieved

            except:
                print("failed")
            self.serverMsg.task_done()

    def redrawAll(self, canvas):
        pass
        ## create client view (cli or visual)
        

MyApp(width=500, height=500)