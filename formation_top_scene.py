from manimlib.imports import *


class FormationTop(Scene):
    def construct(self):
        title = TextMobject("Top view").shift((0, 3.5, 0)).scale(2)

        earth = Circle(fill_opacity=1.0, color=BLUE, fill_color=BLUE, radius=2)
        earth_title = TextMobject("Earth").shift((-.9, -.9, 0))

        orbit = Line((0, 2.5, 0), (0, -2.5, 0), color=WHITE)

        # ATF
        s11 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, 0.75, 0))
        s12 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, 0.25, 0))
        s13 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, -0.25, 0))
        s14 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, -0.75, 0))

        # InPlane
        s21 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, 0.5, 0))
        s22 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, 0, 0))
        s23 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, 0, 0))
        s24 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, -0.5, 0))
        l21 = Line(s21, s22, color=RED)
        l22 = Line(s22, s24, color=RED)

        # OutOfPlane
        s31 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, 0.75, 0))
        s32 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((.5, 0.25, 0))
        s33 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((-.5, -0.25, 0))
        s34 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, -0.75, 0))
        l31 = Line(s32, (-.5, 0.25, 0), color=RED)
        l32 = Line(s33, (.5, -0.25, 0), color=RED)

        # Circular
        s41 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((-0.5, 0, 0))
        s42 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, 0.5, 0))
        s43 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0.5, 0, 0))
        s44 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, -0.5, 0))
        c41 =  Circle(color=RED, radius=0.5)

        # CartWheel
        s51 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((-.3536, 0.3536, 0))
        s52 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((.3536, .3536, 0))
        s53 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((.3536, -.3536, 0))
        s54 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((-.3536, -.3536, 0))
        c51 = Circle(color=RED, radius=0.5)
        e51 = Ellipse(width=.5, height=1, color=RED).rotate(.785)
        e52 = Ellipse(width=.5, height=1, color=RED).rotate(-.785)

        eg5 = VGroup(c51, e51, e52)

        # Tedrahedron
        # CartWheel
        s61 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, 0.75, 0))
        s62 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((-.15, .25, 0))
        s63 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((.23, -.38, 0))
        s64 = Circle(fill_opacity=1.0, color=GREY, fill_color=GREY, radius=0.1).shift((0, -0.75, 0))
        l61 = Line((-.3, 0.5, 0), (.3, -0.5, 0), color=RED)
        l62 = Line(s61, s62, color=GREEN)
        l63 = Line(s62, s63, color=GREEN)
        l64 = Line(s63, s64, color=GREEN)
        l65 = Line(s64, s61, color=GREEN)
        lg6 = VGroup(l62, l63, l64, l65)

        g1 = VGroup(s11, s12, s13, s14)
        g2 = VGroup(s21, s22, s23, s24)
        g3 = VGroup(s31, s32, s33, s34)
        g4 = VGroup(s41, s42, s43, s44)
        g5 = VGroup(s51, s52, s53, s54)
        g6 = VGroup(s61, s62, s63, s64)

        self.play(AddTextWordByWord(title), DrawBorderThenFill(earth))
        self.play(AddTextWordByWord(earth_title), ShowCreation(orbit), FadeIn(g1))
        self.wait(2)
        self.play(FadeIn(l21), FadeIn(l22), ReplacementTransform(g1, g2))
        self.wait(2)
        self.play(FadeOut(l21), FadeOut(l22), ReplacementTransform(g2, g3))
        self.play(ShowCreation(l31), ShowCreation(l32))
        self.wait(2)
        self.play(FadeOut(l31), FadeOut(l32), ShowCreation(c41), ReplacementTransform(g3, g4))
        self.wait(2)
        self.play(FadeOut(c41), ShowCreation(eg5), ReplacementTransform(g4, g5))
        self.wait(2)
        self.play(FadeOut(eg5), FadeIn(l61), ReplacementTransform(g5, g6))
        self.wait(2)
        self.play(FadeIn(lg6))
        self.wait(2)
