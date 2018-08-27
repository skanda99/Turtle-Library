
''' A design with regular polygons '''
''' Polygons are of random size and are placed at random positions '''

import turtle
import random

class Polygons:
    def __init__(self):
        self.pen=turtle.Pen()
        self.pen.pensize(0)         #pen size will always be 3
        self.pen.color('black')         #pen color will be black    
        self.pen.screen.bgcolor('#E8DAEF')          #back ground color ie. color of the canvas
        self.colors=['#D2B4DE','#A569BD','#BB8FCE','#8E44AD','#7D3C98','#6C3483','#5B2C6F','#4A235A']       # polygons will be filled with these colors
        self.length=[25,45,65,75,100,125,135,160]           # length of polygons will be these
        self.pen._shown=False               # turtle (pen) wont be shown
        
    def set_pos(self,x,y):
        '''' Sets the position of pen '''
        self.pen.up()
        self.pen.goto(x,y)
        self.pen.down()

    def draw(self,num_sides):
        ''' Draws a polygon with num_sides '''
        fill_color=random.choice(self.colors)
        L=random.choice(self.length)
        self.pen.fillcolor(fill_color)
        self.pen.begin_fill()
        for i in range(num_sides):
            self.pen.forward(L)
            self.pen.left(360.0/num_sides)
        self.pen.end_fill()
            


x=Polygons()
n=int(input('Enter number of sides of polygon (preferable 4): '))
print('Please maximize the canvas!')


for i in range(100):
    x.set_pos(random.uniform(-800,800),random.uniform(-400,300))
    x.draw(n)

input('Press any key to exit!')


        
