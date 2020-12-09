from manimlib.imports import *


class CostFunction(Scene):
    def construct(self):
        t1 = TexMobject("\\text{Quadratic Cost Function}").shift((0, 3.5, 0)).scale(0.75)
        e = TexMobject("J(z_k) = \\sum_{j=1}^n\\sum_{i=0}^{p-1}\\Big\\{ w_{i,j}[x_j(k+i|k)-x_{j, target}(k+i|k)]\\Big\\}^2")
        self.play(Write(VGroup(t1, e)))
        self.wait()


class Xyz(Scene):
    def construct(self):
        t1 = TexMobject("\\text{Closed Form Solution}").shift((0, 3.5, 0)).scale(0.75)
        e1 = TexMobject("x(t)", "=", "(\\frac{4\\dot{x_0}}{\\omega})\\sin{\\omega t} -"
                                         "\\frac{2\\dot{z_0}}{\\omega}\\cos{\\omega t} +"
                                         "(6\\omega z_0 - e\\dot{x_0})t",
                        "+ (x_0 + \\frac{2\\dot{z_0}}{\\omega})",
                        "+ u_z\\frac{2}{\\omega^2}(\\omega t - \\sin{\\omega t}) +"
                        "u_x(\\frac{4}{\\omega^2}(1 - \\cos{\\omega t}) - \\frac{3}{2}t^2)").move_to(t1, DOWN).shift(
            (0, -2.5, 0)).set_color(
            RED).scale(0.5)
        e2 = TexMobject("y(t)", "=", "y_0\\cos{\\omega t} + \\frac{\\dot{y_0}}{\\omega}\\sin{\\omega t}",
                        "+ u_y\\frac{1}{\\omega^2}(1 - \\cos{\\omega t})").move_to(e1).shift((0, -.8, 0)).set_color(
            GREEN).scale(
            0.5)
        e3 = TexMobject("z(t)", "=", "(\\frac{2\\dot{x_0}}{\\omega} - 3z_0)\\cos{\\omega t} + "
                                     "\\dot{z_0}\\frac{1}{\\omega}\\sin{\\omega t}",
                        "+ (4z_0 - \\frac{2\\dot{x_0}}{\\omega})",
                        "+u_x\\frac{2}{\\omega^2}(\\sin{\\omega t} - \\omega t) + u_z\\frac{1}{\\omega^2}(1-\\cos{\\omega t})").move_to(
            e1).shift(
            (0, -1.6, 0)).set_color(BLUE).scale(0.5)

        eq1 = e1[1]
        eq2 = e2[1].align_to(eq1, LEFT)
        eq3 = e3[1].align_to(eq2, LEFT)

        e1[0].next_to(eq1, LEFT)
        e1[2].next_to(eq1, RIGHT)
        e1[3].next_to(e1[2], RIGHT)
        e1[4].next_to(e1[3], RIGHT)
        e2[0].next_to(eq2, LEFT)
        e2[2].next_to(eq2, RIGHT)
        e2[3].next_to(e2[2], RIGHT)
        e3[0].next_to(eq3, LEFT)
        e3[2].next_to(eq3, RIGHT)
        e3[3].next_to(e3[2], RIGHT)
        e3[4].next_to(e3[3], RIGHT)

        e = VGroup(e1,e2,e3)
        u = VGroup(e1[4], e2[3], e3[4])
        t = VGroup(e1[3],e3[3])

        c = TexMobject("\\vec{u} = \\vec{0}").shift((0,-2.5,0)).scale(1.25)
        c2 = TexMobject("x_0 = -\\frac{2\\dot{z_0}}{\\omega}", "\\text{, }", "\\dot{x_0} = 2\\omega z_0").shift((0, -2.5, 0)).scale(1.25)

        self.play(Write(t1))
        self.play(Write(e1))
        self.wait()
        self.play(Write(e2))
        self.wait()
        self.play(Write(e3))
        self.wait()
        self.play(u.set_color, YELLOW,
                  u.scale, 1.05,
                  Write(c))
        self.wait()
        self.play(ApplyMethod(u.scale, 0.01), FadeOut(c))
        self.play(FadeOut(u))
        self.wait()
        self.play(e.scale, 1.5,
                  e.move_to, .8*RIGHT)
        self.wait()
        self.play(t.set_color, YELLOW,
                  t.scale, 1.05,
                  Write(c2))
        self.wait()
        self.play(ApplyMethod(t.scale, 0.01), FadeOut(c2))
        self.play(FadeOut(t))
        self.wait()



