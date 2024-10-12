from manim import *

class HelloWorld(Scene):
    def construct(self):
        # Add a circle and a square
        circle = Circle()
        square = Square()

        text = Text("Hello, World!", font_size=76)
        text.center()

        
        self.play(
            Write(text, run_time=3)
        )

        # Play with transform
        self.play(
            Transform(text[0:5], circle),
            run_time=3,
            rate_func=linear
        )

        self.play(
            Transform(text[5:], square),
            run_time=3,
            rate_func=linear
        )

        self.wait(1)

        self.play(
            FadeOut(text),
            run_time=3
        )
