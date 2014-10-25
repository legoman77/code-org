'''for (var count = 0; count < 360; count++) {
  moveForward(1);
  turnRight(1);
}
'''

import turtle

bob = turtle.Turtle()
bob.pensize(7)
bob.pencolor('red')

for count in range(360):
    bob.forward(1)
    bob.right(1)
