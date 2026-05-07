x = 2
eta = 0.5

first_derivative = 2*(x+5)

for i in range(30):
    x = x-eta*first_derivative
    print(x)
