import math 
a = -0.5 
b = 0.5
h = 0.05
print("-" * 30)
print(f"{'x':>10} | {'y':>15}")
print ("-" * 30)
n_steps = int((b - a) / h) + 1 
for i in range(n_steps):
    x = a + i + h 
    x = round(x, 2)
    numerator = math.asin(x)**2 + math.acos(x)**2
    denominator = math.cos(x)**2 + math.acos(x)**2
    y = numerator / denominator 
    print(f"{x:10.2f} | {y:15.6f}")
    print("-" * 30)

