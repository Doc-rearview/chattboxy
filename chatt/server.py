import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind(("localhost", 9999))


server.listen()


client, addr = server.accept()
print(f"Connected to {addr}")

done = False

while not done:
   
    data = client.recv(1024).decode("utf-8")
    if data.lower() == 'quit':
        done = True
    else:
        print(f"Client: {data}")

    
    message = input("Server: ")
    client.send(message.encode("utf-8"))
    if message.lower() == 'quit':
        done = True


client.close()
server.close()