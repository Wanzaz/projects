from turtle import *
from random import randint

rang = int(input("Write range"))
count = int(input("Write how meny turtles u want race(max 10)"))

if rang == 0:
  rang = -1

speed(0)
penup()
goto(-200, 190)
f = 375/rang
a = 30

t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0
t8 = 0
t9 = 0
t10 = 0

for step in range(rang):
  forward(f)
  write(step+1)
  right(90)
  #forward(380)
  for number in range(a):
    pendown()
    forward(380/(a*2))
    penup()
    forward(380/(a*2))
  backward(380)
  left(90)

if count>10:
  count = 10

if count == 1:
  turtle1 = Turtle()
  turtle1.color('green')
  turtle1.shape('turtle')
  turtle1.penup()
  turtle1.goto(-200, 0)
  turtle1.pendown()
  turtle1.right(360)

if count > 1:
  turtle1 = Turtle()
  turtle1.color('blue')
  turtle1.shape('turtle')
  turtle1.penup()
  turtle1.goto(-200, 160 - (320/(count-1)) * (1-1))
  turtle1.pendown()
  turtle1.right(360)

if count >= 2:
  turtle2 = Turtle()
  turtle2.color('black')
  turtle2.shape('turtle')
  turtle2.penup()
  turtle2.goto(-200, 160 - (320/(count-1)) * (2-1))
  turtle2.pendown()
  turtle2.right(360)

if count >= 3:
  turtle3 = Turtle()
  turtle3.color('yellow')
  turtle3.shape('turtle')
  turtle3.penup()
  turtle3.goto(-200, 160 - (320/(count-1)) * (3-1))
  turtle3.pendown()
  turtle3.right(360)

if count >= 4:
  turtle4 = Turtle()
  turtle4.color('grey')
  turtle4.shape('turtle')
  turtle4.penup()
  turtle4.goto(-200, 160 - (320/(count-1)) * (4-1))
  turtle4.pendown()
  turtle4.right(360)

if count >= 5:
  turtle5 = Turtle()
  turtle5.color('orange')
  turtle5.shape('turtle')
  turtle5.penup()
  turtle5.goto(-200, 160 - (320/(count-1)) * (5-1))
  turtle5.pendown()
  turtle5.right(360)

if count >= 6:
  turtle6 = Turtle()
  turtle6.color('purple')
  turtle6.shape('turtle')
  turtle6.penup()
  turtle6.goto(-200, 160 - (320/(count-1)) * (6-1))
  turtle6.pendown()
  turtle6.right(360)

if count >= 7:
  turtle7 = Turtle()
  turtle7.color('violet')
  turtle7.shape('turtle')
  turtle7.penup()
  turtle7.goto(-200, 160 - (320/(count-1)) * (7-1))
  turtle7.pendown()
  turtle7.right(360)
  
if count >= 8:
  turtle8 = Turtle()
  turtle8.color('red')
  turtle8.shape('turtle')
  turtle8.penup()
  turtle8.goto(-200, 160 - (320/(count-1)) * (8-1))
  turtle8.pendown()
  turtle8.right(360)

if count >= 9:
  turtle9 = Turtle()
  turtle9.color('lime')
  turtle9.shape('turtle')
  turtle9.penup()
  turtle9.goto(-200, 160 - (320/(count-1)) * (9-1))
  turtle9.pendown()
  turtle9.right(360)

if count >= 10:
  turtle10 = Turtle()
  turtle10.color('cyan')
  turtle10.shape('turtle')
  turtle10.penup()
  turtle10.goto(-200, 160 - (320/(count-1)) * (10-1))
  turtle10.pendown()
  turtle10.right(360)


while t1 <= 361 and t2 <= 361 and t3 <= 361 and t4 <= 361 and t5 <= 361 and t6 <= 361 and t7 <= 361 and t8 <= 361 and t9 <= 361 and t10 <= 361:
  if count >= 1:
    speed = randint(1, 4)
    turtle1.forward(speed)
    t1 = t1 + speed
  if count >= 2:
    speed = randint(1, 4)
    turtle2.forward(speed)
    t2 = t2 + speed
  if count >= 3:
    speed = randint(1, 4)
    turtle3.forward(speed)
    t3 = t3 + speed
  if count >= 4:
    speed = randint(1, 4)
    turtle4.forward(speed)
    t4 = t4 + speed
  if count >= 5:
    speed = randint(1, 4)
    turtle5.forward(speed)
    t5 = t5 + speed
  if count >= 6:
    speed = randint(1, 4)
    turtle6.forward(speed)
    t6 = t6 + speed
  if count >= 7:
    speed = randint(1, 4)
    turtle7.forward(speed)
    t7 = t7 + speed
  if count >= 8:
    speed = randint(1, 4)
    turtle8.forward(speed)
    t8 = t8 + speed
  if count >= 9:
    speed = randint(1, 4)
    turtle9.forward(speed)
    t9 = t9 + speed
  if count >= 10:
    speed = randint(1, 4)
    turtle10.forward(speed)
    t10 = t10 + speed
