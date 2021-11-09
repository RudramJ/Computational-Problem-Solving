"""
file: polygons.py

description: This program draws a polygon with
the number of side supplied at the run time. The
polygon is drawn recursively with decreasing length
until the shape is triangle.

language: python3
author: Rudram Joshi
author: Moinuddin memon
"""
import turtle as t
import sys

# global constants for window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
# Length of sides of Polygon
LENGTH_OF_SIDES = 80
# Limits of sides of Polygon
MAX_NUMBER_OF_SIDES = 8
MIN_NUMBER_OF_SIDES = 3

# "constants" for the color used at each depth, e.g. depth=1 is 'red'
COLORS = 'red', 'orange', 'yellow', 'green', 'blue', 'blueviolet', 'violet'

# pen sizes to use for filled and unfilled polygons
FILL_PEN_WIDTH = 2
UNFILL_PEN_WIDTH = 8

def init():
    """
    Initialize for drawing. (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos (0,0), heading (east), down
    :post: pos (0,0), heading (east), up
    :return: None
    """
    t.setworldcoordinates(-WINDOW_WIDTH / 2, -WINDOW_WIDTH / 2,
                               WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    t.up()
    t.setheading(0)
    t.title('polygons')
    t.speed(0)
    t.tracer(0, 0)

def draw_polygons(numberOfSides, lengthOfSides, toFill):
    """
    A recursive function that draws a polygon ,
    and recursively calls itself to draw a polygon with
    decreasing length of side till the shape is triangle.
    :pre: pos (0,0), heading (east), down
    :post: pos (0,0), heading (east), down
    :param numberOfSides: Number of side of polygon
    :param lengthOfSides: Length of side of polygon
    :param toFill: Whether to fill the polygon or no
    :return: Sum of length of sides of all the polygons
    """
    returnVal = numberOfSides * lengthOfSides
    if numberOfSides < MIN_NUMBER_OF_SIDES:
        return 0
    else:
        t.pendown()
        if (toFill == 'fill'):
            t.color(COLORS[numberOfSides % len(COLORS)])
            t.pensize(FILL_PEN_WIDTH)
            t.begin_fill()
            for _ in range(numberOfSides):
                t.forward(lengthOfSides)
                t.left(180 - (180 * (numberOfSides-2) / numberOfSides))
            t.end_fill()
        else:
            t.pensize(UNFILL_PEN_WIDTH)
        for _ in range(numberOfSides):
            t.pencolor(COLORS[numberOfSides % len(COLORS)])
            t.forward(lengthOfSides)
            t.left(180)
            returnVal += draw_polygons(numberOfSides-1, lengthOfSides/2, toFill)
            t.left(180 - (180 * (numberOfSides-2) / numberOfSides))
            t.left(180)
    return returnVal

def main():
    """
    The main function.
    The init function initializes the parameters for drawing.
    Taking command line arguments of number of sides and
    whether to fill the polygon or not.
    :pre: (relative)
    pos (0,0), heading (east), pen down
    :post: (relative)
    pos (0,0), heading (east), pen down
    :return: None
    """
    init()
    mySides = int( sys.argv[1] )
    fill_state = sys.argv[2]

    if (mySides >= MIN_NUMBER_OF_SIDES and mySides <= MAX_NUMBER_OF_SIDES):
        if (fill_state == 'fill' or fill_state == 'unfill'):
            print('Sum:',draw_polygons(mySides, LENGTH_OF_SIDES, fill_state))
        else:
            print('Please enter "fill" or "unfill" in argv[2].')
            exit()
    else:
        print('Please enter the value of sides between 3 & 8, inclusively in argv[1].')
        exit()

    t.update()
    t.mainloop()

if __name__ == '__main__':
    main()