import turtle

wn = turtle.Screen()
wn.bgcolor('dark purple')
wn.tracer(3)

zig = turtle.Turtle()
zig.pensize(1.3)
zig.color ('orange')
zig.speed (15)

#Espiral
for i in range (180):
    zig.right(48)
    zig.forward(i)

#Hexágono
for i in range (270):
    zig.right(60)
    zig.forward(i)
