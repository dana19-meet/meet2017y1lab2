import turtle
#Everything that comes after the # is a
#comment.
#It is a note to the person reading the code.
#The computer ignores it.
#Write your code below here...
# ...and end it before the next line.
turtle.penup()
#Brings the pen up, so
#nothing will be drawn
turtle.pendown() #Puts the pen down, so we
#are ready to draw!
#turtle.goto(x,y) #Go to the position
# x"&"y",
#but write in numbers
#instead
turtle.penup() #Pick up the pen so it doesn’t
#draw
turtle.goto(-200,-100)  #Move the turtle to the
#position (-200, -100)
#on the screen
turtle.pendown()  #Put the pen down to start
#drawing
#Draw the M:
turtle.goto(-200,-100+200)
turtle.goto(-200+50,-100)
turtle.goto(-200+100,-100+200)
turtle.goto(-200+100,-100)
turtle.penup()#Pick up the pen so it doesn’t
#draw
#turtle.goto(-200+100,-50)  #Move the turtle to the
#position (-200+100,-50)
#on the screen

#drawing
#Draw the E:
turtle.goto(-50,-100)
turtle.pendown()  #Put the pen down to start
turtle.goto(-50,-100+200)
turtle.goto(50,-100+200)
turtle.penup() #Pick up the pen so it doesn’t
turtle.goto(-50,-100+100)
turtle.pendown()
turtle.goto(50,-100+100)
turtle.penup()
turtle.goto(-50,-100)
turtle.pendown()
turtle.goto(50,-100)
turtle.penup()

#Draw the E:








turtle.mainloop()
