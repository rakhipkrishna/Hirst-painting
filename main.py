import colorgram

"""
rgb_colors = []
colors = colorgram.extract('image.jpeg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(125, 174, 187), (49, 114, 142), (197, 132, 164), (205, 154, 93), (119, 181, 172), (45, 133, 118), (151, 65, 95), (193, 91, 130), (151, 92, 54), (58, 160, 152), (197, 208, 221), (59, 157, 165), (232, 193, 207), (151, 26, 52), (179, 152, 52), (14, 35, 89), (207, 95, 64), (223, 173, 189), (27, 52, 118), (240, 229, 222), (159, 209, 198), (217, 203, 114), (183, 215, 204), (152, 207, 216), (76, 24, 63), (20, 95, 69), (185, 187, 205), (109, 121, 158), (19, 57, 39), (145, 32, 24)]

tim.setheading(225)
tim.forward(308)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()




