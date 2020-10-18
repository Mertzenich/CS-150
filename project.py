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
mainFrame = Frame(app)
mainFrame.pack()

left = Frame(mainFrame)
left.pack(side=LEFT)

right = Frame(mainFrame)
right.pack(side=RIGHT)

numFrame1 = Frame(left)
numFrame1.pack(side=BOTTOM)

numFrame2 = Frame(left)
numFrame2.pack(side=BOTTOM)

numFrame3 = Frame(left)
numFrame3.pack(side=BOTTOM)

commandFrame = Frame(right)
commandFrame.pack()

promptBox = tk.Label(commandFrame, text="")

###
### Command Frame
###

buttonAnswer = tk.Button(commandFrame, text="=", width=1,
                          command=partial(promptSolve))


buttonBackspace = tk.Button(commandFrame, text="X", width=1,
                          command=partial(promptRemove, 1))


buttonZero = tk.Button(mainFrame, text="0",
                          command=partial(promptAppend, '0'))

###
### Number Frame 1
###

buttonOne = tk.Button(numFrame1, text="1",
                          command=partial(promptAppend, '1'))


buttonTwo = tk.Button(numFrame1, text="2",
                          command=partial(promptAppend, '2'))


buttonThree = tk.Button(numFrame1, text="3",
                          command=partial(promptAppend, '3'))

###
### Number Frame 2
###

buttonFour = tk.Button(numFrame2, text="4",
                          command=partial(promptAppend, '4'))


buttonFive = tk.Button(numFrame2, text="5",
                          command=partial(promptAppend, '5'))


buttonSix = tk.Button(numFrame2, text="6",
                          command=partial(promptAppend, '6'))


###
### Number Frame 3
###


buttonSeven = tk.Button(numFrame3, text="7",
                          command=partial(promptAppend, '7'))


buttonEight = tk.Button(numFrame3, text="8",
                          command=partial(promptAppend, '8'))


buttonNine = tk.Button(numFrame3, text="9",
                          command=partial(promptAppend, '9'))

###
### Command Frame
###

buttonPlus = tk.Button(commandFrame, text="+", width=1,
                          command=partial(promptAppend, '+'))


buttonMin = tk.Button(commandFrame, text="-", width=1,
                          command=partial(promptAppend, '-'))


buttonMul = tk.Button(commandFrame, text="*", width=1,
                          command=partial(promptAppend, '*'))


buttonDiv = tk.Button(commandFrame, text="/", width=1,
                          command=partial(promptAppend, '/'))


###
### Packing
###

promptBox.pack()
buttonAnswer.pack()
buttonBackspace.pack()

buttonDiv.pack()
buttonMul.pack()
buttonPlus.pack()
buttonMin.pack()

buttonOne.pack(side=LEFT)
buttonTwo.pack(side=LEFT)
buttonThree.pack(side=LEFT)

buttonFour.pack(side=LEFT)
buttonFive.pack(side=LEFT)
buttonSix.pack(side=LEFT)

buttonSeven.pack(side=LEFT)
buttonEight.pack(side=LEFT)
buttonNine.pack(side=LEFT)

buttonZero.pack(side=BOTTOM)

app.mainloop()
