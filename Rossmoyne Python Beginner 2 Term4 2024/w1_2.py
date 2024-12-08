import turtle

turtle.speed(0)

sq_count = 0
while sq_count < 3600:
    count = 0
    while count < 4:
        turtle.forward(100)
        turtle.left(90)
        count = count + 1
    sq_count = sq_count +1
    turtle.right(7)
    turtle.forward(10)
