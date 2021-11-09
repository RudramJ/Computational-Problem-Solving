"""
file: lumber.py

description: This program draws random type of trees
with random height on mouse click. Then let user decide
whether to stock up the logs of trees in sorted manner
or not.

language: python3
author1: Rudram Joshi
author1: Moinuddin Memon
"""
from random import randint
import turtle as t
import yard

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# Constants for type of trees
MAPLE_TREE = 1
PINE_TREE = 2
MANGO_TREE = 3

# Constants for drawing
DIVIDE_SIZE = 100   # Divide line for buttons
LIMIT_FROM_TOP_WINDOW = 50  # Limit for top of trunk

LOWEST_SIZE_OF_TRUNK = 50
HIGHEST_SIZE_OF_TRUNK = 250
SIZE_OF_LEAF = 40
STEM_WIDTH = 10

# Constants for drawing Logs
SORT_LOGS = 1
UNSORT_LOGS = 0

# Creating object of class Lumberyard
myYardObject = yard.LumberYard()

def init_function():
    """
    Initialize for drawing. (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos (0,0), heading (east), down
    :post: pos (0,0), heading (north), up
    :return: None
    """
    t.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    t.up()
    t.setheading(0)
    t.title('lumber')
    t.speed(0)  # set speed of drawing
    divideWindow()  # Function to draw dividing line
    drawButton()    # Function to draw buttons

def drawPineOrMango(noOfSide):
    """
    Draw leaf of tree based on number
    of sides.
    :pre: (relative)
    pos (0, 0), heading (north), pen up
    :post: (relative)
    pos (0, 0), heading (north), pen up
    :param noOfSide: Type of Leaf to draw
    :return:    None
    """
    t.penup()
    t.backward(SIZE_OF_LEAF / 2)
    t.pendown()
    for _ in range (noOfSide):
        t.forward(SIZE_OF_LEAF)
        t.left(360 / noOfSide)
    t.penup()
    t.forward(SIZE_OF_LEAF / 2)

def drawTree(typeOfTree):
    """
    Draw random tree based on input parameter.
    :pre: (relative)
    pos (0, 0), heading (north), pen up
    :post: (relative)
    pos (0, 0), heading (north), pen up
    :param typeOfTree: The type of tree to draw
    :return: None
    """
    trunkLength = getRamdomNumber(LOWEST_SIZE_OF_TRUNK, HIGHEST_SIZE_OF_TRUNK)
    myYardObject.addLog(trunkLength)

    t.pendown()
    t.forward( trunkLength )
    t.right(90)
    if(typeOfTree == 1):    #Draws Maple Leaf
        t.circle(SIZE_OF_LEAF/2)
    elif(typeOfTree == 2):  #Draws Pine Leaf
        drawPineOrMango( 3 )
    elif (typeOfTree == 3): #Draws Mango Leaf
        drawPineOrMango( 4 )
    t.left(90)
    t.backward( trunkLength )
    t.penup()

def doClick(x, y):
    """
    Gets the coordinates from mouse click.
    And sends the turtle to that coordinates
    to draw the trees.
    :pre: (relative)
    pos (x, y), heading (north), pen up
    :post: (relative)
    pos (x, y), heading (north), pen up
    :param x: X-coordinate
    :param y: Y-coordinate
    :return: None
    """
    if( (y < WINDOW_HEIGHT/2 - LIMIT_FROM_TOP_WINDOW) and (y > -WINDOW_HEIGHT/2 + DIVIDE_SIZE) ):
        t.goto(x, y)
        t.setheading(90)
        drawTree( getRamdomNumber(1, 3) )

    elif( (y < -WINDOW_HEIGHT/2 + DIVIDE_SIZE) ):

        if( x < 0 ):
            drawLogs(SORT_LOGS)
        else:
            drawLogs(UNSORT_LOGS)

def getRamdomNumber(lowerLimit, upperLimit):
    """
    Returns the random number between the limits
    provided in the input parameter.
    :param lowerLimit: LowerLimit
    :param upperLimit: UpperLimit
    :return: Random number between limits
    """
    return randint(lowerLimit, upperLimit)

def drawLogs(isSorted):
    """
    Clears the existing drawing and draw the pile of
    logs of the trees according to the button click.
    And wait for mouse-click to end the program.
    :pre: (relative)
    pos (0, 0), heading (east), pen up
    :post: (relative)
    pos (0, STEM_WIDTH * len(myLogs)), heading (north), pen up
    :param isSorted: Whether to sort the log or not
    :return: None
    """
    myLogs = myYardObject.allLogs()
    print("Total length of the logs: ",sum(myLogs))
    t.clear()
    t.goto(0, 0)
    t.right(90)

    if ( isSorted ):
        myLogs.sort(reverse = True)

    for i in myLogs:
        t.backward(i / 2)
        t.pendown()
        t.forward(i)
        t.left(90)
        t.forward(STEM_WIDTH)
        t.left(90)
        t.forward(i)
        t.left(90)
        t.forward(STEM_WIDTH)
        t.penup()
        t.left(180)
        t.forward(STEM_WIDTH)
        t.right(90)
        t.forward(i / 2)

    t.exitonclick()

def divideWindow():
    """
    Draw the line for dividing the buttons and the
    drawing based on size defined.
    Gets the coordinates from mouse click.
    :pre: (relative)
    pos (0, 0), heading (east), pen up
    :post: (relative)
    pos (0, 0), heading (east), pen up
    :return: None
    """
    t.right(90)
    t.forward(WINDOW_HEIGHT/2 - DIVIDE_SIZE)
    t.right(90)
    t.forward(WINDOW_WIDTH/2)
    t.right(180)
    t.pendown()
    t.forward(WINDOW_WIDTH)
    t.penup()
    t.right(180)
    t.forward(WINDOW_WIDTH/2)
    t.right(90)
    t.forward(WINDOW_HEIGHT/2 - DIVIDE_SIZE)
    t.right(90)

def drawButton():
    """
    Draw the buttons based on size defined.
    Gets the coordinates from mouse click.
    :pre: (relative)
    pos (0, 0), heading (east), pen up
    :post: (relative)
    pos (0, 0), heading (north), pen up
    :return: None
    """
    t.right(90)
    t.forward(WINDOW_HEIGHT / 2 - DIVIDE_SIZE + DIVIDE_SIZE/2)
    t.right(90)
    t.forward(WINDOW_WIDTH/2 - DIVIDE_SIZE)
    t.write("Harvest and sort", align="center", font=("Calibri", 15, "normal"))
    t.backward(WINDOW_WIDTH / 2)
    t.write("Harvest unsorted", align="center", font=("Calibri", 15, "normal"))
    t.forward(WINDOW_WIDTH / 2 - DIVIDE_SIZE)
    t.right(90)
    t.forward(WINDOW_HEIGHT / 2 - DIVIDE_SIZE + DIVIDE_SIZE/2)

def main():
    """
    The init function initializes and draws the pre conditions
    for drawing.
    Onscreen click function gets the coordinates of the user click
    to doClick function and sends the turtle to that position.
    :return: None
    """
    init_function()
    t.onscreenclick(doClick)
    t.mainloop()

if __name__ == '__main__':
    main()
