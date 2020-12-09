from manimlib.imports import *


class Table(Scene):
    def construct(self):
        h_size = .75
        nr_size = .7
        t_size = .5

        title = TexMobject("\\text{Planned Formation Scenarios}").shift((0, 3.5, 0)).scale(.75)
        header = TexMobject("\\text{Nr. }", "\\text{Dim. }", "\\text{Formation Scenario }", "\\text{Size [km] }",
                            "\\text{Maneuver Type }", "\\text{Controller }", "\\text{Duration [d] }") \
            .scale(h_size).shift((0, 2.5, 0))
        nr = TexMobject("1.", "2.", "3.", "4.", "5.", "6.", "7.", "8.", "9.", "10.", "11.", "12.", "13.", "14.", "15.") \
            .arrange(DOWN).scale(nr_size).move_to(header[0], DOWN).shift(6.2 * DOWN)

        v = []
        for i in range(6):
            v.append(Line(header[i].get_corner(TOP + RIGHT) + .1 * RIGHT,
                          header[i].get_corner(DOWN + RIGHT) + 6.2 * DOWN + .1 * RIGHT, stroke_width=.5, color=GREEN))

        h_shift = (-.2, .08, 0)
        h = []
        for i in range(15):
            if i >= 9:
                h.append(Line(nr[i].get_corner(TOP), nr[i].get_corner(TOP + RIGHT) + 12.9 * RIGHT, stroke_width=.5,
                              color=GREEN)
                         .shift(h_shift))
            else:
                h.append(Line(nr[i].get_corner(TOP), nr[i].get_corner(TOP + RIGHT) + 13 * RIGHT, stroke_width=.5,
                              color=GREEN)
                         .shift(h_shift))
        text = [
            TexMobject("\\text{/}", "\\text{Initial uncontrolled drifting}", "\\text{/}", "\\text{Drift}", "\\text{/}",
                       "\\text{30}").set_color(BLUE_B).scale(t_size),
            TexMobject("\\text{/}", "\\text{Initial drift compensation}", "\\text{/}", "\\text{Drift compensation}",
                       "\\delta a", "\\text{10}").set_color(BLUE_B).scale(t_size),
            TexMobject("\\text{/}", "\\text{Orbit assimilation}", "\\text{/}", "\\text{Drift compensation}", "MPC",
                       "\\text{20}").set_color(BLUE_B).scale(t_size),
            TexMobject("\\text{1D}", "\\text{ATF}", "\\text{10}", "\\text{Acquisition}", "MPC",
                       "\\text{20}").set_color(GREEN_B).scale(t_size),
            TexMobject("\\text{1D}", "\\text{ATF}", "\\text{10}", "\\text{Maintenance}", "MPC",
                       "\\text{14}").set_color(GREEN_B).scale(t_size),
            TexMobject("\\text{2D}", "\\text{CWF 3:1 in plane}", "\\text{3}", "\\text{Acquisition}", "MPC",
                       "\\text{10}").set_color(YELLOW_B).scale(t_size),
            TexMobject("\\text{2D}", "\\text{CWF 3:1 in plane}", "\\text{3}", "\\text{Maintenance}", "MPC",
                       "\\text{14}").set_color(YELLOW_B).scale(t_size),
            TexMobject("\\text{3D}", "\\text{CWF 3:1 out of plane}", "\\text{3}", "\\text{Acquisition}", "MPC",
                       "\\text{4}").set_color(YELLOW_B).scale(t_size),
            TexMobject("\\text{3D}", "\\text{CWF 3:1 out of plane}", "\\text{3}", "\\text{Maintenance}", "MPC",
                       "\\text{28}").set_color(YELLOW_B).scale(t_size),
            TexMobject("\\text{1D}", "\\text{ATF}", "\\text{10}", "\\text{Acquisition}", "MPC",
                       "\\text{10}").set_color(GOLD_B).scale(t_size),
            TexMobject("\\text{1D}", "\\text{ATF}", "\\text{10}", "\\text{Maintenance}", "MPC",
                       "\\text{14}").set_color(GOLD_B).scale(t_size),
            TexMobject("\\text{3D}", "\\text{Tetrahedron formation}", "\\text{3}", "\\text{Acquisition}", "MPC",
                       "\\text{14}").set_color(RED_B).scale(t_size),
            TexMobject("\\text{3D}", "\\text{Tetrahedron formation}", "\\text{3}", "\\text{Maintenance}", "MPC",
                       "\\text{14}").set_color(RED_B).scale(t_size),
            TexMobject("\\text{1D}", "\\text{ATF}", "\\text{10}", "\\text{Acquisition}", "MPC",
                       "\\text{14}").set_color(PURPLE_B).scale(t_size),
            TexMobject("\\text{1D}", "\\text{ATF}", "\\text{10}", "\\text{Maintenance}", "MPC",
                       "\\text{14}").set_color(PURPLE_B).scale(t_size)]

        self.play(Write(title), Write(header, run_time=3), ShowCreation(VGroup(*v), run_time=3))
        self.play(Write(nr, run_time=3), ShowCreation(VGroup(*h), run_time=3))
        self.wait()

        for i in range(15):
            for j in range(6):
                text[i][j].next_to(v[j], RIGHT).align_to(h[i], DOWN).shift((0, -.35, 0))

            self.play(Write(text[i]))
            self.wait()


