from manim import *

class IntroScene(Scene):

    def construct(self):

        circle = Circle(2.5, color=BLUE_E, fill_opacity=1)
        self.play(DrawBorderThenFill(circle, stroke_width=10.), run_time=2)
        self.wait(0.5)

        phi = MathTex(r"\Phi", font_size=106)

        title = Text("Phys", font_size=76, slant="ITALIC")

        subtitle = Text(
            "Traduzindo a Natureza", font_size=36,
            ).shift(DOWN * 0.5)

        phi.move_to(LEFT + UP * 0.5)
        title.next_to(phi, RIGHT)

        cont1 = Arc(2.8, TAU * 1 / 4, stroke_width=15)
        cont2 = Arc(2.8, -TAU * 1 / 4, stroke_width=15)
        
        self.play(Write(phi), Write(title), run_time=1)

        self.play(Write(subtitle), Create(cont1), Create(cont2), run_time=2)
        self.wait(1)
        self.play(FadeOut(*self.mobjects), run_time=1)
