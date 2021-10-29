import turtle

import colorgram
import random
import turtle as hobbs


def Colors():
    hobbs.colormode(255)
    color = colorgram
    g = color.extract("image.jpg.jpg", 31)
    color_list = []
    for x in range(30):
        h = g[x].rgb
        color_tuples = ((h[0], h[1], h[2]))
        color_list += [(color_tuples)]
    return color_list

def Screen():
    hobbs.Screen()
    hobbs.exitonclick()


gogs = turtle.Turtle()
def gogo():
    gogs.hideturtle()
    gogs.pensize(10)
    gogs.speed("fastest")
    gogs.pu()

gogo()
gogs.setheading(225)
gogs.forward(300)
gogs.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    gogs.dot(20, random.choice(Colors()))
    gogs.forward(50)

    if dot_count % 10 == 0:
        gogs.setheading(90)
        gogs.forward(50)
        gogs.setheading(180)
        gogs.forward(500)
        gogs.setheading(0)



Screen()


