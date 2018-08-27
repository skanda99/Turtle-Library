'''The Android logo'''

''' No much OOP involved '''

import turtle as t

pen1=t.Pen()
pen1.speed(0)
pen1._shown=False

pen1.color('#51F70E')
pen1.fillcolor('#51F70E')

# Main Body

pen1.up()
pen1.goto(-75,90)
pen1.down()

pen1.begin_fill()

for i in range(2):
    pen1.forward(150)
    pen1.right(90)
    pen1.forward(180)
    pen1.right(90)

pen1.end_fill()

# leg1
pen1.up()
pen1.goto(-50,-90)
pen1.down()

pen1.begin_fill()
pen1.right(90)
pen1.forward(60)
pen1.circle(25/2,180)
pen1.forward(60)
pen1.right(90)
pen1.end_fill()

# leg 2
pen1.up()
pen1.goto(25,-90)
pen1.down()

pen1.begin_fill()
pen1.right(90)
pen1.forward(60)
pen1.circle(25/2,180)
pen1.forward(60)
pen1.right(90)
pen1.end_fill()

# head

pen1.up()
pen1.goto(75,100)
pen1.down()

pen1.begin_fill()
pen1.left(90)
pen1.circle(75,180)
pen1.end_fill()

# eye1
pen1.up()
pen1.goto(-30,137.5)
pen1.down()
pen1.fillcolor('white')

pen1.begin_fill()
pen1.circle(5)
pen1.end_fill()

# eye2
pen1.up()
pen1.goto(21,137.5)
pen1.down()
pen1.fillcolor('white')

pen1.begin_fill()
pen1.circle(5,-360)
pen1.end_fill()


# ear1

pen1.up()
pen1.goto(75,100)
pen1.left(180)
pen1.circle(75,60)
pen1.right(90)
pen1.pensize(10)
pen1.down()

pen1.forward(35)

# ear2

pen1.up()
pen1.goto(75,100)
pen1.left(30)
pen1.circle(75,120)
pen1.right(90)
pen1.pensize(10)
pen1.down()

pen1.forward(35)

# hand 1

pen1.up()
pen1.goto(85,90-(25/2))
pen1.down()
pen1.pensize(1)
pen1.fillcolor('#51F70E')

pen1.begin_fill()
pen1.left(150)
pen1.forward(100)
pen1.circle(25/2,180)
pen1.forward(100)
pen1.circle(25/2,180)
pen1.end_fill()


# hand 2

pen1.up()
pen1.goto(-85-25,90-(25/2))
pen1.down()
pen1.pensize(1)
pen1.fillcolor('#51F70E')

pen1.begin_fill()
pen1.forward(100)
pen1.circle(25/2,180)
pen1.forward(100)
pen1.circle(25/2,180)
pen1.end_fill()

# text

pen1.up()
pen1.goto(0,-300)
pen1.down()


input('Press any key to exit!')

