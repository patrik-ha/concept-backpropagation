from manim import * 
import numpy as np
from manim.mobject.geometry.tips import ArrowTriangleFilledTip


class MainFigure(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.set_width(10)
        self.camera.frame.move_to(RIGHT * 3)

        latent = Rectangle(color=GREEN, height=2, width=0.2, fill_opacity=0.3)
        s = MathTex("s", color=BLACK).scale(0.75).next_to(latent, DOWN)
        odot = MathTex("\\odot", color=BLACK).scale(0.7).next_to(latent, RIGHT)
        max_plane = Rectangle(color=RED, height=2, width=0.2, fill_opacity=0.3).next_to(odot, RIGHT)
        s_pert = MathTex("s^*", color=BLACK).scale(0.75).next_to(max_plane, DOWN).shift(UP * 0.11).shift(LEFT * 0.1)

        encompassing = SurroundingRectangle(Group(latent, odot, max_plane, s, s_pert), color=BLACK, stroke_width=2)
        enc_edge = max_plane.get_edge_center(RIGHT) + RIGHT * 0.25
        arr = Line(enc_edge, enc_edge + RIGHT * 0.5, fill_color=BLACK, stroke_color=BLACK, stroke_width=1).add_tip(ArrowTriangleFilledTip(fill_color=BLACK, stroke_color=BLACK).scale(0.3))

        square1 = Rectangle(color=BLUE, height=1.8, width=0.2, fill_opacity=0.3).next_to(arr, RIGHT).shift(LEFT * 0.1)
        ellip1 = Tex("...", color=BLACK).scale(0.7).next_to(square1, RIGHT, buff=SMALL_BUFF)
        square2 = Rectangle(color=GOLD, height=1.6, width=0.2, fill_opacity=0.3).next_to(ellip1, RIGHT, buff=SMALL_BUFF)
        ellip2 = Tex("...", color=BLACK).scale(0.7).next_to(square2, RIGHT, buff=SMALL_BUFF)
        square3 = Rectangle(color=BLUE, height=1.4, width=0.2, fill_opacity=0.3).next_to(ellip2, RIGHT, buff=SMALL_BUFF)
        self.add(latent, s, odot, max_plane, s_pert, encompassing, square1, square2, ellip1, ellip2, arr, square3)

        enc_edge = square2.get_edge_center(DOWN) + DOWN * 0.15
        line1 = Line(enc_edge, enc_edge + DOWN * 0.5, fill_color=BLACK, stroke_color=BLACK, stroke_width=1)
        line2 = Line(enc_edge + DOWN * 0.5, enc_edge + DOWN * 0.5 + RIGHT * 0.5, fill_color=BLACK, stroke_color=BLACK, stroke_width=1).add_tip(ArrowTriangleFilledTip(fill_color=BLACK, stroke_color=BLACK).scale(0.3))
        arr = Group(line1, line2)
        probe = Tex("Probe", fill_color=BLACK).scale(0.55)
        probe = Group(probe, SurroundingRectangle(probe, color=BLACK, stroke_width=1)).next_to(line2, RIGHT, buff=SMALL_BUFF)
        self.add(arr, probe)