from manim import *

class RiemannSum(Scene):
    def construct(self):
        # Definir o eixo x e o eixo y
        axes = Axes(
            x_range=[-1, 4, 1],
            y_range=[0, 10, 1],
            axis_config={"color": RED},
        )

        # Desenha o gráfico da função f(x) = x^2
        graph = axes.plot(lambda x: x**2, color=BLUE)

        # Adiciona o gráfico e o título à cena
        graph_label = axes.get_graph_label(graph, label="f(x) = x^2")
        self.play(Create(axes), Create(graph), Write(graph_label))

        # Definir o número de retângulos e o intervalo da soma de Riemann
        num_rects = 10
        riemann_rects = axes.get_riemann_rectangles(
            graph,
            x_range=[0, 3],
            dx=3/num_rects,
            stroke_width=0.5,
            stroke_color=WHITE,
            fill_opacity=0.6,
            color=[BLUE, GREEN]
        )

        # Adiciona as somas de Riemann (retângulos)
        self.play(Create(riemann_rects))

        for i in range(10, 101, 10):
            self.remove(riemann_rects)
            new_riemann_rects = axes.get_riemann_rectangles(
                graph,
                x_range=[0, 3],
                dx=3/i,
                stroke_width=0.5,
                stroke_color=GREEN,
                fill_opacity=0.6,
                color=[BLUE, GREEN]
            )
            self.play(Transform(riemann_rects, new_riemann_rects), run_time=1)
        
        filled_area = axes.get_area(graph, [0, 3], color=GREEN, opacity=0.6)
        self.play(Create(filled_area))
        self.wait(2)
