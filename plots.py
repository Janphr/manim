from manimlib.imports import *


class GraphPosition(GraphScene):
    CONFIG = {
        "y_axis_label": r"Distance $10^7[m]$",
        "x_axis_label": r"Time $10^4[s]$",
        "x_min": 0,
        "x_max": 8,
        "x_axis_width": 10,
        "num_graph_anchor_points": 100,
        "y_min": -7,
        "y_max": 1,
        "y_axis_height": 1.25,
        "axes_color": GREEN,
        "x_labeled_nums": range(0, 9, 1),
        "y_labeled_nums": [-6,-4,-2,0],
        "exclude_zero_label": False
    }

    def construct(self):
        h1 = 3
        h2 = 2.55
        self.graph_origin = (-4.8, h1, 0)
        self.setup_axes(animate=True)
        g1 = self.get_graph(lambda x:0,color = GREEN)
        t1 = TexMobject("x").shift((-6.5, h2, 0))
        self.play(Write(t1), ShowCreation(g1))


        self.y_axis_label = r"Distance $10^6[m]$"
        self.graph_origin = (-4.8, h1-2.5, 0)
        self.y_labeled_nums = [-15,-10,-5,0]
        self.y_min = -16
        self.y_max = 1
        self.setup_axes(animate=True)
        g1 = self.get_graph(lambda x:0,color = GREEN)
        t1 = TexMobject("y").shift((-6.5, h2-2.5, 0))
        self.play(Write(t1), ShowCreation(g1))


        self.y_axis_label = r"Distance $10^6[m]$"
        self.graph_origin = (-4.8, h1-5.3, 0)
        self.y_labeled_nums = [-10,-5,0,5]
        self.x_labeled_nums = range(1, 9, 1)
        self.y_min = -10
        self.y_max = 7
        self.setup_axes(animate=True)
        g1 = self.get_graph(lambda x:0,color = GREEN)
        t1 = TexMobject("z").shift((-6.5, h2-5, 0))
        self.play(Write(t1), ShowCreation(g1))
        self.wait()


class GraphVelocity(GraphScene):
    CONFIG = {
        "y_axis_label": r"Velocity $10^3[m/s]$",
        "x_axis_label": r"Time $10^4[s]$",
        "x_min": 0,
        "x_max": 8,
        "x_axis_width": 10,
        "num_graph_anchor_points": 100,
        "y_min": -1,
        "y_max": 4,
        "y_axis_height": 1.25,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(1, 9, 1),
        "y_labeled_nums": [0,2,4],
        "exclude_zero_label": False
    }

    def construct(self):
        h1 = 2.15
        h2 = 2.55
        self.graph_origin = (-4.8, h1-.1, 0)
        self.setup_axes(animate=True)
        g1 = self.get_graph(lambda x:0,color = GREEN)
        t1 = TexMobject("\\dot{x}").shift((-6.5, h2, 0))
        self.play(Write(t1), ShowCreation(g1))


        self.y_axis_label = r"Velocity $10^3[m/s]$"
        self.graph_origin = (-4.8, h1-2.5, 0)
        self.y_labeled_nums = [0,1,2]
        self.y_min = -.25
        self.y_max = 2
        self.setup_axes(animate=True)
        g1 = self.get_graph(lambda x:0,color = GREEN)
        t1 = TexMobject("\dot{y}").shift((-6.5, h2-2.5, 0))
        self.play(Write(t1), ShowCreation(g1))


        self.y_axis_label = r"Velocity $10^3[m/s]$"
        self.graph_origin = (-4.8, h1-4.1, 0)
        self.y_labeled_nums = [-2,-1,0]
        self.x_labeled_nums = range(0, 9, 1)
        self.y_min = -2
        self.y_max = .25
        self.setup_axes(animate=True)
        g1 = self.get_graph(lambda x:0,color = GREEN)
        t1 = TexMobject("\dot{z}").shift((-6.5, h2-5, 0))
        self.play(Write(t1), ShowCreation(g1))
        self.wait()

class GraphControl(GraphScene):
    CONFIG = {
        "y_axis_label": r"Force $[N]$",
        "x_axis_label": r"Time $10^4[s]$",
        "graph_origin": (-4.8, 2.7, 0),
        "x_min": 0,
        "x_max": 8,
        "x_axis_width": 10,
        "num_graph_anchor_points": 100,
        "y_min": -100,
        "y_max": 100,
        "y_axis_height": 1.25,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(1, 9, 1),
        "y_labeled_nums": [-100,0,100],
        "exclude_zero_label": False
    }

    def construct(self):
        h2 = 2.55
        self.setup_axes()
        g1 = self.axes
        t1 = TexMobject("F_1").shift((-6.5, h2, 0))
        self.play(Write(t1), ShowCreation(g1, run_time=2))


        g2 = self.axes.copy()
        g2.shift(2.5*DOWN)
        t2 = TexMobject("F_2").shift((-6.5, h2-2.5, 0))
        self.play(Write(t2), ShowCreation(g2, run_time=2))


        g3 = self.axes.copy()
        g3.shift(5*DOWN)
        t3 = TexMobject("F_3").shift((-6.5, h2-5, 0))
        self.play(Write(t3), ShowCreation(g3, run_time=2))
        self.wait()

class GraphFuel(GraphScene):
    CONFIG = {
        "y_axis_label": r"Mass $[kg]$",
        "x_axis_label": r"Time $10^4[s]$",
        "graph_origin": (-4.8, -2.7, 0),
        "x_min": 0,
        "x_max": 8,
        "num_graph_anchor_points": 100,
        "y_min": 0,
        "y_max": 1000,
        "y_axis_height": 5,
        "axes_color": GREEN,
        "x_labeled_nums": range(0, 9, 1),
        "y_labeled_nums": range(0, 1001, 100),
        "exclude_zero_label": False
    }

    def construct(self):
        self.setup_axes(animate=True, x_axis_num_direction=DOWN,
                        y_axis_label_direction=.5*TOP,
                        y_axis_label_pos=TOP)
        t1 = TexMobject("\\text{Mass of expelled fuel}").shift((0, 3.1, 0))
        self.play(Write(t1))
        self.wait()

