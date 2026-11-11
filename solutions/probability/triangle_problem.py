import pandas as pd 
import numpy as np

n = 1_000_000

rng = np.random.default_rng(42)

# generating independent cuts inside a 1 unit stick

cut1 = np.random.uniform(0, 1, n)
cut2 = np.random.uniform(0, 1, n)

#build the segment lenghts -> depending which part is the bigger we need to adjust
X = np.where(cut1 < cut2, cut1, cut2)
Y = np.where(cut1 < cut2, cut2 - cut1, cut1 - cut2)
Z = 1 - X -Y

#conditoning that the to make a triangle each part must be smaller than 0.5 
triangle = (X < 0.5) & (Y < 0.5) & (Z < 0.5)

# monte carlo prob
p_mc = np.mean(triangle)

#check if we are getting a right probability 
assert np.isclose(p_mc, 0.25, atol=0.001), \
    f"Monte Carlo estimate {p_mc:.6f} differs too much from 0.25"

