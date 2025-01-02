import socket
import tkinter as tk
from tkinter import filedialog
import threading












def person2_gui(client):
    root = tk.Tk()
    root.title("Person 2 - Chatboxxy")
    root.configure(bg="black")

    chat_frame = tk.Frame(root, bg="black")
    chat_frame.pack(pady=10)

    chat_window = tk.Text(chat_frame, bg="black", fg="red", width=50, height=20)
    chat_window.pack()

    input_frame = tk.Frame(root, bg="black")
    input_frame.pack(pady=10)

    entry = tk.Entry(input_frame, width=40, bg="black", fg="red")
    entry .pack(side=tk.LEFT)

    send_button = tk.Button(input_frame, text="Send", bg="red", fg="black", command=lambda: send_message(entry, chat_window, client))
    send_button.pack(side=tk.LEFT)

    file_button = tk.Button(input_frame, text="Send File", bg="red", fg="black", command=lambda: send_file(client, chat_window))
    file_button.pack(side=tk.LEFT)

    
    threading.Thread(target=receive_messages, args=(client, chat_window), daemon=True).start()

    root.mainloop()






def send_message(entry, chat_window, client):
    message = entry.get()
    chat_window.insert(tk.END, f"You: {message}\n")
    client.send(message.encode("utf-8"))
    entry.delete(0, tk.END)


def send_file(client, chat_window):
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "rb") as file:
            file_data = file.read()
            client.sendall(b"FILE:" + file_data)
        chat_window.insert(tk.END, f"You sent a file: {file_path}\n")

def receive_messages(client, chat_window):
    while True:
        data = client.recv(1024)
        if not data:
            break
        if data.startswith(b"FILE:"):
            file_data = data[5:]
            with open("received_file", "wb") as file:
                file.write(file_data)
            chat_window.insert(tk.END, "Person 1 sent you a file: 'received_file'\n")
        else:
            chat_window.insert(tk.END, f"Person 1: {data.decode('utf-8')}\n")

############################ Start Person 2 (Client)
def start_person2():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))
    print("Person 2 connected to Person 1.")

    
    person2_gui(client)

    client.close()
start_person2()
