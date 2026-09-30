import math 
P = 1.0 
for n in range(1, 21): 
    factorial_val = math.gamma(1.45 * n + 2)
    term = ((-1) ** n) * ((2 * n + 1) / factorial_val) * math.cos(n / 2)
    P *= term
print(f" Произведение P = {P} ") 