import turtle as t

paint = t.Turtle()
paint2 = t.Turtle()

paint.getscreen()


paint.pencolor("red")

paint.pensize(6)

paint.fillcolor("pink")
paint.begin_fill()

for i in range(4):
    paint.forward(200)
    paint.right(90)
    paint2.backward(200)
    paint2.right(90)

paint.end_fill()

t.mainloop()

# t.fillcolor("green")
# t.end_fill()
# t.begin_fill()
# t.fillcolor("red")

# t.begin_fill()
# t.end_fill()