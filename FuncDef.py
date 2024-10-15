from manim import *

class FuncDef(Scene):
    def construct(self):

        title = Text("Funções Reais").scale(1.5)
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(FadeOut(title), run_time=2)
        self.wait(1)

        # Conjunto A e B
        conj_A = Ellipse(width=2.5, height=3.5, color=BLACK, fill_color=BLUE,
                        fill_opacity=0.5).move_to(LEFT*2)
        conj_B = Ellipse(width=2.5, height=3.5, color=BLACK, fill_color=RED,
                         fill_opacity=0.5).move_to(RIGHT*2)
        label_A = Tex("A").move_to(LEFT*2 + DOWN*2.2)
        label_B = Tex("B").move_to(RIGHT*2 + DOWN*2.2)

        conj_group = VGroup(conj_A, conj_B)
        self.play(Create(conj_group), run_time=2)
        self.wait(1)

        self.play(Write(label_A), Write(label_B), run_time=2)
        self.wait(1)
        self.play(FadeOut(label_A), FadeOut(label_B), run_time=2)

        # Elementos do conjunto A
        elem1A = Dot().move_to(LEFT*2 + UP)
        label_elem1A = MathTex(r"x_1").move_to(LEFT*2.5 + UP)
        elem2A = Dot().move_to(LEFT*2 + UP*0.33)
        label_elem2A = MathTex(r"x_2").move_to(LEFT*2.5 + UP*0.33)
        elem3A = Dot().move_to(LEFT*2 + DOWN*0.33)
        label_elem3A = MathTex(r"x_3").move_to(LEFT*2.5 + DOWN*0.33)
        elem4A = Dot().move_to(LEFT*2 + DOWN)
        label_elem4A = MathTex(r"x_4").move_to(LEFT*2.5 + DOWN)
        # Elementos do conjunto B
        elem1B = Dot().move_to(RIGHT*2 + UP)
        label_elem1B = MathTex(r"y_1").move_to(RIGHT*2.5 + UP)
        elem2B = Dot().move_to(RIGHT*2 + UP*0.33)
        label_elem2B = MathTex(r"y_2").move_to(RIGHT*2.5 + UP*0.33)
        elem3B = Dot().move_to(RIGHT*2 + DOWN*0.33)
        label_elem3B = MathTex(r"y_3").move_to(RIGHT*2.5 + DOWN*0.333)
        elem4B = Dot().move_to(RIGHT*2 + DOWN)
        label_elem4B = MathTex(r"y_4").move_to(RIGHT*2.5 + DOWN)

        elementosA = VGroup(elem1A, elem2A, elem3A, elem4A)
        label_elementosA = VGroup(label_elem1A, label_elem2A, label_elem3A, label_elem4A)
        elementosB = VGroup(elem1B, elem2B, elem3B, elem4B)
        label_elementosB = VGroup(label_elem1B, label_elem2B, label_elem3B, label_elem4B)

        self.play(Create(elementosA), Write(label_elementosA), run_time=4)
        self.wait(2)
        self.play(Create(elementosB), Write(label_elementosB), run_time=4)
        self.wait(2)

        arrows = [
            CurvedArrow(start_point=elem1A.get_center(), end_point=elem1B.get_center(), color=WHITE,
                tip_shape=StealthTip, angle=-PI/3),
            CurvedArrow(start_point=elem2A.get_center(), end_point=elem2B.get_center(), color=WHITE,
                tip_shape=StealthTip, angle=-PI/3),
            CurvedArrow(start_point=elem3A.get_center(), end_point=elem3B.get_center(), color=WHITE,
                tip_shape=StealthTip, angle=-PI/3),
            CurvedArrow(start_point=elem4A.get_center(), end_point=elem4B.get_center(), color=WHITE,
                tip_shape=StealthTip, angle=-PI/3),
        ]
        self.play(*[Create(arrow) for arrow in arrows], run_time=4)
        self.wait(2)

        # Move o end_point do arrows[1] para nova posição
        new_end_point1 = elem3B.get_center()
        new_end_point2 = elem4B.get_center()
        new_end_point3 = elem1B.get_center()
        self.play(arrows[1].animate.put_start_and_end_on(arrows[1].get_start(), new_end_point1), run_time=3)
        self.play(arrows[1].animate.put_start_and_end_on(arrows[1].get_start(), new_end_point2), run_time=3)
        self.play(arrows[1].animate.put_start_and_end_on(arrows[1].get_start(), new_end_point3), run_time=3)
        self.wait(1)
        self.play(arrows[1].animate.put_start_and_end_on(arrows[1].get_start(), elem2B.get_center()), run_time=2)
        self.wait(3)



        









        # Notação de Elementos dos conjuntos
        # not_A = MathTex(r"x \in A").move_to(LEFT*2 + UP*2)
        # not_B = MathTex(r"f(x) \in B").move_to(RIGHT*2 + UP*2)


        # text = MathTex(r"f: \mathbb{R} \to \mathbb{R}").scale(1.5)
        # self.play(Write(text), run_time=2)





