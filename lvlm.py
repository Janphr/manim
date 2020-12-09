from manimlib.imports import *


class LVLM(Scene):
    def construct(self):
        earth = Circle(fill_opacity=1.0, color=BLUE_B, fill_color=BLUE, radius=16).shift((-18, 0, 0))
        orbit = CubicBezier([
            [-7.1, -3, 0],
            [0, -2, 0],
            [5, 0, 0],
            [-2.115, 2, 0],
        ])

        pts = [
            (0, 0, 0),
            (1, 0, 0),
            (.75, .25, 0),
            (-.25, .25, 0),
            (0, 0, 0)
        ]

        mid = Circle(radius=.2, fill_opacity=1.0, fill_color=RED_B, color=RED_E).shift((0, -1.3, 0))
        left = Polygon(*pts, color=GREY).shift((-1.2, -1.5, 0))
        right = Polygon(*pts, color=GREY).shift((.3, -1.4, 0))
        sat = VGroup(left, right)

        y = Arrow((0, -1.3, 0), 3 * DOWN, color=GREEN)
        z = Arrow((0, -1.3, 0), 2 * LEFT + .9 * DOWN, color=BLUE)

        tip_base = (1.65, -.5, 0)

        x = VGroup(ArrowTip(length=.15, start_angle=PI / 4.3, color=RED).shift((1.78, -.33, 0)).stretch_to_fit_width(.2)
                   , Line((-.03, -1.27, 0), tip_base, color=RED, stroke_width=1)
                   , Line((-.02, -1.28, 0), tip_base, color=RED, stroke_width=2)
                   , Line((-.01, -1.29, 0), tip_base, color=RED, stroke_width=2)
                   , Line((0, -1.3, 0), tip_base, color=RED, stroke_width=3)
                   , Line((.01, -1.31, 0), tip_base, color=RED, stroke_width=2)
                   , Line((.02, -1.32, 0), tip_base, color=RED, stroke_width=2)
                   , Line((.03, -1.33, 0), tip_base, color=RED, stroke_width=1))

        tx = TexMobject("\\text{x}").next_to(x[0], DOWN)
        ty = TexMobject("\\text{y}"). next_to(y, RIGHT).shift((0,-.3,0))
        tz = TexMobject("\\text{z}").next_to(z,TOP).shift((-.1,-1,0))



        self.play(FadeIn(earth))
        self.play(ShowCreation(orbit))
        self.play(ShowCreation(right), DrawBorderThenFill(mid), ShowCreation(left))
        self.add_foreground_mobjects(mid, left)
        self.play(FadeIn(VGroup(y, z, x)), Write(VGroup(tx, ty, tz)))
        self.wait()

