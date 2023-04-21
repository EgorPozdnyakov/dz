from tkinter import *
from random import randint, uniform
from time import sleep

def new_color(*vidgets):

    a = str(hex(randint(0, 15))[2:])
    b = str(hex(randint(0, 15))[2:])
    c = str(hex(randint(0, 15))[2:])
    d = str(hex(randint(0, 15))[2:])
    e = str(hex(randint(0, 15))[2:])
    f = str(hex(randint(0, 15))[2:])
    color = '#' + c + f + a + b + d + e

    for vidget in vidgets:
        vidget.config(background= color)

    return color

def create_objects(N):
    list_of_obj = []

    for obj in range(0, N):
        side = randint(10, 70) # сторона квадрата
        x, y = randint(0, 430), randint(0, 430) # начальные координаты
        vx, vy = randint(0, 5), randint(0, 5) # скорости
        obj = canva.create_oval(x, y, x + side, y + side, fill= new_color(), # создание объекта на канве
                         outline= new_color(), width= randint(1, 5))
        obj_id = {'obj':obj, 'vx':vx, 'vy':vy} # создание словаря из параметров объекта: id + скорости
        list_of_obj.append(obj_id) # добавляем словарь объекта в список
    return list_of_obj # возвращаем список в основную программу

root = Tk()
root.geometry('500x500')
root.resizable(False, False)
new_color(root)

canva = Canvas(width= 500, height= 500)
canva.pack()
new_color(canva)

objects = create_objects(5) # objects = список из словарей объектов

indicate = True
while indicate:
    for obj in objects: # для одного словаря объекта в списке
        canva.move(obj['obj'], obj['vx'], obj['vy']) # указываем id объекта и его скорости из словаря
        if canva.coords(obj['obj'])[0] > 460 or canva.coords(obj['obj'])[0] < 0:
            obj['vx'] = -obj['vx'] 
        if canva.coords(obj['obj'])[1] > 460 or canva.coords(obj['obj'])[1] < 0:
            obj['vy'] = -obj['vy'] 
    root.update()
    sleep(0.01)

root.mainloop()