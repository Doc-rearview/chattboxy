import tkinter as tk
from tkinter import Scrollbar, Text
import google.generativeai as genai
import os

#Tokens or lexical units are the smallest fractions in the python programme. 
# A token is a set of one or more characters having a meaning together
# to make a project -> documentation is very important.
# text is the ques.




#########   send and receive 
def send_message():
    user_message = user_input.get("1.0", tk.END).strip()
    if user_message:
        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, f"You: {user_message}\n", "user_message")
        chat_log.config(state=tk.DISABLED)
        user_input.delete("1.0", tk.END)
        try:
            
            genai.configure(api_key="AIzaSyDbYFrawCr3lA-Nn2ubnf6sRi77HdJS4CM")


            generation_cofig = {"temperature": 0.9, "top_p":1, "top_k":1, "max_output_tokens": 2048}

            model = genai.GenerativeModel("gemini-pro", generation_config=generation_cofig)

            response = model.generate_content(user_message)

            res=response.text
            bot_response = response.text 
        except Exception as e:
            bot_response = f"Error: {e}"

        chat_log.config(state=tk.NORMAL)
        chat_log.insert(tk.END, f"AI: {bot_response}\n", "ai_response")
        chat_log.config(state=tk.DISABLED)
        chat_log.yview(tk.END)


def create_chat_gui():
    global chat_log, user_input

    
    window = tk.Tk()
    window.title("chatbot--boxxy")

   
    chat_log = Text(window, wrap=tk.WORD, state=tk.DISABLED, height=20, width=60, bg="lightgray")
    chat_log.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
    chat_log.tag_config("user_message", foreground="blue")
    chat_log.tag_config("ai_response", foreground="green")
    ############### Scrollbar
    scrollbar = Scrollbar(window, command=chat_log.yview)
    scrollbar.grid(row=0, column=2, sticky="ns")
    chat_log["yscrollcommand"] = scrollbar.set

   ###### #############input 
    user_input = Text(window, wrap=tk.WORD, height=5, width=50, bg="white")
    user_input.grid(row=1, column=0, padx=10, pady=10)
    send_button = tk.Button(window, text="Send", command=send_message)
    send_button.grid(row=1, column=1, padx=10, pady=10)
    
    window.mainloop()


if __name__ == "__main__":
    create_chat_gui()
