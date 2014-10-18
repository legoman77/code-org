'''for (var count = 0; count < 4; count++) {
  moveForward(100);
  turnRight(90);
}
'''

import turtle

bob = turtle.Turtle()
bob.pensize(7)

for count in range(4):
    bob.forward(100)
    bob.right(90)
