from manim import * 
import numpy as np
from manim.mobject.geometry.tips import ArrowTriangleFilledTip


class MainFigure(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.set_width(25)

        arrow1 = Arrow(LEFT * 1.5, RIGHT * 1.5, fill_color=BLACK, stroke_color=BLACK).shift(UP * 4)
        sup_text = Paragraph("maximise\n loopiness", color=BLACK).scale(0.6).next_to(arrow1, DOWN, SMALL_BUFF)

        one = ImageMobject("figures/mnist/1.png").scale(0.5).next_to(arrow1, LEFT)
        two = ImageMobject("figures/mnist/2.png").scale(0.5).next_to(arrow1, RIGHT)


        mnist_group = Group(arrow1, sup_text, one, two)
        self.add(mnist_group)

        arrow = Arrow(LEFT * 1.5, RIGHT * 1.5, fill_color=BLACK, stroke_color=BLACK).next_to(arrow1, DOWN, LARGE_BUFF * 6)
        sup_text = Paragraph("maximise\n threat on \n my queen", color=BLACK).scale(0.6).next_to(arrow, DOWN, SMALL_BUFF)

        one = ImageMobject("figures/chess/1.png").scale(0.38).next_to(arrow, LEFT)
        two = ImageMobject("figures/chess/2.png").scale(0.38).next_to(arrow, RIGHT)

        self.add(arrow, sup_text, one, two)