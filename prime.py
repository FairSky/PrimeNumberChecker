__author__ = '@PavelVavruska'

import turtle

from src.prime_checker import PrimeChecker
from src.utils.colors import bcolors


def main():
    """
       Initialization of variables
       """
    turtles = []
    wn = turtle.Screen()
    wn.bgcolor("#151515")

    # Creating of turtles
    for x in xrange(0, 10):
        turtles.append(turtle.Turtle())

    # Initialization of turtles
    for x in xrange(0, 10):
        turtles[x].penup()
        turtles[x].tracer(1000)  # speed of rendering
        turtles[x].setpos(-50, -250)
        turtles[x].tracer(50)  # speed of rendering
        turtles[x].left(23 + x * 12)  # direction of turtle
        turtles[x].shape("arrow")
        turtles[x].pendown()
    count = 0  # Set counter of steps to zero (text rows and turtles switcher)

    for x in xrange(1, 1001, 2):
        """
              Main loop - possible prime numbers (only odd numbers)
              """

        # Text output
        bcolors.printOK_BOLD('%6.6s' % str(x)),

        # is_x_prime_or_divisor contains True or divisor
        is_x_prime_or_divisor = PrimeChecker.isPrimeNumber(x)
        turtles[count].color("#FF%d%d" % (30 + 5 * count, 10 + 5 * count),
                             "#FF%d%d" % (30 + 5 * count, 10 + 5 * count))
        turtles[count].forward(7)

        # Graphical and text output of prime numbers
        # in form of colorful stamps and console output
        if is_x_prime_or_divisor == True:
            bcolors.printBOLD('%-4s' % str(is_x_prime_or_divisor)),
            turtles[count].circle(3)
            turtles[count].color("#555555", "#FFFF00")
        else:
            bcolors.printError('%-4s' % str(is_x_prime_or_divisor)),

        # Counter reset
        count += 1
        if count > 9:
            count = 0
            print  # making new row at the end of 10th column in text output

    # Turtle captions - Column indexes
    for x in xrange(0, 10):
        turtles[x].color("#FFFFFF", "#FF3333")
        turtles[x].write("%d" % x,\
            True, align="right", font=("Arial", 16, "bold"))

    # Render user interface
    turtle.penup()
    turtle.color("#FFFFFF", "#FF3333")
    turtle.setpos(-50, 220)
    turtle.write("Visualization of columns:",\
        True, align="right", font=("Arial", 16, "bold"))
    turtle.color("#999999", "#FF3333")
    turtle.setpos(-60, 195)
    turtle.write("circles = prime numbers",\
        True, align="right", font=("Arial", 12, "bold"))
    turtle.setpos(280, -265)
    turtle.write("@PavelVavruska 2012",\
        True, align="right", font=("Arial", 12, "bold"))
    turtle.exitonclick()  # Waiting for user interaction at the end

if __name__ == '__main__':
    main()
