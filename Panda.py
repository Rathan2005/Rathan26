import turtle as TK

def panda():
    # Initializing turtle
    t.speed(3)
    
    # Face
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.begin_fill()
    t.circle(150)
    t.end_fill()

    # Eyes
    t.penup()
    t.goto(-70, 50)
    t.pendown()
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.penup()
    t.goto(70, 50)
    t.pendown()
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    # Inner eyes
    t.penup()
    t.goto(-70, 70)
    t.pendown()
    t.dot(20)

    t.penup()
    t.goto(70, 70)
    t.pendown()
    t.dot(20)

    # Nose
    t.penup()
    t.goto(0, 30)
    t.pendown()
    t.dot(30)

    # Mouth
    t.penup()
    t.goto(-30, -20)
    t.pendown()
    t.right(90)
    t.circle(30, 180)

    # Ears
    t.penup()
    t.goto(-90, 150)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    t.penup()
    t.goto(90, 150)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    # Hide turtle
    t.hideturtle()

# Set up screen
t.bgcolor("white")
t.color("black")
t.speed(2)

# Draw panda
panda()

# Close the window on click
t.Screen().exitonclick()