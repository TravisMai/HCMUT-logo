import turtle

turtle.title('HCMUT LOGO')

def draw_rhombus(t, color):
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(100) # move forward 100 units
        t.left(60)     # turn left by 60 degrees
        t.forward(100) # move forward 100 units
        t.left(120)    # turn left by 120 degrees
    t.end_fill()
    t.forward(100) # move forward 100 units
    t.left(60)     # turn left by 60 degrees
    t.forward(100) # move forward 100 units
    t.left(60)    # turn left by 60 degreesacc

def draw_shape(t):
    draw_rhombus(t,"#1488db")
    draw_rhombus(t,"#042b92")

def write(x,y,color,size,name):
    turtle.pencolor('white')
    turtle.setposition(-x,-y)
    turtle.color(color)
    style = ('Sans-serif', size, 'bold')
    turtle.write(name, font=style)
    turtle.hideturtle()

t = turtle.Turtle()
t.left(90)     
t.speed(0)
t.penup()
t.setposition(86.60254038,0)
t.pendown()
for i in range(3):
    draw_shape(t)
    t.right(120)

write(60,80,"#042b92",60,"BK")
write(60,100,"#1488db",24,"TP.HCM")
t.hideturtle()
turtle.mainloop()