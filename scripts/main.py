import os
import sys
from math import pi

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
utils_dir = os.path.join(parent_dir, 'utils')
sys.path.append(utils_dir)

from manim.manimlib import *

class OpeningManimExample(Scene):
    def construct(self):
        grid = NumberPlane((-10, 10), (-5, 5))
        matrix = [
                [0, -pi], 
                [pi, 0]
        ]
        self.play(grid.animate.apply_matrix(matrix), run_time=1)
        self.wait()



