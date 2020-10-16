import tkinter as tk




prompt = ''

def promptAppend(letter):
    global prompt
    prompt += str(letter)

def promptRemove(num):
    global prompt
    prompt = prompt[:-num]

def promptSolve():
    global prompt
    return eval(prompt)

promptAppend('5')
promptAppend('+')
promptAppend('6')
promptRemove(2)
promptAppend('*')
promptAppend('7')

print(promptSolve())

app = tk.Tk()
labelExample = tk.Button(app, text="0")
    
buttonExample = tk.Button(app, text="Increase", width=30,
                          command=promptAppend(5))

buttonExample.pack()
labelExample.pack()
app.mainloop()