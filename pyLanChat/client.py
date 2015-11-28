# client
import sys
import time
import select
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((‘localhost’, 8888)     # define your own bind IP and port.
            server.listen(10)
            input = [server, sys.stdin]     # take keyboard input
            client, address = server.accept()     # get the client IP address
            input.append(client)             # add client to list
while true:
            input_data, out_data, except_data = select.select(input, [], []) # select monitor the input data stream
      for receive_data in input_data
            if receive_data = sys.stdin       # server input
                data = raw_input()
            if data == ‘^c’:
                running = 0
                client.send(data)   #send data to server
                client.close()
                break;
                client.send(“sending time: %s: \n%” %(time.ctime(), data))
            else:
                data = receive_data.recv(1024)    # get a line of characters
                print “<client sent>”, data
server.close()