class CWG(Scene):
    def construct(self):
        t = TexMobject("\\text{Clohessy-Wiltshire equations:}").shift((4, 3, 0)).scale(0.75)
        e1 = TexMobject("\\ddot{x}", "=", "3\\omega^2x + 2\\omega\\dot{y} + u_x").move_to(t, LEFT).shift(
            (0, -1, 0)).set_color(RED).scale(0.75)
        e2 = TexMobject("\\ddot{y}", "=", "-2\\omega\\dot{x} + u_y").move_to(e1).shift((0, -.9, 0)).set_color(
            GREEN).scale(0.75)
        e3 = TexMobject("\\ddot{z}", "=", "-\\omega^2z + u_z").move_to(e1).shift((0, -1.6, 0)).set_color(BLUE).scale(
            0.75)
        n = TextMobject("with: ", "$u = \\frac{F}{m}$, $\\omega = \\sqrt{\\frac{\\mu}{a^3}}$").scale(0.75).align_to(t,
                                                                                                                    LEFT).shift(
            (0, -1, 0))

        eq1 = e1[1]
        eq2 = e2[1].align_to(eq1, LEFT)
        eq3 = e3[1].align_to(eq2, LEFT)

        e1[0].next_to(eq1, LEFT)
        e1[2].next_to(eq1, RIGHT)
        e2[0].next_to(eq2, LEFT)
        e2[2].next_to(eq2, RIGHT)
        e3[0].next_to(eq3, LEFT)
        e3[2].next_to(eq3, RIGHT)

        t1 = TexMobject("\\text{CW in transformed LVLH frame:}").shift((-4, 3, 0)).scale(0.75)
        e11 = TexMobject("\\ddot{x}", "=", "2\\omega\\dot{z} + u_x").move_to(t1, LEFT).shift((0, -1, 0)).set_color(
            RED).scale(0.75)
        e12 = TexMobject("\\ddot{y}", "=", "- \\omega^2y + u_y").move_to(e11).shift((0, -.8, 0)).set_color(GREEN).scale(
            0.75)
        e13 = TexMobject("\\ddot{z}", "=", "3\\omega^2z - 2\\omega\\dot{x} + u_z").move_to(e11).shift(
            (0, -1.6, 0)).set_color(BLUE).scale(0.75)

        eq11 = e11[1]
        eq12 = e12[1].align_to(eq11, LEFT)
        eq13 = e13[1].align_to(eq12, LEFT)

        e11[0].next_to(eq11, LEFT)
        e11[2].next_to(eq11, RIGHT)
        e12[0].next_to(eq12, LEFT)
        e12[2].next_to(eq12, RIGHT)
        e13[0].next_to(eq13, LEFT)
        e13[2].next_to(eq13, RIGHT)

        t2 = TexMobject("\\text{State equations:}").shift((3, 3, 0)).scale(0.75)
        e21 = TexMobject("\\dot{x_1}", "=", "x_4").move_to(t2, LEFT).shift((0, -1, 0)).scale(0.75)
        e22 = TexMobject("\\dot{x_2}", "=", "x_5").move_to(e21).shift((0, -.8, 0)).scale(0.75)
        e23 = TexMobject("\\dot{x_3}", "=", "x_6").move_to(e21).shift((0, -1.6, 0)).scale(0.75)
        e24 = TexMobject("\\dot{x_4}", "=", "\\ddot{x_1} = 2\\omega\\dot{x_3} + u_1").move_to(e21, LEFT).shift(
            (0, -2.4, 0)).set_color(RED).scale(0.75)
        e25 = TexMobject("\\dot{x_5}", "=", "\\ddot{x_2} = - \\omega^2x_2 + u_2").move_to(e21).shift(
            (0, -3.2, 0)).set_color(GREEN).scale(0.75)
        e26 = TexMobject("\\dot{x_6}", "=", "\\ddot{x_3} = 3\\omega^2x_3 - 2\\omega\\dot{x_1} + u_3").move_to(
            e21).shift((0, -4, 0)).set_color(BLUE).scale(0.75)

        eq21 = e21[1]
        eq22 = e22[1].align_to(eq21, LEFT)
        eq23 = e23[1].align_to(eq22, LEFT)
        eq24 = e24[1].align_to(eq23, LEFT)
        eq25 = e25[1].align_to(eq24, LEFT)
        eq26 = e26[1].align_to(eq25, LEFT)

        e21[0].next_to(eq21, LEFT)
        e21[2].next_to(eq21, RIGHT)
        e22[0].next_to(eq22, LEFT)
        e22[2].next_to(eq22, RIGHT)
        e23[0].next_to(eq23, LEFT)
        e23[2].next_to(eq23, RIGHT)
        e24[0].next_to(eq24, LEFT)
        e24[2].next_to(eq24, RIGHT)
        e25[0].next_to(eq25, LEFT)
        e25[2].next_to(eq25, RIGHT)
        e26[0].next_to(eq26, LEFT)
        e26[2].next_to(eq26, RIGHT)

        m1 = Matrix(["\\dot{x_1}", "\\dot{x_2}", "\\dot{x_3}", "\\dot{x_4}", "\\dot{x_5}", "\\dot{x_6}", ]) \
            .stretch_to_fit_width(1).scale(.75).shift(6.25 * LEFT)
        eqals = TexMobject("=").scale(.75).next_to(m1, RIGHT)
        m2 = Matrix([
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, "2\\omega"],
            [0, "-\\omega^2", 0, 0, 0, 0],
            [0, 0, "3\\omega^2", "-2\\omega", 0, 0],
        ]).stretch_to_fit_width(6).scale(.75).next_to(eqals, RIGHT)
        m3 = Matrix(["x_1", "x_2", "x_3", "x_4", "x_5", "x_6", ]) \
            .stretch_to_fit_width(1).scale(.75).next_to(m2, RIGHT)
        plus = TexMobject("+").scale(.75).next_to(m3, RIGHT)
        m4 = Matrix([
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
        ]).stretch_to_fit_width(6).scale(.75).next_to(plus, RIGHT)
        m5 = Matrix([0, 0, 0, "u_1", "u_2", "u_3", ]) \
            .stretch_to_fit_width(1).scale(.75).next_to(m4, RIGHT)

        e31 = TextMobject("$\\dot{x}_{(t)}$", "A", "$x_{(t)}$", "B", "$u_{(t)}$")
        e31[0].next_to(m1, DOWN)
        e31[1].next_to(m2, DOWN)
        e31[2].next_to(m3, DOWN)
        e31[3].next_to(m4, DOWN)
        e31[4].next_to(m5, DOWN)


        self.play(Write(t))
        self.play(Write(e1))
        self.play(Write(e2))
        self.play(Write(e3))
        self.play(Write(n))
        self.wait()
        self.play(Write(t1))
        self.play(TransformFromCopy(e2, e11))
        self.wait()
        self.play(TransformFromCopy(e3, e12))
        self.wait()
        self.play(TransformFromCopy(e1, e13))
        self.wait()
        self.play(FadeOut(VGroup(t, e1, e2, e3, n)))
        self.wait()
        self.play(Write(VGroup(t2, e21, e22, e23, e24, e25, e26)))
        self.wait()
        self.play(FadeOut(VGroup(t1, e11, e12, e13)),
                  Transform(VGroup(t2, e21, e22, e23, e24, e25, e26), m1))
        self.play(Write(VGroup(eqals, m2, m3, plus, m4, m5)))
        self.wait()
        self.play(Write(e31))
        self.wait()


        e41 = TextMobject("$\\chi_{(t)} = e^{At} X_{(0)} = $").scale(.75)
        m21 = TexMobject(
            r"\begin{bmatrix} 1 & 0 & 6(\omega t - \sin{\omega t}) & \frac{4\sin{\omega t}}{\omega}-3t & 0 &\frac{2}{\omega}(1 - \cos{\omega t})\\"
            r"0 & \cos{\omega t} & 0 & 0 & \frac{\sin{\omega t}}{\omega} & 0\\"
            r"0 & 0 & 4 - 3\cos{\omega t} & -\frac{2}{\omega}(1 + \cos{\omega t}) & 0 & \frac{\sin{\omega t}}{\omega}\\"
            r"0 & 0 & 6\omega(1 - \cos{\omega t}) & 4\cos{\omega t} - 3 & 0 & 2\sin{\omega t}\\"
            r"0 & -\omega\sin{\omega t} & 0 & 0 & \cos{\omega t} & 0\\"
            r"0 & 0 & 3\omega\sin{\omega t} & -2\sin{\omega t} & 0 & \cos{\omega t}\end{bmatrix}").scale(.75)
        m22 = Matrix(["x_0", "y_0", "z_0", "\\dot{x_0}", "\\dot{y_0}", "\\dot{z_0}", ]) \
            .scale(.75)

        self.play(FadeOut(VGroup(t2, e21, e22, e23, e24, e25, e26)), FadeOut(VGroup(eqals, m2, m3, plus, m4, m5, e31)), Write(VGroup(e41, VGroup(m21, m22).arrange()).arrange(DOWN)))
        self.wait()
