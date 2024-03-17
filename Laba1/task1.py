

from graphics import *
import time
import numpy as np
import math as mt

#----------------   І. Масштабування    ------------------------

def scale(x,y,sx,sy):
    a = np.array([[x, y, 1]])
    f = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])  # матриця квадрата по строках
    ft = f.T  # транспонована матриця
    total = a.dot(ft)  # множення для перетворень 1 точки квадрата
    x11 = total[0, 0];
    y11 = total[0, 1]
    return x11, y11

xw=600; yw=400; st=50
# розміри графічного вікна та параметри перетворень
win = GraphWin("2-D масштабування", xw, yw)
win.setBackground('white')

width = 3; height = 3;
# розміри квадрата
x1=width; y1=height; x2=2*width; y2=2*height
obj = Rectangle(Point(x1, y1), Point(x2, y2))
obj.draw(win)


for i in range(3):
    time.sleep(0.2)
    x11, y11 = x2, y1
    x22, y22 = scale(x2, y2, 2, 2)
    obj = Rectangle(Point(x11, y11), Point(x22, y22))
    obj.draw(win)

    x1, y1 = x22, y11
    x2, y2 = scale(x22, y22, 2, 2)
    obj = Rectangle(Point(x1, y1), Point(x2, y2))
    obj.draw(win)

win.getMouse()
win.close()

#----------------    І. ПЕРЕНОС + обертання   --_--------------


win = GraphWin("2-D проекція ПЕРЕНОС + ОБЕРТАННЯ", xw, yw)
win.setBackground('white')
width = 100; height = 50;
dx=10; dy=30;

x11=width; y11=yw-2*height
x22=2*width; y22=yw-2*height
x33=2*width; y33=yw-height
x44=width; y44=yw-height


def perenos(x,y):
    a = np.array([[x, y, 1]])
    f = np.array([[1, 0, dx], [0, 1, -dy], [0, 0, 1]])
    ft = f.T
    total = a.dot(ft)
    x = total[0, 0]
    y = total[0, 1]
    return x,y

def rotate(x,y,TetaR):
    ap = np.array([[x, y, 1]])
    fp = np.array([[mt.cos(TetaR), -mt.sin(TetaR), 0], [mt.sin(TetaR), mt.cos(TetaR), 0], [0, 0, 1]])
    ftp = fp.T
    totalp = ap.dot(ftp)
    x = totalp[0, 0]
    y = totalp[0, 1]
    return x,y


stop=xw/dx*6
stop = float(stop)
ii = int(stop)
TetaG = 45;
TetaR = (3 / 14 * TetaG) / 180

# ----------------------------- Анімація перенос та обертання ------------------------------

for i in range(ii):
    time.sleep(0.2)
    obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))

    x11, y11 = perenos(x11, y11)
    x22, y22 = perenos(x22, y22)
    x33, y33 = perenos(x33, y33)
    x44, y44 = perenos(x44, y44)


    DTetaR = (3 / 14 * ((xw/dx)*0.65)) / 180
    TetaR=TetaR+DTetaR

    x11,y11=rotate(x11,y11,TetaR)
    x22, y22 = rotate(x22, y22, TetaR)
    x33, y33 = rotate(x33, y33, TetaR)
    x44, y44 = rotate(x44, y44, TetaR)

    obj = Polygon(Point(x11, y11), Point(x22, y22), Point(x33, y33), Point(x44, y44))
    obj.draw(win)

    # -----------------------------------------------------------------------------------------------

win.getMouse()
win.close()