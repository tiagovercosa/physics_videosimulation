from manim import *

class FunctionConstant(Scene):
    def construct(self):

        # Título
        title = Text("Função Constante", font="Times New Roman",
                      font_size=76.0)
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(title.animate.shift(UP*3 + LEFT*4.5).scale(0.5), run_time=2)

        # Define o plano cartesiano
        axes = Axes(
            x_range=[-5, 5, 1], y_range=[-2, 4, 1],
            x_length=10,
            axis_config={
                "include_numbers": True,
                "tip_shape": StealthTip
                }
        )

        # Define a função constante
        graph = axes.plot(lambda x: 2, color=BLUE)
        graph_label = axes.get_graph_label(graph, label="f(x) = 2").shift(UP*1)
        alpha = ValueTracker(0)
        point = always_redraw(
            lambda: Dot(
                graph.point_from_proportion(alpha.get_value()),
                color=RED
            )
        )
        line = always_redraw(
            lambda: DashedLine(
                axes.c2p(alpha.get_value() * 10 - 5, 2),
                axes.c2p(alpha.get_value() * 10 - 5, 0),
                color=RED
            )
        )

        self.play(Create(axes, run_time=3))
        self.play(Create(graph), Write(graph_label), run_time=4)
        self.wait(1)
        self.play(Indicate(graph), Indicate(graph_label), run_time=3)
        self.wait(1)
        self.add(point, line)
        self.wait(1)
        self.play(alpha.animate.set_value(1), rate_func=linear, run_time=6)
