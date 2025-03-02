import ollama
from ollama import chat
from ollama import ChatResponse
import json
from tkinter import *

models = []
system_msg = {
    'role': 'system',
    'content': 'You are a helpful feline assistant named Sherman who is a Birman',
}
messages = [system_msg]

main = Tk()
main.minsize(500, 500)
main.title('ShermintGPT')
logo = PhotoImage(file='/Users/dog/ShermIntGPT/ShermintGPT_logo.png')
main.iconphoto(False, logo)

def run_model():
        
        tVal = t.get("1.0", "end")
        prompt = t.get("1.0", "end")
        model = lb.get(lb.curselection()[0])

        messages.append({"role": "user", "content": prompt})
        response = ollama.chat(model=model, messages=messages)
        response_content = response.message.content

        t2.config(state=NORMAL)
        t2.delete("1.0", "end")
        t2.insert("1.0", response_content)
        t2.config(state=DISABLED)

        messages.append({"role": "assistant", "content": response_content})

def reset_chat():

        messages.clear()
        messages.append(system_msg)

def get_models():
        
        ret = ollama.list()
        models = [x.model for x in ret.models]
        lb.delete(0, END)
        lb.insert(0, *models)

def pull_model():
        
        ModelToPull = e.get()
        ollama.pull(ModelToPull)
        get_models()

def delete_model():
        
        ModelToDelete = e.get()
        ollama.delete(ModelToDelete)
        get_models()

t = Text()
t.grid(row=0, column=0)

t2 = Text(state=DISABLED)
t2.grid(row=0, column=2)

lb = Listbox(exportselection=False)
lb.grid(row=0, column=1)
get_models()

b = Button(text='Run', command=run_model)
b.grid(row=1, column=0)

e = Entry()
e.grid(row=1, column=2)

b2 = Button(text='Pull model', command=pull_model)
b2.grid(row=2, column=2)

b3 = Button(text='Delete model', command=delete_model)
b3.grid(row=3, column=2)

b4 = Button(text='Reset chat', command=reset_chat)
b4.grid(row=2, column=0)

main.mainloop()
