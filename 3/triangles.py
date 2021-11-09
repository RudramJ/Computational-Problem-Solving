"""
file: triangles.py

description: This program draws a triangle using
recursion as prescribed in Activity 1.

language: python3
author: Rudram Joshi
author: Moinuddin memon
"""
import turtle as t
# global constants for window dimensions
COLORS = 'red', 'orange', 'green', 'blue', 'teal'
LENGTH_OF_TRIANGLE = 150
DEPTH = 6

def draw_triangles_1( length ):
    """
    Draws a red triangle
    :param length: Length of one side of triangle
    :pre:  turtle down, lower left, facing east
    :post:  turtle down, lower left, facing east
    :return: None
    """
    t.pencolor('red')
    for _ in range(3):
        t.forward(length)
        t.left( 120 )

def draw_triangles_2( length ):
    """
    draws a green triangle and calls the
    method draw_triangles_1 after every side
    to draw red triangle with half side length
    :param length: Length of one side of triangle
    :pre:  turtle down, lower left, facing east
    :post:  turtle down, lower left, facing east
    :return: None
    """
    t.pendown()
    for _ in range(3):
        t.pencolor('green')
        t.forward( length )
        draw_triangles_1( length/2 )
        t.left(120)
    t.penup()

def draw_triangles_rec(length, depth):
    """
    draws a triangle mentioned in activity 1 using recursion
    Calls the method itself after every side of triangle drawn
    decreasing the length by half and depth by 1 till 0.
    :param length: Length of one side of triangle
    :param depth: Number of times to call the method
    :return: None
    """
    if depth == 0:
        pass
    else:
        t.pendown()
        # drawing the triangles
        for _ in range(3):
            t.pencolor(COLORS[depth % len(COLORS)])
            t.forward(length)
            draw_triangles_rec(length / 2, depth -1)
            t.left(120)

def main():
    """
    The main function.
    initializes the parameters for drawing.
    Calls the drawing triangle method to draw
    the required triangles.
    :pre: (relative)
    pos (0,0), heading (east), pen down
    :post: (relative)
    pos (0,0), heading (east), pen up
    :return: None
    """
    t.speed(0)
    draw_triangles_rec( LENGTH_OF_TRIANGLE, DEPTH)
    t.mainloop()

if __name__ == '__main__':
    main()