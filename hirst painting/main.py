# import colorgram

# rgb_colors = []
# # Extract 6 colors from an image.
# colors = colorgram.extract('damien-hirst-lactulose.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import turtle as t
t.colormode(255)
from turtle import Screen
import random
tim = t.Turtle()
tim.hideturtle()
tim.speed('fastest')
color_list = [(239, 236, 238), (238, 237, 236), (237, 237, 241), (25, 108, 164), (194, 38, 81), (238, 161, 49), (234, 215, 85), (226, 237, 228), (223, 137, 176), (144, 108, 56), (102, 197, 219), (206, 166, 29), (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), (118, 192, 140), (3, 186, 176), (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184), (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31)]
tim.penup()
tim.setheading(245)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20,random.choice(color_list))
    tim.penup()
    tim.forward(50)
    
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)  
        tim.forward(500)
        tim.setheading(0)








screen = Screen()
screen.exitonclick()



























