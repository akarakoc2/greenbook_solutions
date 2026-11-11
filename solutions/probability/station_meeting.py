import pandas as pd 
import numpy as np


n = 1_000_000
rng = np.random.default_rng(42)

#Generating independent arrival time for the bankers (minutes after 5 am)
banker_a = np.random.uniform(0, 60, n)
banker_b = np.random.uniform(0, 60, n)

# They meet if arrival times differ by at most 5 minutes

meet = np.abs(banker_a - banker_b) <= 5

#estimating the probability

p_mc = np.mean(meet) # eg. 1 0 1 0 - > 2 / 4 .. 

p_exact = 1 - (55 / 60)**2 

print(f"Monte Carlo: {p_mc:.5f}")
print(f"Exact:       {p_exact:.5f}")
print(f"Error:       {abs(p_mc - p_exact):.5f}")


print(meet)