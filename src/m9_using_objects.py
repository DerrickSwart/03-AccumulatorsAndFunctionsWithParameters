"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Derrick Swart.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()
def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(400, 400)

    circle_1 = rg.Circle(rg.Point(50, 50), 10)
    circle_1.fill_color = 'red'
    circle_2 = rg.Circle(rg.Point(50, 100), 20)
    circle_2.attach_to(window)
    circle_1.attach_to(window)
    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(400, 400)
    circle = rg.Circle(rg.Point(50,50), 10)
    color = 'red'
    circle.fill_color = color
    print('circle color :', color)
    thick = 5
    circle.outline_thickness = thick
    print('thickness:', thick)
    x_coor = 50
    y_coor = 50
    print('center point :', x_coor, ',', y_coor)
    circle.center = rg.Point(x_coor, y_coor)
    print("x coorinate of circle :", x_coor)
    print('y coordinate of circle :', y_coor)
    circle.attach_to(window)

    print(' ')

    rec = rg.Rectangle(rg.Point(100, 100), rg.Point(200, 20))
    color2 = 'blue'
    rec.fill_color = color2
    print('rectangle color:', color2)
    thick_rec = 10
    rec.outline_thickness = thick_rec
    print('thickness of rec', thick_rec)
    x = 100 + (50/2)
    y = 20 + (80/2)
    print('center point rec', x, ',', y)
    print('x coor. center of rec:', x)
    print('y coor. center of rec :', y)
    rec.attach_to(window)

    window.render()
    window.close_on_mouse_click()

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 4. Implement and test this function.
    rg.RoseWindow(400, 400)
    line_1 = rg.Line(rg.Point(10, 100), rg.Point(10,300))
    thick = 10
    line_1.thickness = thick
    print('big line thickness:', thick)
    mid = line_1.get_midpoint()
    print('thick line midpoint:', mid)
    x = 10
    y = 300 - 100
    print('x coor. of midpoint:', x)
    print('y coor. of midpoint', y)

    line_1.attach_to(window)
    line_2.a

    line_2 = rg.Line(rg.Point(50, 100), rg.Point(50,300))

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
