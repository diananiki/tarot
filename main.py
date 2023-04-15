import pandas as pd
from tkinter import *
import random
import playsound


def func():
    playsound.playsound('magic.mp3')
    var_lb.destroy()
    btn.destroy()
    icon.destroy()
    P = []
    M = [i for i in range(0, 22)]
    random.shuffle(M)
    ind = 0
    text = Text(font=("Arial", 16), wrap=WORD, bd=5, bg='#ffdfab', padx=10, pady=10)
    for i in data.keys()[::-1]:
        if i == 'Аркан' or i == 'picture':
            continue
        arkan = M[ind]
        ind += 1
        P += [data['picture'][arkan]]
        s = '\t' + i + ' : ' + data['Аркан'][arkan] + '\n' + data[i][arkan] + '\n' + '\n'
        text.insert(0.0, s)
        text.pack()
    window.image0 = PhotoImage(file=P[0])
    card = Label(frame, image=window.image0, bg='#edc482', relief=RAISED, bd=3)
    card.grid(row=2, column=3)
    window.image1 = PhotoImage(file=P[1])
    card = Label(frame, image=window.image1, bg='#edc482', relief=RAISED, bd=3)
    card.grid(row=2, column=2)
    window.image2 = PhotoImage(file=P[2])
    card = Label(frame, image=window.image2, bg='#edc482', relief=RAISED, bd=3)
    card.grid(row=2, column=1)
    window.image3 = PhotoImage(file=P[3])
    card = Label(frame, image=window.image3, bg='#edc482', relief=RAISED, bd=3)
    card.grid(row=2, column=0)


excel_data = pd.read_excel('data.xlsx')
data = pd.DataFrame(excel_data, columns=['Аркан', 'Персональные качества', 'Отношения', 'Здоровье', 'Работа', 'picture'])

window = Tk()
window.title("Гадание Таро")
window.geometry('600x400')
window.configure(bg='#edc482')
frame = Frame(window, padx=10, pady=10, bg='#edc482')
frame.pack(expand=True)
window.image = PhotoImage(file="tarot.png")
icon = Label(frame, image=window.image, bg='#edc482')
icon.grid(row=1, column=1)
var_lb = Label(frame, text="Погадаем?)\n", font=("Comic Sans MS", 20), bg='#edc482')
var_lb.grid(row=2, column=1)
btn = Button(frame, text="Разложить", font=("Arial", 18), command=func, bg='#e8ac4a')
btn.grid(row=3, column=1)
window.mainloop()