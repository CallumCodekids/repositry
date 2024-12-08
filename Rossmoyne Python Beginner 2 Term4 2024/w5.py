import turtle
turtle.colormode(255)

def square(side_length):
    count = 0
    while count < 4:
        turtle.forward(side_length)
        turtle.left(90)
        count = count + 1
        
        
def equilateral_shape(side_length, number_of_sides):
    count = 0
    while count < number_of_sides:
        turtle.forward(side_length)
        turtle.left(360 / number_of_sides)
        count = count + 1
        
def between_0_255(num):
    return min(max(num, 0),255)
        
def pattern(number_of_times, starting_sides, starting_side_length, turn_amount, side_number_growth, side_length_growth, red, green, blue, red_growth, green_growth, blue_growth):
    count = 0
    while count < number_of_times:
        turtle.color(between_0_255(red + red_growth*count), between_0_255(green + green_growth*count), between_0_255(blue + blue_growth*count))
        equilateral_shape(starting_side_length + side_length_growth * count ,starting_sides +  side_number_growth * count)
        turtle.left(turn_amount)
        count = count +1
        
      
turtle.speed(0)
pattern(5, 40, 20, 120, 50, 19, 1, 125, 2, 10, 20, 30)



