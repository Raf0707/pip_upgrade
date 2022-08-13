import os
import tkinter as tk
 
root= tk.Tk()
 
canvas1 = tk.Canvas(root, width = 300, height = 350, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()
 
label1 = tk.Label(root, text='Upgrade PIP', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 80, window=label1)
 
def upgradePIP():

    '''
    Выберите вашу среду разработки - PyCharm или IDLE Python
    P. S. Анаконду не ставил, но попробуйте вариант для PyCharm в анаконде
    Так как терминалы PyCharm и Anaconda идентичны

    Выберите подходящий вам вариант и оставьте его
    неподходящий вариант удалите или закомментируйте
    для однострочного комментария используйте знак # перед началом строки
    '''

    # for PyCharm
    os.system('pip install --upgrade pip')

    # for IDLE Python
    os.system('start cmd /k python.exe -m pip install --upgrade pip')
    
button1 = tk.Button(text='      Upgrade PIP     ', command=upgradePIP, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=button1)
 
root.mainloop()
