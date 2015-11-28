#server code
import sys
import time
import select
import socket

address = (‘localhost’, 8888)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.connect(address)
input = [client, sys.stdin]
while true:
    input_data, output_data, except_data = select.select(input, [], [])
    for receive_data in input_data:
        if receive_data in input_data:
            data = client.recv(1024)
            if data == ‘^c”:
                running = 0
                print ‘server exit’
                receive_data.close()
                break
            print “<server sent data>” , data
            else:
                client_data = raw_input()
                client.send(“sending time: %s: \n%” %(time.ctime(), data))
client.close()