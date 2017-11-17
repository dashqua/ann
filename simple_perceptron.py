import matplotlib as plt
import numpy as np
from tkinter import *
import os


def sign(n):
    return ((n>=0)-(n<0))



class Perceptron:
    #Constructor   
    def __init__(self):
        self.weight = [0.0,0.0]
        n = len(self.weight)
        for i in range(0,n):
            self.weight[i] =  np.random.uniform(low=-1,high=1)
            
    def guess(self,inputs):
        sum = 0
        n = len(self.weight)
        for i in range(0,n):
            sum += inputs[i]*self.weight[i]
        return sign(sum)
        
    def train(self,inputs, target):
        guess = self.guess(inputs)
        error =  target-guess
        n=len(self.weight)
        for i in range(0,n):
            self.weight[i] += error*inputs[i]*lr


class Point:
    #Constructor
    def __init__(self):
        self.x = np.random.uniform(low=0,high=width)
        self.y = np.random.uniform(low=0,high=height)
        if (self.x > self.y):
            self.label = 1
        else:
            self.label = -1
    def show(self):
        if (self.label==1):
            canvas.create_oval(self.x-thick, self.y+thick, self.x+thick, self.y-thick, width=2, fill='black')
        else:
            canvas.create_oval(self.x-thick, self.y+thick, self.x+thick, self.y-thick, width=2, fill='white')


def main():
    p = Perceptron()
    inputs = [-1,0.5]
    guess = p.guess(inputs)
    print(guess)
    return
    
    
    
    
#onMouseClick()
def mousePressed(event):
    global brain, points, training, nbred
    nbred = 0
    training += 1
    print('training ', training)
    for pt in points:
        inputs = [ pt.x , pt.y ]
        target = pt.label
        brain.train(inputs, target)
        guess = brain.guess(inputs)
        if (guess == target):
            canvas.create_oval(pt.x-thick/2, pt.y+thick/2, pt.x+thick/2, pt.y-thick/2, width=2, fill='green')
        else:
            canvas.create_oval(pt.x-thick/2, pt.y+thick/2, pt.x+thick/2, pt.y-thick/2, width=2, fill='red')   
            nbred +=1

    #Legend
    widget = Label(canvas, text='#false '+str(nbred) , fg='white', bg='black', font='Times 24 bold')
    widget.pack()
    canvas.create_window(100, 100, window=widget)
        
    
    
#Background
global width,height, nbred
width = 800
height = 800
nbred = 0
fenetre = Tk()
canvas = Canvas(fenetre, width=width, height=height, background='white')
canvas.pack()

#Line
canvas.create_line(0,0,width,height, width = 3)

#Points
global thick, num
thick = 10
num = 500
points = []
for i in range(num):
    p = Point()
    points.append( Point() )
    points[i].show()

#Perceptron
global lr, training
lr = 0.0005
training = 0
brain = Perceptron()
canvas.bind_all('<KeyPress>', mousePressed )    
for pt in points:
    inputs = [ pt.x , pt.y ]
    target = pt.label
        
#End
fenetre.mainloop()  
