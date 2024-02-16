
from tkinter import *
import tkinter as tk

from PIL import Image, ImageTk

import random
import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms

import time
import numpy as np
#from mcq import startquiz as s
import cv2

import os
from PIL import Image, ImageTk
from PIL import Image  # For face recognition we will the the LBPH Face Recognizer
from tkinter import messagebox as mb

questions = ["1.How many Keywords are there in C Programming language ?",
             "2.Which of the following functions takes A console Input in Python ?",
             "3.Which of the following is the capital of India ?",
             "4.Which of The Following is must to Execute a Python Code ?",
             "5.The Taj Mahal is located in  ?",
             "6.The append Method adds value to the list at the  ?",
             "7.Which of the following is not a costal city of india ?",
             "8.Which of The following is executed in browser(client side) ?",
             "9.Which of the following keyword is used to create a function in Python ?",
             "10.To Declare a Global variable in python we use the keyword ?",
             ]

answers_choice = [
    ["23", "32", "33", "43", ],
    ["get()", "input()", "gets()", "scan()", ],
    ["Mumbai", "Delhi", "Chennai", "Lucknow", ],
    ["TURBO C", "Py Interpreter", "Notepad", "IDE", ],
    ["Patna", "Delhi", "Benaras", "Agra", ],
    ["custom location", "end", "center", "beginning", ],
    ["Bengluru", "Kochin", "Mumbai", "vishakhapatnam", ],
    ["perl", "css", "python", "java", ],
    ["function", "void", "fun", "def", ],
    ["all", "var", "let", "global", ],
]

answers = [1, 1, 1, 1, 3, 1, 0, 1, 3, 3]

user_answer = []

indexes = []


def gen():
    global indexes
    while len(indexes) < 5:
        x = random.randint(0, 9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

    # print(indexes)


def showresult(score):
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        window,

    )
    labelimage.pack(),
    labelresulttext = Label(
        window,
        font=("Consolas", 20)
    )
    labelresulttext.pack()
    if score >= 20:
        # im = Image.open('great.jpg')
        # imgtk = ImageTk.PhotoImage(image=im)
        img = Label(window, text='Greate Exam Done',
                    image=imgtk, font=('times', 15, ' bold '))
        # img.image = imgtk
        img.place(x=50, y=2)
    #    labelimage.configure(image=img)
     #   labelimage.image=img
      #  labelresulttext.configure(text="You are excelent")
    elif 10 <= score < 20:
        # im = Image.open('ok.jpg')
        # imgtk = ImageTk.PhotoImage(image=im)
        img = Label(window, text='Ok Exam Done', font=('times', 15, ' bold '))
        # img.image = imgtk
        img.place(x=50, y=2)
       # labelimage.configure(image=img)
        # labelimage.image=img
        #labelresulttext.configure(text="You can be better")
    else:
        # im = Image.open('bad.jpg')
        # imgtk = ImageTk.PhotoImage(image=im)
        img = Label(window, text='Bad Exam Done', font=('times', 15, ' bold '))
        # img.image = imgtk
        img.place(x=50, y=2)
        # labelimage.configure(image=img)
        #labelimage.image = img
        #labelresulttext.configure(text="You can be better")


def calc():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    print(score)
    showresult(score)


ques = 1


def camera():
    flag = 0
    recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 100)