class Table1(Scene):
    def construct(self):
        h_size = .75
        t_size = .7

        shift_down = 3.5*DOWN

        header = TexMobject("\\text{Orbit parameter\\quad\\quad\\quad}", "\\text{Symbol\\quad}", "\\text{Target\\quad}",
                            "\\text{Chaser\\quad}", "\\text{Unit}").scale(h_size).shift((0, 2.5, 0))
        parameters = TexMobject("\\text{Semi-major axis}", "\\text{Eccentricity}", "\\text{Inclination}",
                                "\\text{Longitude of ascending node}", "\\text{Argument of periapsis}",
                                "\\text{Mean anomaly}").scale(t_size).arrange(DOWN).move_to(header[0], DOWN).shift(shift_down)
        symbols = TexMobject("a", "e", "i", "\\Omega", "\\omega", "M_0")\
            .scale(t_size).arrange(DOWN).move_to(header[1], DOWN).shift(shift_down)
        target = TexMobject("50000", "0.8", "260", "60", "120", "80")\
            .scale(t_size).arrange(DOWN).move_to(header[2], DOWN).shift(shift_down)
        chaser = TexMobject("35000", "0.5", "270", "30", "160", "15")\
            .scale(t_size).arrange(DOWN).move_to(header[3], DOWN).shift(shift_down)
        units = TexMobject("\\text{km}", "\\text{/}", "\\text{°}", "\\text{°}", "\\text{°}", "\\text{°}")\
            .scale(t_size).arrange(DOWN).move_to(header[4], DOWN).shift(shift_down)

        for i in range(6):
            symbols[i].align_to(parameters[i],TOP)
            target[i].align_to(parameters[i], TOP)
            chaser[i].align_to(parameters[i], TOP)
            units[i].align_to(parameters[i], TOP)

        l1 = Line((-4.5, 2.1, 0), (4.5, 2.1, 0))

        self.play(Write(header), ShowCreation(l1))
        self.play(Write(parameters))
        self.play(Write(symbols))
        self.play(Write(target))
        self.play(Write(chaser))
        self.play(Write(units))
        self.wait()

class Table2(Scene):
    def construct(self):
        h_size = .75
        t_size = .7

        shift_down = 1.8*DOWN

        header = TexMobject("\\text{Chaser satellite property\\quad}", "\\text{Symbol\\quad}", "\\text{Value\\quad}",
                            "\\text{Unit}").scale(h_size).shift((0, 2.5, 0))
        parameters = TexMobject("\\text{Dry mass}", "\\text{Fuel mass}", "\\text{Specific impulse}")\
            .scale(t_size).arrange(DOWN).move_to(header[0], DOWN).shift(shift_down)
        symbols = TexMobject("m_{dry}", "m_{f_0}", "I_{sp}")\
            .scale(t_size).arrange(DOWN).move_to(header[1], DOWN).shift(shift_down)
        values = TexMobject("100", "900", "450")\
            .scale(t_size).arrange(DOWN).move_to(header[2], DOWN).shift(shift_down)
        units = TexMobject("kg", "kg", "s")\
            .scale(t_size).arrange(DOWN).move_to(header[3], DOWN).shift(shift_down)

        for i in range(3):
            symbols[i].align_to(parameters[i],TOP)
            values[i].align_to(parameters[i], TOP)
            units[i].align_to(parameters[i], TOP)

        l1 = Line((-4, 2.1, 0), (4, 2.1, 0))

        self.play(Write(header), ShowCreation(l1))
        self.play(Write(parameters))
        self.play(Write(symbols))
        self.play(Write(values))
        self.play(Write(units))
        self.wait()

class Table3(Scene):
    def construct(self):
        h_size = .75
        t_size = .7

        shift_down = 2.3*DOWN

        header = TexMobject("\\text{MPC parameter\\quad\\quad", "\\text{Symbol\\quad}", "\\text{Value\\quad}", "\\text{Unit}")\
            .scale(h_size).shift((0, 2.5, 0))
        parameters = TexMobject("\\text{Prediction horizon}", "\\text{Control constraint}", "\\text{Control weight}",
                                "\\text{Time step size}").scale(t_size).arrange(DOWN).move_to(header[0], DOWN).shift(shift_down)
        symbols = TexMobject("p", "F_{min}^{max}", "w", "T_s")\
            .scale(t_size).arrange(DOWN).move_to(header[1], DOWN).shift(shift_down)
        values = TexMobject("70", "\\pm 100", "15\\times 10^{10}", "300")\
            .scale(t_size).arrange(DOWN).move_to(header[2], DOWN).shift(shift_down)
        units = TexMobject("\\text{/}", "N", "\\text{/}", "s")\
            .scale(t_size).arrange(DOWN).move_to(header[3], DOWN).shift(shift_down)

        for i in range(4):
            values[i].align_to(parameters[i], TOP)
            symbols[i].align_to(parameters[i], TOP)
            units[i].align_to(parameters[i], TOP)

        symbols[2].shift((0,-.1,0))

        l1 = Line((-3.7, 2.1, 0), (3.7, 2.1, 0))

        self.play(Write(header), ShowCreation(l1))
        self.play(Write(parameters))
        self.play(Write(symbols))
        self.play(Write(values))
        self.play(Write(units))
        self.wait()