import turtle
import math
a=turtle.Turtle()
def fractal(size,heading,initial,angle,id):
	if(size>40):
		if(id==1):
			a.penup()
			a.goto(initial)
			a.pendown()
			a.setheading(heading-angle)
			a.forward(size)
			initial=[a.position()[0],a.position()[1]]
			fractal(size*0.9,heading-angle,initial,angle,-1)
			fractal(size*0.9,heading-angle,initial,angle,1)
		else:
			a.penup()
			a.goto(initial)
			a.pendown()
			a.setheading(heading+angle)
			a.forward(size)
			initial=[a.position()[0],a.position()[1]]
			fractal(size*0.9,heading+angle,initial,angle,-1)
			fractal(size*0.9,heading+angle,initial,angle,1)
	return
a.left(90)
a.forward(100)
fractal(70,90,[0,100],25,1)
fractal(70,90,[0,100],25,-1)
turtle.done()
