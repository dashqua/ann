import matplotlib as plt
import numpy as np
from tkinter import *

def sign(n):
    return ((n>=0)-(n<0))

def f(x):
    return np.pi*x +1

class Perceptron:
    def __init__(self,n):
        self.weight = []
        for i in range(0,n):
            self.weight.append( np.random.uniform(low=-1,high=1)  )
            
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
            
    def guessY(self,x):
        w0 = self.weight[0]
        w1 = self.weight[1]
        w2 = self.weight[2]
        return -(w2/w1) - (w0/w1)*x

class Point:
    #Constructor
    def __init__(self, *args):
        global width, height
        if (len(args)!=2):
            self.x = np.random.uniform(low=-1,high=1)
            self.y = np.random.uniform(low=-1,high=1)
        else:
            self.x = args[0]
            self.y = args[1]
        self.bias = 1
        lineY = f(self.y)
        if (self.x > lineY):
            self.label = 1
        else:
            self.label = -1
        self.pixelX = (self.x +1)*width/2      
        self.pixelY = (-self.y+1)*height/2
        
    def show(self):
        px = self.pixelX
        py = self.pixelY
        if (self.label==1):
            canvas.create_oval(px-thick, py+thick, px+thick, py-thick, width=2, fill='black')
        else:
            canvas.create_oval(px-thick, py+thick, px+thick, py-thick, width=2, fill='white')

    
#onMouseClick()
def mousePressed(event):
    global brain, points, trainingID, nbred
    nbred = 0
    trainingID += 1
    print('training ', trainingID)
    for pt in points:
        inputs = [ pt.x , pt.y , pt.bias ]
        target = pt.label
        brain.train(inputs, target)
        guess = brain.guess(inputs)
        if (guess == target):
            canvas.create_oval(pt.pixelX-thick/2, pt.pixelY+thick/2, pt.pixelX+thick/2, pt.pixelY-thick/2, width=2, fill='green')
        else:
            canvas.create_oval(pt.pixelX-thick/2, pt.pixelY+thick/2, pt.pixelX+thick/2, pt.pixelY-thick/2, width=2, fill='red')   
            nbred +=1
    #Legend
    widget = Label(canvas, text='#false '+str(nbred) , fg='white', bg='black', font='Times 24 bold')
    widget.pack()
    canvas.delete("leg")
    canvas.create_window(100, 100, window=widget, tag="leg")
    #Guessed Line 
    p3 = Point( -1, brain.guessY(-1) )
    p4 = Point( 1 , brain.guessY( 1) )
    canvas.delete("templine")
    canvas.create_line(p3.pixelX,p3.pixelY,p4.pixelX,p4.pixelY,width = 3,tag="templine")

    #training = points[trainingIndex]
    #inputs = [training.x , training.y , training.bias ]
    #target = training.label
    #brain.train(inputs, target)
    #trainingIndex += 1
    #if (trainingIndex == len(points)):
    #    trainingIndex == 0    
    
#Background
global width,height, nbred
width = 800
height = 800
nbred = 0
fenetre = Tk()
canvas = Canvas(fenetre, width=width, height=height, background='white')
canvas.pack()

#Line
p1 = Point(f(-1),-1);
p2 = Point( f(1),1 );
canvas.create_line(p1.pixelX,p1.pixelY,p2.pixelX,p2.pixelY,width = 5,fill="red")

#Points
global thick, num, trainingIndex
thick = 8
num = 1000
trainingIndex = 0
points = []
for i in range(num):
    p = Point()
    points.append( Point() )
    points[i].show()

#Perceptron
global lr, trainingID
lr = 100#0.0005
trainingID = 0
brain = Perceptron(3)
canvas.bind_all('<KeyPress>', mousePressed )  

#End
fenetre.mainloop()  