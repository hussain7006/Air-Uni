import numpy as np
import matplotlib.pyplot as plt

# =============================================
# FUNCTION 1: y = 3(x-5)^4 + 8(x-5)^3 - 18(x-5)^2
# =============================================
def f1(x):
    return 3*(x-5)**4 + 8*(x-5)**3 - 18*(x-5)**2

def grad_f1(x):
    return 12*(x-5)**3 + 24*(x-5)**2 - 36*(x-5)

# =============================================
# FUNCTION 2: y = 6x^3 - 12x^2 + 1
# =============================================
def f2(x):
    return 6*x**3 - 12*x**2 + 1

def grad_f2(x):
    return 18*x**2 - 24*x

# =============================================
# FUNCTION 3: y = 4x/(1+x^2)
# =============================================
def f3(x):
    return 4*x / (1 + x**2)

def grad_f3(x):
    return (4*(1+x**2) - 4*x*2*x) / (1+x**2)**2
    # = (4 - 4x^2) / (1+x^2)^2

# =============================================
# FUNCTION 4: y = 4x^0.5 - x^2  (sirf positive x)
# =============================================
def f4(x):
    return 4*x**0.5 - x**2

def grad_f4(x):
    return 2*x**(-0.5) - 2*x
    # = 2/sqrt(x) - 2x


def gradient_descent(grad_func, x_start, eta, iterations, x_max=300):
    """
    grad_func  = gradient function
    x_start    = starting x value
    eta        = learning rate
    iterations = kitni baar update karna hai
    x_max      = maximum allowed x value
    """
    x = x_start
    history = [x]
    
    for i in range(iterations):
        grad = grad_func(x)
        x = x - eta * grad
        
        # Boundaries check (sirf positive x)
        x = max(0.0001, min(x, x_max))
        
        history.append(x)
    
    return x, history


learning_rates = [0.0001, 0.001, 0.01, 0.1]
iterations_list = [1, 2, 5, 50, 100, 500]

functions = {
    "F1: 3(x-5)^4+...": (grad_f1, f1),
    "F2: 6x^3-12x^2+1": (grad_f2, f2),
    "F3: 4x/(1+x^2)": (grad_f3, f3),
    "F4: 4x^0.5-x^2": (grad_f4, f4),
}

x_start = 2  # starting point (positive)

print("="*70)
for fname, (grad_fn, fn) in functions.items():
    print(f"\nFunction: {fname}")
    print(f"{'Iterations':<12}", end="")
    for eta in learning_rates:
        print(f"η={eta:<10}", end="")
    print()
    print("-"*70)
    
    for itr in iterations_list:
        print(f"{itr:<12}", end="")
        for eta in learning_rates:
            try:
                x_final, _ = gradient_descent(grad_fn, x_start, eta, itr)
                y_final = fn(x_final)
                print(f"x={x_final:.3f}  ", end="")
            except:
                print(f"ERROR      ", end="")
        print()


# Ek function ka plot karte hain example k taur par
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

fn_info = [
    ("F1: 3(x-5)^4+8(x-5)^3-18(x-5)^2", grad_f1, f1),
    ("F2: 6x^3-12x^2+1", grad_f2, f2),
    ("F3: 4x/(1+x^2)", grad_f3, f3),
    ("F4: 4sqrt(x)-x^2", grad_f4, f4),
]

x_ranges = [
    np.linspace(0.1, 10, 300),
    np.linspace(0.1, 5, 300),
    np.linspace(0.1, 10, 300),
    np.linspace(0.1, 4, 300),
]

for idx, ((title, gfn, fn), xr) in enumerate(zip(fn_info, x_ranges)):
    ax = axes[idx]
    
    # Function plot
    y_vals = [fn(xi) for xi in xr]
    ax.plot(xr, y_vals, 'b-', linewidth=2, label='Function')
    
    # GD paths for different learning rates
    colors = ['red', 'green', 'orange', 'purple']
    for eta, color in zip([0.0001, 0.001, 0.01, 0.1], colors):
        try:
            x_final, history = gradient_descent(gfn, 2, eta, 100)
            y_history = [fn(xi) for xi in history]
            ax.plot(history, y_history, 'o-', color=color, 
                   markersize=3, alpha=0.6, label=f'η={eta}')
        except:
            pass
    
    ax.set_title(title, fontsize=9)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('gradient_descent_results.png', dpi=150, bbox_inches='tight')
plt.show()
print("Plot save ho gaya!")