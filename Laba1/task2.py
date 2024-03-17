
from graphics import *
import numpy as np
import math as mt
import random

#---------------------------------- координати паралелепіпеда ------------------------------------
xw=600; yw=600; st=200
# розташування координат у строках: дальній чотирикутник - A B I M,  ближній чотирикутник D C F E
Prlpd = np.array([ [0, 0, 0, 1],
                  [st, 0, 0, 1],
                  [st, st/2, 0, 1],
                  [0, st/2, 0, 1],
                  [0, 0, st, 1],
                  [st, 0, st, 1],
                  [st, st/2, st, 1],
                  [0, st/2, st, 1]])    # по строках
print('enter matrix')
print(Prlpd)

#------------------функція побудови сітки-------------------------------------
def Grid(spacing = 50, xw=600):
    num_lines = xw // spacing
    color = "#ECECEC"
    # Draw vertical grid lines
    for i in range(num_lines):
        x = (i + 1) * spacing
        line = Line(Point(x, 0), Point(x, yw))
        line.setFill(color)
        line.draw(win)

    # Draw horizontal grid lines
    for i in range(num_lines):
        y = (i + 1) * spacing
        line = Line(Point(0, y), Point(xw, y))
        line.setFill(color)
        line.draw(win)
#--------функція проекції на xy, z=0 -------------------------------------
def ProjectXY (Figure):
   f = np.array([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1] ])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   print('проекция на ху')
   print(Prxy)
   return Prxy

#----------зміщення ----------------------------------------------
def ShiftXYZ (Figure, l, m, n):
   f = np.array([ [1, 0, 0, l], [0, 1, 0, m], [0, 0, 1, n], [1, 0, 0, 1] ])    # по строках
   ft=f.T
   Prxy = Figure.dot(ft)
   print('зміщення')
   print(Prxy)
   return Prxy

#-----обертання коло х----------------------------------------
def insertX (Figure, TetaG):
    TetaR=(3/14*TetaG)/180
    f = np.array([ [1, 0, 0, 0], [0, mt.cos(TetaR), mt.sin(TetaR), 0], [0, -mt.sin(TetaR),  mt.cos(TetaR), 0], [0, 0, 0, 1]])
    ft=f.T
    Prxy = Figure.dot(ft)
    print('обертання коло х')
    print(Prxy)
    return Prxy

#-----обертання коло у----------------------------------------
def insertY (Figure, TetaG):
    TetaR=(3/14*TetaG)/180
    print(TetaR)
    f = np.array([ [mt.cos(TetaR), 0, -mt.sin(TetaR), 0], [0,1,0,0], [mt.sin(TetaR), 0,mt.cos(TetaR) ,0], [0,0,0,1]])
    ft=f.T
    Prxy = Figure.dot(ft)
    print('обертання коло y')
    print(Prxy)
    return Prxy

#--------аксонометрія ----------------------------------------------
def dimetri (Figure, TetaG1, TetaG2):
    TetaR1=(3/14*TetaG1)/180; TetaR2=(3/14*TetaG2)/180
    f1 = np.array([[mt.cos(TetaR1), 0 , -mt.sin(TetaR1), 0], [0, 1, 0, 0],  [mt.sin(TetaR1), 0, mt.cos(TetaR1), 1], [0, 0, 0, 0]])
    ft1 = f1.T
    Prxy1 = Figure.dot(ft1)
    f2 = np.array([ [1, 0, 0, 0], [0, mt.cos(TetaR2), mt.sin(TetaR2), 0], [0, -mt.sin(TetaR2),  mt.cos(TetaR2), 0], [0, 0, 0, 1]])
    ft2=f2.T
    Prxy2 = Prxy1.dot(ft2)
    print('dimetri')
    print(Prxy2)
    return Prxy2

