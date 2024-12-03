import tkinter as tk
from tkinter import ttk
import os
import json

root = tk.Tk()
root.title('TODO List')

tasks = []
user_name = ''

def addTask():
    task = enter.get()
    if task:
        tasks.append(task)
        enter.delete(0, tk.END)
        update()
        save()


def deleteTask():
    try:
        selected_task_index = listbox.curselection()[0]
        del tasks[selected_task_index]
        update()
        save()
    except IndexError:
        pass


def save():
    data = {'user':user_name,'tasks': tasks}
    with open(f'{user_name}.json','w') as f:
        json.dump(data,f)

        


def load():
    filename = f'{user_name}.json'
    if os.path.exists(filename):
        with open(filename,'r') as f:
            data = json.load(f)
            global tasks
            tasks = data['tasks']
            update()


def update():   
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)


def register():
    global enter, listbox, user_name
    user_name = entry.get()
    if user_name:
        # Удаляем начальные виджеты
        entry.destroy()
        btn_go.destroy()

        # Создаем новые виджеты
        label = ttk.Label(root, text=f'Добро пожаловать, {user_name}!', font=('Arial', 14))
        btn_add = ttk.Button(root, text='Add Task', command=addTask)
        btn_delete = ttk.Button(root, text='Delete Task', command=deleteTask)
        listbox = tk.Listbox(root, width=40)
        enter = ttk.Entry(root)

        # Упаковка новых виджетов
        label.pack()
        btn_add.pack(anchor='w', pady=5)
        btn_delete.pack(anchor='sw', pady=5)
        enter.pack(anchor=tk.N, pady=10)
        listbox.pack(pady=10)
        load()



entry = ttk.Entry(root)
entry.pack()
btn_go = ttk.Button(root, text='Go', command=register)
btn_go.pack()

root.mainloop()
