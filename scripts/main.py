import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
utils_dir = os.path.join(parent_dir, 'utils')
sys.path.append(utils_dir)
sys.path.append(current_dir)

from manim.manimlib import *
from matrix_cal import MATRIX1, MATRIX2

class OpeningManimExample(Scene):
    def construct(self):
        grid = NumberPlane((-10, 10), (-10, 10))
        grid.add_coordinate_labels()
        
        self.add(grid)

        self.play(ApplyMatrix(MATRIX1, grid), run_time=3)
        self.play(ApplyMatrix(np.dot(np.linalg.inv(MATRIX1), MATRIX2), grid), run_time=3)
        self.wait()

        
