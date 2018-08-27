
''' A design program '''

import turtle

class Design:      
    def __init__(self):
        self.pen=turtle.Pen()
        self.pen.screen.bgcolor('black')      # back ground color = Black
        self.pen._shown=False     # pen wont be shown
        self.pen.speed(0)
        self.colors=['#FF1A03','#FF6A03','#FBFF03','#48FF03','#03FFCD','#0303FF','#8903FF','#FF03FF']    # colors

    def draw(self):
        ''' Draws design '''
        for i in range(300):
            self.pen.color(self.colors[i%8])        # regularly sets pen color to one in self.colors list
            self.pen.forward(i)
            self.pen.left(59)       # angle is important for design



d=Design()   # object of class Design
d.draw()   # call for draw method

input('Press any key to exit!')
