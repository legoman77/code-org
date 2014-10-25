'''for (var count = 0; count < 8; count++) {
  penColour(colour_random());
  moveForward(100);
  moveBackward(100);
  turnRight(45);
}
'''

import turtle
import mymod

bob = turtle.Turtle()
bob.pensize(7)

for count in range(8):
    bob.pencolor(mymod.random_color())
    bob.forward(100)
    bob.backward(100)
    bob.right(45)
