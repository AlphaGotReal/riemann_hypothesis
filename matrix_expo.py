import numpy as np
from tqdm import tqdm
from math import e, pi, log

def mexp(b, M, limit=1e5):
   
    S = np.eye(M.shape[0])
    T = np.eye(M.shape[0])
    for r in range(1, int(limit)):
        T = np.dot(T, M) * log(b) / r
        S += T
    return S

def zeta(s, limit=1e5):
    z = 0
    for r in tqdm(range(1, int(limit))):
        z += (1 / r ** s)
    return z

def mzeta(M, limit=1e5):
    S = np.zeros_like(M)
    for r in tqdm(range(1, int(limit))):
        S += mexp(r, -M)
    return S


