"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Mariah Mufich.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# TODO: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
jewels = rg.SimpleTurtle('turtle')
jewels.pen = rg.Pen('green',5)
jewels.speed = 10

size = 200
for k in range(15):
    jewels.draw_square(size)
    jewels.pen_up()
    jewels.right(45)
    jewels.forward(10)
    jewels.left(45)
    jewels.pen_down()
    size = size - 15


jaden = rg.SimpleTurtle('turtle')
jaden.pen = rg.Pen('red',5)
jaden.speed = 5

size = 100
for k in range(15):
    jaden.draw_circle(size)
    jaden.pen_up()
    jaden.right(45)
    jaden.forward(10)
    jaden.left(45)
    jaden.pen_down()
    size = size - 15
window.close_on_mouse_click()
