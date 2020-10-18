import tkinter as tk
from tkinter import *
from functools import partial

prompt = ''

def promptAppend(letter):
    global prompt
    prompt += str(letter)
    promptBox.config(text=str(prompt))
    print(prompt)


def promptRemove(num):
    global prompt
    prompt = prompt[:-num]
    promptBox.config(text=str(prompt))
    print(prompt)


def promptSolve():
    global prompt
    answer = eval(prompt)
    buttonAnswer.config(text=str(answer))
    print(answer)


app = tk.Tk()
numFrame = Frame(app)
numFrame.pack(side=LEFT)

numFrame1 = Frame(numFrame)
numFrame1.pack(side=BOTTOM)

numFrame2 = Frame(numFrame)
numFrame2.pack(side=BOTTOM)

numFrame3 = Frame(numFrame)
numFrame3.pack(side=BOTTOM)

commandFrame = Frame(app)
commandFrame.pack(side=RIGHT)

promptBox = tk.Label(commandFrame, text="")


buttonAnswer = tk.Button(commandFrame, text="Answer", width=30,
                          command=partial(promptSolve))


buttonBackspace = tk.Button(commandFrame, text="Backspace", width=30,
                          command=partial(promptRemove, 1))


buttonZero = tk.Button(numFrame, text="0", width=30,
                          command=partial(promptAppend, '0'))


buttonOne = tk.Button(numFrame1, text="1", width=30,
                          command=partial(promptAppend, '1'))


buttonTwo = tk.Button(numFrame1, text="2", width=30,
                          command=partial(promptAppend, '2'))


buttonThree = tk.Button(numFrame1, text="3", width=30,
                          command=partial(promptAppend, '3'))


buttonFour = tk.Button(numFrame2, text="4", width=30,
                          command=partial(promptAppend, '4'))


buttonFive = tk.Button(numFrame2, text="5", width=30,
                          command=partial(promptAppend, '5'))


buttonSix = tk.Button(numFrame2, text="6", width=30,
                          command=partial(promptAppend, '6'))


buttonSeven = tk.Button(numFrame3, text="7", width=30,
                          command=partial(promptAppend, '7'))


buttonEight = tk.Button(numFrame3, text="8", width=30,
                          command=partial(promptAppend, '8'))


buttonNine = tk.Button(numFrame3, text="9", width=30,
                          command=partial(promptAppend, '9'))


buttonPlus = tk.Button(commandFrame, text="+", width=30,
                          command=partial(promptAppend, '+'))


buttonMin = tk.Button(commandFrame, text="-", width=30,
                          command=partial(promptAppend, '-'))


buttonMul = tk.Button(commandFrame, text="*", width=30,
                          command=partial(promptAppend, '*'))


buttonDiv = tk.Button(commandFrame, text="/", width=30,
                          command=partial(promptAppend, '/'))

promptBox.pack()
buttonAnswer.pack()
buttonBackspace.pack()

buttonPlus.pack()
buttonMin.pack()
buttonMul.pack()
buttonDiv.pack()

buttonOne.pack(side=LEFT)
buttonTwo.pack(side=LEFT)
buttonThree.pack(side=LEFT)

buttonFour.pack(side=LEFT)
buttonFive.pack(side=LEFT)
buttonSix.pack(side=LEFT)

buttonSeven.pack(side=LEFT)
buttonEight.pack(side=LEFT)
buttonNine.pack(side=LEFT)

buttonZero.pack()

app.mainloop()
