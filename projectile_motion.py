import numpy as np
import matplotlib.pyplot as plt

# Parameters
v0 = 25  # initial velocity (m/s)
theta_deg = 40  # launch angle (degrees)
g = 9.8  # gravity

theta = np.radians(theta_deg)
T = 2 * v0 * np.sin(theta) / g

t = np.linspace(0, T, 100)
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t ** 2

plt.figure(figsize=(8, 4))
plt.plot(x, y, label=f'v₀={v0} m/s, θ={theta_deg}°')
plt.title('Projectile Motion - Physics Visualization')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('projectile_motion.png')
plt.show()
