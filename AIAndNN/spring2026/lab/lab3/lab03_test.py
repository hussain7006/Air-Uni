# x = 2
# eta = 0.001

# for i in range(500):
#     x = x-eta*(2*(x+5))
#     print(x)


# def gradient_descent(x, eta, iterations):
#     for i in range(iterations):
#         x = x - eta*(2*(x+5))
#     return x


# learning_rates = [0.0001, 0.001, 0.01, 0.1]
# iterations = [1, 2, 5, 50, 100, 500]

# for eta in learning_rates:
#     for it in iterations:
#         result = gradient_descent(2, eta, it)
#         print("eta:", eta, "iter:", it, "x:", result)


# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(-10, 10, 100)
# y = (x + 5)**2

# plt.plot(x, y)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Gradient Descent Function")
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 10, 100)
# y = 6*x**3 - 12*x**2 + 1

# plt.plot(x, y)
# plt.title("Higher Order Function")
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(-10,10,100)
# y = (x+5)**2

# # gradient descent
# x_gd = 2
# eta = 0.1
# points_x=[]
# points_y=[]

# for i in range(10):
#     points_x.append(x_gd)
#     points_y.append((x_gd+5)**2)
#     x_gd = x_gd - eta*(2*(x_gd+5))

# plt.plot(x,y)
# plt.scatter(points_x,points_y)
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(-10, 10, 100)
# y = (x+5)**2

# # gradient descent
# x_gd = 2
# eta = 0.1

# points_x = []
# points_y = []

# for i in range(10):
#     points_x.append(x_gd)
#     points_y.append((x_gd+5)**2)
#     x_gd = x_gd - eta*(2*(x_gd+5))

# plt.plot(x, y, label='Function: (x+5)^2')
# plt.scatter(points_x, points_y, color='red', label='Gradient Descent Points')
# plt.title("Gradient Descent Convergence")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()



# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # function
# def f(x):
#     return (x+5)**2

# # derivative
# def grad(x):
#     return 2*(x+5)

# # curve
# x = np.linspace(-10,10,400)
# y = f(x)

# # gradient descent params
# x_gd = 2
# eta = 0.1
# iterations = 20

# points_x = []
# points_y = []

# # store points
# for i in range(iterations):
#     points_x.append(x_gd)
#     points_y.append(f(x_gd))
#     x_gd = x_gd - eta*grad(x_gd)

# # plot
# fig, ax = plt.subplots()
# ax.plot(x,y,label="Function")

# point, = ax.plot([], [], 'ro', label="GD Steps")
# final_point, = ax.plot([], [], 'go', markersize=10, label="Local Minimum")

# # animation function
# def update(frame):
#     point.set_data(points_x[:frame], points_y[:frame])
    
#     # show final minimum
#     if frame == len(points_x)-1:
#         final_point.set_data(points_x[-1], points_y[-1])
    
#     return point, final_point

# ani = FuncAnimation(fig, update, frames=len(points_x), interval=500)

# plt.legend()
# plt.title("Gradient Descent Animation")
# plt.show()

# print("Final Local Minimum x =", points_x[-1])
# print("Final Local Minimum y =", points_y[-1])