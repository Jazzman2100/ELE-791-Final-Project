#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import cmath

# Step 1: Prompt user input
alpha = float(input("Enter alpha (e.g., 0.1): "))
n = int(input("Enter n (e.g., 1): "))

# Step 2: Define phi range
phi_vals = np.linspace(np.pi/2 * 0.01, np.pi/2, 100)

# Step 3: Compute del_phi
S_phi_vals = []

for phi in phi_vals:
    # Numerator components
    term0 = 1/2 * alpha**2 + alpha**2 * np.cos(phi)
    term1 = 1/2 * alpha**2 * np.cos(2*phi)
    term2 = alpha**2 + n
    term3 = ((alpha**2)-n) * np.cos(phi)
    term4 = -alpha**2 / 2 * (1+np.cos(phi))**2

    numerator = cmath.sqrt(term0 + term1 + term2 + term3 + term4) * (alpha**2 + n)
    # real_num = np.real(numerator)
    # Denominator
    denominator = abs(alpha/cmath.sqrt(2) * np.sin(phi))

    S_phi = numerator/denominator
    S_phi_vals.append(S_phi)


# Step 4: Plot
plt.figure(figsize=(8, 5))
#plt.ylim(0, 20)
# Normalize phi to [0, 1] for the x-axis
phi_normalized = phi_vals / (np.pi / 2)
plt.plot(phi_normalized, S_phi_vals, label=f'α={alpha}, n={n}')
plt.xlabel(r'$\phi$ (unit: $\pi/2$ radian)')
plt.ylabel('S(φ)')
plt.title('S(φ) vs. φ')
plt.grid(True)
plt.legend()

# Save plot
filename = f"S_phi_alpha_{alpha}_n_{n}_04_commutator_fixed.png"
plt.savefig(filename)
print(f"Plot saved as {filename}")
