import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
build_dir = os.path.join(parent_dir, 'build')
sys.path.append(build_dir)

from math import log, e, pi
import numpy as np
from tqdm import tqdm

from cheat.std import *

def pydisplay(matrix: np.ndarray):
    for y in range(matrix.shape[1]):
        for x in range(matrix.shape[0]):
            print(matrix[y, x], end='\t')
        print()

def pymexp(b: float, M: np.ndarray, limit=1e5):
    T = np.eye(M.shape[0])
    S = T.copy()
    for r in tqdm(range(1, int(limit))):
        T = np.dot(T, M) * log(b) / r # T = (ln(r) * M)^r / r!
        S += T
    return S

MATRIX1 = [[2, 0],
    [0, 2]]

MATRIX2 = mzeta(MATRIX1, 1000);

display(MATRIX1)
print()
display(MATRIX2)

