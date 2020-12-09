from manimlib.imports import *


class InitStateChaser(Scene):
    def construct(self):
        state = TexMobject("X_{(t_0)}").shift(4*LEFT)
        eqals1 = TexMobject("=").next_to(state, RIGHT)
        m1 = Matrix(["x_0", "y_0", "z_0", "\\dot{x_0}", "\\dot{y_0}", "\\dot{z_0}", ]).next_to(eqals1, RIGHT)
        eqals2 = TexMobject("=").next_to(m1, RIGHT)
        m2 = Matrix(["-6.15\\times 10^7\\quad [m]", "-1.64\\times 10^7\\quad [m]", "6.95\\times 10^6\\quad [m]", "3.49\\times 10^3[m/s]",
                     "0.13\\times 10^3[m/s]", "-1.49\\times 10^3[m/s]", ]).next_to(eqals2, RIGHT)

        self.play(Write(VGroup(state,eqals1,m1, eqals2, m2)))
        self.wait()
