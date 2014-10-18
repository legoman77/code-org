'''for (var count = 0; count < 3; count++) {
  penColour(colour_random());
  moveForward(100);
  turnRight(120);
}
'''

import turtle
import mymod


bob = turtle.Turtle()
bob.pensize(7)

for count in range (3):
    bob.color(mymod.random_color())
    bob.forward(100)
    bob.right(120)
