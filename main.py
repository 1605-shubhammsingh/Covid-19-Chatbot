from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import pandas as pd

# Initialize the audio library
engine = pp.init()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()

bot = ChatBot('SMS')

data = pd.read_excel('WHO_FAQ.xlsx')
question = data.iloc[:, 0]
answer = data.iloc[:, -1]
convo = []
count = 0
for count in range(len(question)):
    convo.append(question[count])
    convo.append(question[count])


trainer = ListTrainer(bot)

trainer.train(convo)

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you:  "+query)
    msgs.insert(END, "SMS:  "+str(answer_from_bot))
    textF.delete(0, END)
    speak(answer_from_bot)
    msgs.yview(END)

main = Tk()
main.geometry('500x700')
main.title("Chat Bot-SMS")
img = PhotoImage(file = "logo.png")
photoL = Label(main, image = img)
photoL.pack(pady = 5)
frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width = 80, height = 20, yscrollcommand = sc.set)
sc.pack(side = RIGHT, fill = Y)
msgs.pack(side = LEFT, fill = BOTH, pady = 10)
frame.pack()


# Creating the text input field
textF = Entry(main, font = ("Verdana", 15))
textF.pack(fill = X, pady  = 10)

btn = Button(main, text = "Ask SMS", font = ("Verdana", 20), command = ask_from_bot)
btn.pack()


# Creating a function
def enter_function(event):
    btn.invoke()


# Going to bind main window with enter key
main.bind('<Return>', enter_function)

main.mainloop()