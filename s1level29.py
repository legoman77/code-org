'''for (var count = 0; count < 3; count++) {
  moveForward(100);
  turnRight(120);
}
turnLeft(180);
for (var count2 = 0; count2 < 4; count2++) {
  moveForward(100);
  turnRight(90);
}
'''

import turtle

bob = turtle.Turtle()
bob.pensize(7)
bob.pencolor('red')

for count in range(3):
    bob.forward(100)
    bob.right(120)

bob.left(180)
for count in range(4):
    bob.forward(100)
    bob.right(90)