#    recognizer = cv2.face.FisherFaceRecognizer(0, 3000);

    recognizer.read('trainingdata.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # iniciate id counter
    id = 0
    # names related to ids: example ==> Marcelo: id=1,  etc
    #names = ['None', 'Criminal person identified', 'Missing person', 'Criminal person identified', 'Criminal person identified', 'Missing person','Missing person']
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video widht
    cam.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:

        ret, img = cam.read()
#        img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray, 1.3, 8, minSize=(int(minW), int(minH)))
#        faces = faceCascade.detectMultiScale(
#            gray,
#            scaleFactor = 1.2,
#            minNeighbors = 5,
#            minSize = (int(minW), int(minH)),
#           )
        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

            # If confidence is less them 100 ==> "0" : perfect match

            if (confidence < 50):
                # print(id)
                #name = names[id]
                id = id

                print(type(id))

                #
                #id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))

                cv2.putText(img, str(id), (x+5, y-5),
                            font, 1, (255, 255, 255), 2)
                cv2.putText(img, str(confidence), (x+5, y+h-5),
                            font, 1, (255, 255, 0), 1)
                cv2.imshow('camera', img)


def close():
    window.destroy()


def selected():
    global radiovar, user_answer
    global lblquestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    # print(x)
    if ques < 5:
        lblquestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        flag = 0
        recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 100)
    #    recognizer = cv2.face.FisherFaceRecognizer(0, 3000);

        recognizer.read('trainingdata.yml')
        cascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascadePath)
        font = cv2.FONT_HERSHEY_SIMPLEX
        # iniciate id counter
        id = 0
        # names related to ids: example ==> Marcelo: id=1,  etc
        #names = ['None', 'Criminal person identified', 'Missing person', 'Criminal person identified', 'Criminal person identified', 'Missing person','Missing person']
        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640)  # set video widht
        cam.set(4, 480)  # set video height
        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        while True:

            ret, img = cam.read()
    #        img = cv2.flip(img, -1) # Flip vertically
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(
                gray, 1.3, 8, minSize=(int(minW), int(minH)))
    #        faces = faceCascade.detectMultiScale(
    #            gray,
    #            scaleFactor = 1.2,
    #            minNeighbors = 5,
    #            minSize = (int(minW), int(minH)),
    #           )
            for(x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

                # If confidence is less them 100 ==> "0" : perfect match

                if (confidence < 50):
                    # print(id)
                    #name = names[id]
                    id = id

                    print(type(id))

                    #
                    #id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))

                    cv2.putText(img, str(id), (x+5, y-5),
                                font, 1, (255, 255, 255), 2)
                    cv2.putText(img, str(confidence), (x+5, y+h-5),
                                font, 1, (255, 255, 0), 1)
                    cv2.imshow('camera', img)
                    ques += 1
                    cam.release()
                else:
                    cv2.imshow('camera', img)
                    id = "unknown Student Identified"
                    cv2.putText(img, str(id), (x+5, y-5),
                                font, 1, (255, 255, 255), 2)
                    mb.showwarning(
                        "Exam Portal", "Exam Will closed  \nbecouse of Froud face detected!!")
                    close()
                    cam.release()
                    print("Fraud Exam Detected")

    else:
       # print(indexes)
        # print(user_answer)
        calc()


def startquiz():

    global lblquestion, r1, r2, r3, r4

    lblquestion = Label(
        window,
        text=questions[indexes[0]],
        font=("Consolas", 14),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff"

    )
    lblquestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        window,
        text=answers_choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        window,
        text=answers_choice[indexes[0]][1],
        font=('Times', 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff"

    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        window,
        text=answers_choice[indexes[0]][2],
        font=('Times', 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff"

    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        window,
        text=answers_choice[indexes[0]][3],
        font=('Times', 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff"

    )
    r4.pack(pady=5)


def startIsPressed():
    labetext.destroy()
    lblrules.destroy()
    labelinstruction.destroy()
    btnstrt.destroy()
    gen()
    startquiz()


window = Tk()
window.title("GUI")
window.geometry('450x450')
window.config(background="#ffffff")
window.resizable(0, 0)

'''
image = Image.open("pani.jpg")
newsize = (100,100)
image = image.resize((newsize),Image.ANTIALIAS)
image.save("pani.ppm", "ppm")
img1 = ImageTk.PhotoImage(file="pani.ppm")

labelImage= Label( 
    window,
    image = img1
)

labelImage.pack()
'''

labetext = Label(
    window,
    text="Quizstar",
    font=("Comic sans MS", 24, "bold"),
    bg='green'
)
labetext.pack(pady=(40, 0))

# image2 = Image.open("startbutton.png")
# newsize = (100, 100)
# image2 = image2.resize((newsize), Image.ANTIALIAS)
# image2.save("sbutton.ppm", "ppm")
# img2 = PhotoImage(file="sbutton.ppm")
# button3 = tk.Button(window, text="Start Exam", command=startIsPressed, width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
# button3.place(x=10, y=340)

labelinstruction = Label(
    window,
    text="Read the Rules And\n Click Start once you are ready",
    background="#ffffff",
    font=("Consolas", 14),
    justify='center'
)
labelinstruction.pack(pady=(10, 90))

lblrules = Label(
    window,
    text="This quiz contains 10 questions\n You will get 20 seconds to solve a question \n once you select a radio button that will be final choice \n hence think before you select ",
    width=100,
    font=("Times", 14),
    background="#000000",
    foreground="#ffffff"
)

lblrules.pack()

btnstrt = Button(
    window,
    text="Start Exam",
    border=5,
    command=startIsPressed,
)
btnstrt.place(x=200, y=350)
# Create an Exit  Button


# image3 = Image.open("exit.jpg")
# newsize1 = (100, 50)
# image3 = image3.resize((newsize1), Image.ANTIALIAS)
# image3.save("ebutton.ppm", "ppm")
# img3 = PhotoImage(file="ebutton.ppm")
# Create an Exit  Button

Exitbtn = Button(
    window,
    text="Exit Exam",
    border=5,
    command=window.destroy,
)
Exitbtn.place(x=200, y=400)

window.mainloop()
