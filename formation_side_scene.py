from manimlib.imports import *


class FormationSide(Scene):
    def construct(self):
        title = TextMobject("Side view").shift((0, 3.5, 0)).scale(2)

        earth = Circle(fill_opacity=1.0, color=BLUE, fill_color=BLUE, radius=2)
        earth_title = TextMobject("Earth").shift((-.9, -.9, 0))

        orbit = Circle(color=WHITE, radius=2.5)

        # ATF
        s11 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.4, 0.75, 0))
        s12 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.5, 0.25, 0))
        s13 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.5, -0.25, 0))
        s14 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.4, -0.75, 0))

        # InPlane
        s21 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.5, 0, 0))
        s22 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.2, 0, 0))
        s23 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.65, -0.25, 0))
        s24 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.65, 0.25, 0))
        c2 = Circle(color=RED, radius=0.3).move_to(s21)

        # OutOfPlane
        s31 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.4, 0.75, 0))
        s32 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.5, 0.25, 0))
        s33 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.5, -0.25, 0))
        s34 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.4, -0.75, 0))

        # Circular
        s41 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.47, 0.5, 0))
        s42 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.5, 0, 0))
        s43 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.5, 0, 0))
        s44 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.47, -0.5, 0))
        l41 = Line(s41, s42, color=RED)
        l42 = Line(s42, s44, color=RED)

        # CartWheel
        s51 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.47, 0.5, 0))
        s52 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.23, 0, 0))
        s53 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.73, 0, 0))
        s54 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.47, -0.5, 0))
        e51 = Ellipse(width=.5, height=1, color=RED).shift((2.47, 0, 0))
        e52 = Ellipse(width=.25, height=.5, color=RED).shift((2.47, 0.25, 0))
        e53 = Ellipse(width=.25, height=.5, color=RED).shift((2.47, -0.25, 0))

        eg5 = VGroup(e51, e52, e53)

        # Tedrahedron
        # CartWheel
        s61 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.4, 0.75, 0))
        s62 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.77, .25, 0))
        s63 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.67, -.4, 0))
        s64 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((2.4, -0.75, 0))
        e61 = Ellipse(width=.7, height=1, color=RED).shift((2.47, 0, 0))
        l61 = Line(s61, s62, color=GREEN)
        l62 = Line(s62, s63, color=GREEN)
        l63 = Line(s63, s64, color=GREEN)
        l64 = Line(s64, s61, color=GREEN)

        lg6 = VGroup(l61, l62, l63, l64)

        g1 = VGroup(s11, s12, s13, s14)
        g2 = VGroup(s21, s22, s23, s24)
        g3 = VGroup(s31, s32, s33, s34)
        g4 = VGroup(s41, s42, s43, s44)
        g5 = VGroup(s51, s52, s53, s54)
        g6 = VGroup(s61, s62, s63, s64)

        self.play(AddTextWordByWord(title), DrawBorderThenFill(earth))
        self.play(AddTextWordByWord(earth_title), ShowCreation(orbit), FadeIn(g1))
        self.wait(2)
        self.play(ShowCreation(c2), ReplacementTransform(g1, g2))
        self.wait(2)
        self.play(FadeOut(c2), ReplacementTransform(g2, g3))
        self.wait(2)
        self.play(FadeIn(l41), FadeIn(l42), ReplacementTransform(g3, g4))
        self.wait(2)
        self.play(FadeOut(l41), FadeOut(l42), ShowCreation(eg5), ReplacementTransform(g4, g5))
        self.wait(2)
        self.play(FadeOut(eg5), ShowCreation(e61), ReplacementTransform(g5, g6))
        self.wait(2)
        self.play(FadeIn(lg6))
        self.wait(2)
