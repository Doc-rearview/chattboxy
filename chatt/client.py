import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect(("localhost", 9999))

done = False

while not done:
   
    message = input("Client: ")
    client.send(message.encode("utf-8"))
    if message.lower() == 'quit':
        done = True

   
    data = client.recv(1024).decode("utf-8")
    if data.lower() == 'quit':
        done = True
    else:
        print(f"Server: {data}")


client.close()