#--------функція побудови паралелепіпеда -----------------------------
def PrlpdWiz(Prxy, color = "black"):
    Ax = Prxy[0, 0];  Ay = Prxy[0, 1]
    Bx = Prxy[1, 0];  By = Prxy[1, 1]
    Ix = Prxy[2, 0];  Iy = Prxy[2, 1]
    Mx = Prxy[3, 0];  My = Prxy[3, 1]

    Dx = Prxy[4, 0];  Dy = Prxy[4, 1]
    Cx = Prxy[5, 0];  Cy = Prxy[5, 1]
    Fx = Prxy[6, 0];  Fy = Prxy[6, 1]
    Ex = Prxy[7, 0];  Ey = Prxy[7, 1]

    # print(Ax, Ay); print(Bx, By); print(Ix, Iy);  print(Mx, My);
    # print(Dx, Dy); print(Cx, Cy); print(Fx, Fy); print(Ex, Ey);

    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Ix, Iy), Point(Mx, My))
    obj.draw(win)
    obj.setOutline(color)

    obj = Polygon(Point(Dx, Dy), Point(Cx, Cy), Point(Fx, Fy), Point(Ex, Ey))
    obj.draw(win)
    obj.setOutline(color)

    obj = Polygon(Point(Ax, Ay), Point(Bx, By), Point(Cx, Cy), Point(Dx, Dy))
    obj.draw(win)
    obj.setOutline(color)

    obj = Polygon(Point(Mx, My), Point(Ix, Iy), Point(Fx, Fy), Point(Ex, Ey))
    obj.draw(win)
    obj.setOutline(color)
    return PrlpdWiz

#-------- повний цикл побудови для подальшої анімації-----------------------------
def build_Prlpd(Prlpd, l, m ,n, color='black'):
    Prlpd1 = ShiftXYZ(Prlpd, l, m, n)
    print("sdgwdgfsdg = ", l, m, n)
    Prlpd2 = dimetri(Prlpd1, TetaG1, TetaG2)
    Prxy3 = ProjectXY(Prlpd2)
    PrlpdWiz(Prxy3, color)

#----------------побудова паралелепіпеда -----------------------------

win = GraphWin("3-D модель паралелепіпеда, ПЕРВИННЕ ПОЛОЖЕННЯ", xw, yw)
win.setBackground('white')
Grid(50, xw)

Prxy3=Prlpd
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

win = GraphWin("3-D модель паралелепіпеда, ЦЕНТР", xw, yw)
win.setBackground('white')
xw=600; yw=600; st=0; TetaG1=0; TetaG2=-90
l=(xw/3)-st; m=(yw/3)-st; n=m
Grid(50, xw)
Prlpd1=ShiftXYZ (Prlpd, l, m, n)

Prxy3=ProjectXY (Prlpd1)
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

win = GraphWin("3-D модель паралелепіпеда, ОБЕРТ У", xw, yw)
win.setBackground('white')
TetaG1=180; TetaG2=-90
xw=600; yw=600; st=-100;
l=(xw/3)-st; m=(yw/3)+50; n=m
Grid(50, xw)
Prlpd1=ShiftXYZ (Prlpd, l, m, n)
Prlpd2=insertY (Prlpd1, TetaG1)
Prxy3=ProjectXY (Prlpd2)
PrlpdWiz(Prxy3)
win.getMouse()
win.close()

win = GraphWin("3-D паралелепіпеда, АКСОНОМЕТРИЧНА ПРОЕКЦІЯ на ХУ", xw, yw)
win.setBackground('white')
TetaG1=180; TetaG2=-90
l=(xw/2); m=(yw/2); n=m
Grid(50, xw)
build_Prlpd(Prlpd, l , m ,n)
win.getMouse()
win.close()



win = GraphWin("3-D паралелепіпеда АНІМАЦІЯ", xw, yw)
win.setBackground('white')
xw=600; yw=600; st=50; TetaG1=180; TetaG2=-90; length = 100
l=(xw/2); m=(yw/2); n=m
Grid(50, xw)
build_Prlpd(Prlpd, l , m ,n)


for i in range(15):
    time.sleep(1)
    build_Prlpd(Prlpd, l, m, n, "white")
    Grid(50, xw)
    time.sleep(1)
    Grid(50, xw)
    l = random.randint(100, xw-100)
    m = random.randint(100, xw-100)
    n = random.randint(100, xw-100)
    build_Prlpd(Prlpd, l, m, n)
win.getMouse()
win.close()

