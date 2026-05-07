import sympy as sp

x = sp.symbols('x')

# f = (x+5)**2
# 4x/(1+x2)
f =   (4*x)/(1+x**2)

df = sp.diff(f, x)
print(df)
