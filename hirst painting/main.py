# import colorgram
#
# color_list = []
# colors = colorgram.extract('image.jpg', 48)
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
# print(color_list)
#

from turtle import Turtle , Screen
import random

tom = Turtle()
tom.pensize(20)


screen = Screen()
screen.setup(500,500)
screen.colormode(255)

color_list = [(234, 220, 96), (174, 81, 22), (236, 48, 85), (233, 162, 89), (69, 187, 230),
              (171, 54, 106), (250, 54, 16), (93, 197, 129), (231, 128, 155),
              (111, 218, 246), (123, 233, 208), (19, 126, 212), (51, 121, 41),
              (249, 222, 0), (22, 178, 214), (247, 144, 156), (54, 177, 84), (83, 24, 34),
              (95, 39, 18), (29, 88, 36), (187, 23, 13), (30, 65, 37), (186, 18, 32),
              (245, 160, 151), (178, 135, 38), (254, 5, 18), (37, 128, 230), (255, 9, 5), (126, 88, 0)]

tom.color("white")
y_position = -200
for i in range(10):
    x_position = -200
    for j in range(10):
        tom.speed("fastest")
        tom.forward(50)
        tom.goto(x_position, y_position)
        tom.pendown()
        tom.color(random.choice(color_list))
        tom.dot(20)
        tom.penup()
        x_position += 50
    y_position += 50
    tom.backward(500)






screen.exitonclick()
