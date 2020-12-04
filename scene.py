from manim import *
# Thanks 3blue1brown for inspiring me to create this project.


# This class is an inheritance from the parent Scene class
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # Create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(ShowCreation(circle))  # show the circle on screen
