from manim import * 
import numpy as np
from manim.mobject.geometry.tips import ArrowTriangleFilledTip


class ProbeForAutoencoder(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame.set_width(10)
        self.camera.frame.move_to(RIGHT * 3)
        square1 = Rectangle(color=BLUE, height=2, width=0.2, fill_opacity=0.3)
        square2 = Rectangle(color=BLUE, height=1.5, width=0.2, fill_opacity=0.3).next_to(square1, RIGHT)
        square3 = Rectangle(color=BLUE, height=1, width=0.2, fill_opacity=0.3).next_to(square2, RIGHT)

        latent = Rectangle(color=GOLD, height=0.75, width=0.2, fill_opacity=0.3).next_to(square3, RIGHT)
        s = MathTex("s", color=BLACK).scale(0.75).next_to(latent, DOWN)
        odot = MathTex("\\odot", color=BLACK).scale(0.7).next_to(latent, RIGHT)
        max_plane = Rectangle(color=RED, height=0.75, width=0.2, fill_opacity=0.3).next_to(odot, RIGHT)
        s_pert = MathTex("s^*", color=BLACK).scale(0.75).next_to(max_plane, DOWN).shift(UP * 0.11).shift(LEFT * 0.1)

        encompassing = SurroundingRectangle(Group(latent, odot, max_plane, s, s_pert), color=BLACK, stroke_width=2)

        square4 = Rectangle(color=BLUE, height=1, width=0.2, fill_opacity=0.3).next_to(max_plane, RIGHT)
        square5 = Rectangle(color=BLUE, height=1.5, width=0.2, fill_opacity=0.3).next_to(square4, RIGHT)
        square6 = Rectangle(color=BLUE, height=2, width=0.2, fill_opacity=0.3).next_to(square5, RIGHT)

        self.add(square1, square2, square3, latent, odot, max_plane, square4, square5, square6, encompassing, s, s_pert)


        enc_edge = encompassing.get_edge_center(UP) + UP * 0.15
        arr = Line(enc_edge, enc_edge + UP * 0.75, fill_color=BLACK, stroke_color=BLACK, stroke_width=1).add_tip(ArrowTriangleFilledTip(fill_color=BLACK, stroke_color=BLACK).scale(0.3))
        
        probe = Tex("Probe", fill_color=BLACK).scale(0.55)
        probe_2 = Tex("(MNIST)", fill_color=BLACK).scale(0.35).next_to(probe, DOWN, buff=SMALL_BUFF)
        probe = Group(probe, probe_2)
        probe = Group(probe, SurroundingRectangle(probe, color=BLACK, stroke_width=1)).next_to(arr, UP, buff=SMALL_BUFF)
        self.add(arr, probe)

        container = SurroundingRectangle(Group(square1, square2, square3, square4, square5, square6), color=BLACK, stroke_width=1)
        ae_label = Tex("Autoencoder", fill_color=BLACK).scale(0.5).next_to(container, DOWN)
        self.add(container, ae_label)

        connect_arr = Line(ORIGIN, RIGHT * 0.5, fill_color=BLACK, stroke_color=BLACK, stroke_width=1).add_tip(ArrowTriangleFilledTip(fill_color=BLACK, stroke_color=BLACK).scale(0.3)).next_to(container, RIGHT)

        self.add(connect_arr)

        square7 = Rectangle(color=BLUE, height=2, width=0.2, fill_opacity=0.3).next_to(connect_arr, RIGHT)
        square8 = Rectangle(color=BLUE, height=1, width=0.2, fill_opacity=0.3).next_to(square7, RIGHT)
        square9 = Rectangle(color=GOLD, height=0.5, width=0.2, fill_opacity=0.3).next_to(square8, RIGHT)
        square10 = Rectangle(color=BLUE, height=0.2, width=0.2, fill_opacity=0.3).next_to(square9, RIGHT)

        classifier_container = SurroundingRectangle(Group(square7, square8, square9, square10), color=BLACK, stroke_width=1)
        classifier_label = Tex("Classifier", fill_color=BLACK).scale(0.5).next_to(classifier_container, DOWN)
        
        enc_edge = square9.get_edge_center(UP) + UP * 0.15
        arr = arr.copy().set_x(square9.get_x())
        
        probe = Tex("Probe", fill_color=BLACK).scale(0.55)
        probe_2 = Tex(r"(Fashion \\ MNIST)", fill_color=BLACK).scale(0.35).next_to(probe, DOWN, buff=SMALL_BUFF)
        probe = Group(probe, probe_2)
        probe = Group(probe, SurroundingRectangle(probe, color=BLACK, stroke_width=1)).next_to(arr, UP, buff=SMALL_BUFF)
        self.add(square7, square8, square9, square10, classifier_label, classifier_container, arr, probe)