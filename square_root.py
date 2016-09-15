# square_root.py - calculate square roots of a \in \mathbb{R} with successive approximation given by:
# s_{n+1} = (1/2)(s_n + a/s_n)

import math

a = 3

current = 2

iterations = 50

for i in range(iterations):
    current = (1/2)*(current + a/current)
    print("Iteration", i, ":", current)

print("Actual value:", math.sqrt(a))