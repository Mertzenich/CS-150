import tkinter as tk
from functools import partial

prompt = ''


def promptAppend(letter):
    global prompt
    prompt += str(letter)
    print(prompt)


def promptRemove(num):
    global prompt
    prompt = prompt[:-num]
    print(prompt)


def promptSolve():
    global prompt
    answer = eval(prompt)
    print(answer)
    return answer


#print(promptSolve())


app = tk.Tk()


buttonAnswer = tk.Button(app, text="Answer", width=30,
                          command=partial(promptSolve))


buttonBackspace = tk.Button(app, text="Backspace", width=30,
                          command=partial(promptRemove, 1))


buttonZero = tk.Button(app, text="0", width=30,
                          command=partial(promptAppend, '0'))


buttonOne = tk.Button(app, text="1", width=30,
                          command=partial(promptAppend, '1'))


buttonTwo = tk.Button(app, text="2", width=30,
                          command=partial(promptAppend, '2'))


buttonThree = tk.Button(app, text="3", width=30,
                          command=partial(promptAppend, '3'))


buttonFour = tk.Button(app, text="4", width=30,
                          command=partial(promptAppend, '4'))


buttonFive = tk.Button(app, text="5", width=30,
                          command=partial(promptAppend, '5'))


buttonSix = tk.Button(app, text="6", width=30,
                          command=partial(promptAppend, '6'))


buttonSeven = tk.Button(app, text="7", width=30,
                          command=partial(promptAppend, '7'))


buttonEight = tk.Button(app, text="8", width=30,
                          command=partial(promptAppend, '8'))


buttonNine = tk.Button(app, text="9", width=30,
                          command=partial(promptAppend, '9'))


buttonPlus = tk.Button(app, text="+", width=30,
                          command=partial(promptAppend, '+'))


buttonMin = tk.Button(app, text="-", width=30,
                          command=partial(promptAppend, '-'))


buttonMul = tk.Button(app, text="*", width=30,
                          command=partial(promptAppend, '*'))


buttonDiv = tk.Button(app, text="/", width=30,
                          command=partial(promptAppend, '/'))

buttonAnswer.pack()
buttonBackspace.pack()
buttonPlus.pack()
buttonMin.pack()
buttonMul.pack()
buttonDiv.pack()
buttonZero.pack()
buttonOne.pack()
buttonTwo.pack()
buttonThree.pack()
buttonFour.pack()
buttonFive.pack()
buttonSix.pack()
buttonSeven.pack()
buttonEight.pack()
buttonNine.pack()
app.mainloop()
