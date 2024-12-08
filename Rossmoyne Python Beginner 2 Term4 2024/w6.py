import turtle
from w5 import equilateral_shape

turtle.speed(0)
count = 0
while count < 100:
    equilateral_shape(20, count +3)
    count = count +1
