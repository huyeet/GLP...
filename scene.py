from manim import *
# Thanks 3blue1brown for inspiring me to create this project.


# This class is an inheritance from the parent Scene class
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # Create a circle
        circle.set_fill(RED_A, opacity=0.5)  # set the color and transparency

        square = Square()  # Create a square
        square.flip()  # Flip Horizontally
        square.rotate(-9 * TAU / 28)  # Rotate a certain amount TAU is essentially 2pi

        self.play(ShowCreation(square))  # Animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # Fade out animation

