"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Mariah Mufich.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   Write code that constructs a SimpleTurtle with a red Pen
#   and makes it move around a bit.  Don't forget to:
#     -- import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     -- ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
maggie = rg.SimpleTurtle('turtle')
maggie.pen = rg.Pen('pink',5)
maggie.speed = 10

size = 50
for k in range(15):
    maggie.draw_circle(size)
    maggie.pen_up()
    maggie.right(45)
    maggie.forward(10)
    maggie.left(45)
    maggie.pen_down()
    size = size - 15

window.close_on_mouse_click()
