'''penColour('#228b22');
turnRight(90);
for (var count = 0; count < 4; count++) {
  moveForward(100);
  turnRight(90);
}
turnLeft(180);
moveForward(50);
for (var count2 = 0; count2 < 4; count2++) {
  moveForward(100);
  turnLeft(90);
}
'''

import turtle

bob = turtle.Turtle()
bob.pensize(7)
bob.pencolor('green')

for count in range(4):
    bob.forward(100)
    bob.right(90)

bob.left(180)
bob.forward(50)
for count in range(4):
    bob.forward(100)
    bob.left(90)
