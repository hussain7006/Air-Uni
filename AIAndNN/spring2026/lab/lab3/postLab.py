import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ============================================
# COST FUNCTION
# ============================================
def cost_function(t1, t2):
    return t1**2 + t2**2

# ============================================
# GRADIENTS
# ============================================
def grad_t1(t1):
    return 2 * t1        # ∂J/∂θ₁

def grad_t2(t2):
    return 2 * t2        # ∂J/∂θ₂

# ============================================
# 2D GRADIENT DESCENT
# ============================================
def gradient_descent_2d(t1_init, t2_init, eta, iterations):
    
    theta1 = t1_init
    theta2 = t2_init
    
    history = {
        'theta1': [theta1],
        'theta2': [theta2],
        'cost'  : [cost_function(theta1, theta2)]
    }
    
    print(f"\n{'Iter':<6} {'θ₁':<15} {'θ₂':<15} {'Cost J':<15}")
    print("=" * 54)
    print(f"{'0 (init)':<6} {theta1:<15.6f} {theta2:<15.6f} "
          f"{cost_function(theta1, theta2):<15.6f}")
    
    for i in range(iterations):
        
        # Gradients calculate karo
        g1 = grad_t1(theta1)
        g2 = grad_t2(theta2)
        
        # Simultaneous update (important!)
        theta1_new = theta1 - eta * g1
        theta2_new = theta2 - eta * g2
        
        theta1 = theta1_new
        theta2 = theta2_new
        
        J = cost_function(theta1, theta2)
        
        history['theta1'].append(theta1)
        history['theta2'].append(theta2)
        history['cost'].append(J)
        
        print(f"{i+1:<6} {theta1:<15.8f} {theta2:<15.8f} {J:<15.10f}")
    
    return theta1, theta2, history

# ============================================
# RUN KARO - Lab k values
# ============================================
print("=" * 54)
print("  2D Gradient Descent")
print("  J(θ₁,θ₂) = θ₁² + θ₂²")
print("=" * 54)
print("Initial: θ₁ = 0.75, θ₂ = 0.75")
print("Learning Rate η = 0.2")
print("Iterations = 10")

t1_final, t2_final, hist = gradient_descent_2d(
    t1_init    = 0.75,
    t2_init    = 0.75,
    eta        = 0.2,
    iterations = 10
)

print(f"\n{'='*54}")
print(f"FINAL RESULT:")
print(f"θ₁ = {t1_final:.8f}  (Expected → 0)")
print(f"θ₂ = {t2_final:.8f}  (Expected → 0)")
print(f"Final Cost = {cost_function(t1_final, t2_final):.10f}")


fig = plt.figure(figsize=(15, 5))

# --- PLOT 1: Cost Decrease ---
ax1 = fig.add_subplot(1, 3, 1)
ax1.plot(hist['cost'], 'b-o', markersize=5, linewidth=2)
ax1.set_xlabel('Iterations')
ax1.set_ylabel('Cost J(θ)')
ax1.set_title('Cost Decrease Over Time')
ax1.grid(True, alpha=0.3)
for i, c in enumerate(hist['cost']):
    ax1.annotate(f'{c:.3f}', (i, c), 
                textcoords="offset points",
                xytext=(0,8), fontsize=7)

# --- PLOT 2: Parameters Convergence ---
ax2 = fig.add_subplot(1, 3, 2)
ax2.plot(hist['theta1'], 'r-o', markersize=5, label='θ₁')
ax2.plot(hist['theta2'], 'g--s', markersize=5, label='θ₂')
ax2.axhline(y=0, color='black', linestyle=':', 
            linewidth=2, label='True Min = 0')
ax2.set_xlabel('Iterations')
ax2.set_ylabel('Parameter Value')
ax2.set_title('θ₁ & θ₂ Converging to 0')
ax2.legend()
ax2.grid(True, alpha=0.3)

# --- PLOT 3: 3D Surface ---
ax3 = fig.add_subplot(1, 3, 3, projection='3d')

t1_r = np.linspace(-1, 1, 50)
t2_r = np.linspace(-1, 1, 50)
T1, T2 = np.meshgrid(t1_r, t2_r)
J_surf = T1**2 + T2**2

# Surface
ax3.plot_surface(T1, T2, J_surf, alpha=0.3, 
                 cmap='coolwarm')

# GD Path
ax3.plot(hist['theta1'], hist['theta2'], hist['cost'],
         'ko-', markersize=6, linewidth=2, 
         label='GD Path', zorder=5)

# Start aur end point
ax3.scatter([0.75], [0.75], [1.125], 
            color='red', s=100, label='Start', zorder=6)
ax3.scatter([t1_final], [t2_final], 
            [cost_function(t1_final, t2_final)],
            color='green', s=100, label='End', zorder=6)

ax3.set_xlabel('θ₁')
ax3.set_ylabel('θ₂')
ax3.set_zlabel('J(θ)')
ax3.set_title('3D Bowl Shape\nGD Path')
ax3.legend(fontsize=8)

plt.tight_layout()
plt.savefig('post_lab_result.png', dpi=150)
plt.show()