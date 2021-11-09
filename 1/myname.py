"""
file: myname.py

description: This program designs the typography for,
and implements a program that uses it to draw my family
name using the Python's turtle graphic module.

Drawing "JOSHIIR" since my family name is "JOSHI",
I am adding "IR" to full-fill the criteria of Homework.

language: python3
author: Rudram Joshi
"""
import turtle
import math

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# global constant for the "myname" dimensions
EDGE_GAPING = 10    # Gap between name and window
NO_OF_LETTERS = 7   # No of Letters to draw
SPACING = EDGE_GAPING   # Spacing between letters
STARTING_POINT = (EDGE_GAPING - (WINDOW_WIDTH/2))  # Position to begin drawing

# Letter width and height with respect to window size, spacing and no of letters
LETTER_WIDTH = ( WINDOW_WIDTH - (2*EDGE_GAPING) -
                ( SPACING*(NO_OF_LETTERS-1) ) ) / ( NO_OF_LETTERS )
LETTER_HEIGHT = LETTER_WIDTH

def init():
    """
    Initialize for drawing. (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos (0,0), heading (east), down
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    turtle.up()
    turtle.setheading(0)
    turtle.title('myname')
    turtle.speed(10)     # set speed of drawing

def drawLetterJ():
    """
    Draw the letter "J".
    :pre: (relative)
    pos (STARTING_POINT,0), heading (east), pen up
    :post: (relative)
    pos (STARTING_POINT+ 1*LETTER_WIDTH + 0*SPACING, 0), heading (east), pen up
    :return: None
    """
    turtle.pendown()
    turtle.forward( LETTER_WIDTH / 2 )
    turtle.left( 90 )
    turtle.forward( LETTER_HEIGHT )
    turtle.right( 90 )
    turtle.penup()
    turtle.backward( LETTER_WIDTH / 2 )
    turtle.pendown()
    turtle.forward( LETTER_WIDTH )
    turtle.penup()
    turtle.right( 90 )
    turtle.forward( LETTER_HEIGHT )
    turtle.left( 90 )

def drawLetterO():
    """
    Draw the letter "O".
    :pre: (relative)
    pos (STARTING_POINT + 1*LETTER_WIDTH + 1*SPACING, 0), heading (east), pen up
    :post: (relative)
    pos (STARTING_POINT + 2*LETTER_WIDTH + 1*SPACING, 0), heading (east), pen up
    :return: None
    """
    turtle.forward( LETTER_WIDTH / 2 )
    turtle.pendown()
    turtle.circle( LETTER_WIDTH / 2 )
    turtle.penup()
    turtle.forward( LETTER_WIDTH / 2 )

def drawLetterS():
    """
    Draw the letter "S".
    :pre: (relative)
    pos (STARTING_POINT + 2*LETTER_WIDTH + 2*SPACING, 0), heading (east), pen up
    :post: (relative)
    pos (STARTING_POINT + 3*LETTER_WIDTH + 2*SPACING, 0), heading (east), pen up
    :return: None
    """
    turtle.pendown()
    turtle.forward( LETTER_WIDTH / 2 )
    turtle.circle( LETTER_WIDTH / 4, 180 )
    turtle.circle( -LETTER_WIDTH / 4, 180 )
    turtle.forward( LETTER_WIDTH / 2 )
    turtle.penup()
    turtle.right( 90 )
    turtle.forward( LETTER_HEIGHT )
    turtle.left( 90 )

def drawLetterH():
    """
    Draw the letter "H".
    :pre: (relative)
    pos (STARTING_POINT + 3*LETTER_WIDTH + 3*SPACING, 0), heading (east), pen up
    :post: (relative)
    pos (STARTING_POINT + 4*LETTER_WIDTH + 3*SPACING, 0), heading (east), pen up
    :return: None
    """
    turtle.left( 90 )
    turtle.pendown()
    turtle.forward( LETTER_HEIGHT )
    turtle.penup()
    turtle.backward( LETTER_HEIGHT / 2 )
    turtle.right( 90 )
    turtle.pendown()
    turtle.forward( LETTER_WIDTH )
    turtle.penup()
    turtle.left( 90 )
    turtle.forward( LETTER_HEIGHT / 2 )
    turtle.left( 180 )
    turtle.pendown()
    turtle.forward( LETTER_HEIGHT )
    turtle.left( 90 )
    turtle.penup()

def drawLetterI():
    """
    Draw the letter "I".
    :pre: (relative)
    pos (STARTING_POINT + 4*LETTER_WIDTH + 4*SPACING, 0), heading (east), pen up
    :post: (relative)
    pos (STARTING_POINT + 5*LETTER_WIDTH + 4*SPACING, 0), heading (east), pen up
    :return: None
    """
    turtle.pendown()
    turtle.forward( LETTER_WIDTH )
    turtle.penup()
    turtle.backward( LETTER_WIDTH / 2 )
    turtle.left( 90 )
    turtle.pendown()
    turtle.forward( LETTER_HEIGHT )
    turtle.right( 90 )
    turtle.penup()
    turtle.backward( LETTER_WIDTH / 2 )
    turtle.pendown()
    turtle.forward( LETTER_WIDTH )
    turtle.penup()
    turtle.right( 90 )
    turtle.forward( LETTER_HEIGHT )
    turtle.left( 90 )

def drawLetterR():
    """
    Draw the letter "R".
    Since I is repeated, the position will be
    STARTING_POINT + 6*LETTER_WIDTH + 6*SPACING
    :pre: (relative)
    pos (STARTING_POINT + 6*LETTER_WIDTH + 6*SPACING, 0), heading (east), pen up
    :post: (relative)
    pos (STARTING_POINT + 7*LETTER_WIDTH + 6*SPACING, 0), heading (east), pen up
    :return: None
    """
    turtle.left( 90 )
    turtle.pendown()
    turtle.forward( LETTER_HEIGHT )
    turtle.right( 90 )
    turtle.forward( LETTER_HEIGHT / 2 )
    turtle.circle( -LETTER_HEIGHT / 4, 180 )
    turtle.forward( LETTER_HEIGHT / 2 )
    turtle.left( 90 )
    # math library is used to calculate the angle and length
    # for slant line of letter "R".
    turtle.left( math.atan(LETTER_WIDTH/(LETTER_HEIGHT/2)) * (180/math.pi) )
    turtle.forward( math.sqrt( (LETTER_WIDTH ** 2) + (LETTER_HEIGHT/2 ** 2) ) )
    turtle.penup()
    turtle.setheading( 0 )

def drawFamilyName():
    """
    The function to call the letters to draw
    the family name.
    :pre: (relative)
    pos (0,0), heading (east), pen down
    :post: (relative)
    pos (STARTING_POINT + 7*LETTER_WIDTH + 6*SPACING, 0), heading (east), pen up
    :return: None
    """
    # setting starting point for turtle
    turtle.setposition(STARTING_POINT, 0)

    # functions of letters can be interchanged.
    drawLetterJ()
    turtle.forward(SPACING)     # Spacing between letter
    drawLetterO()
    turtle.forward(SPACING)
    drawLetterS()
    turtle.forward(SPACING)
    drawLetterH()
    turtle.forward(SPACING)
    drawLetterI()
    turtle.forward(SPACING)
    drawLetterI()
    turtle.forward(SPACING)
    drawLetterR()

def main():
    """
    The main function.
    The init function initializes the parameters for drawing.
    The drawFamilyName functions draws the name using the different letters.
    The turtle main loop is for visualization of drawing.

    :pre: (relative)
    pos (0,0), heading (east), pen down
    :post: (relative)
    pos (STARTING_POINT + 7*LETTER_WIDTH + 6*SPACING, 0), heading (east), pen up
    :return: None
    """
    init()
    drawFamilyName()
    turtle.mainloop()

if __name__ == '__main__':
    main()