import math 
x=0.1 
numerator = math.sin(x ** math.log(x)) ** 2
term1 = x ** (2 * x)
term2 = x ** (x ** (1/3)) 
denominator = math.sqrt(term1 + term2)
y = numerator / denominator
print(f"Значение y при x = {x} : {y}") 