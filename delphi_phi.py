#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import cmath

# Step 1: Prompt user input
alpha = float(input("Enter alpha (e.g., 0.1): "))
n = int(input("Enter n (e.g., 1): "))

# Step 2: Define phi range
phi_vals = np.linspace(0.01, np.pi/2-0.01, 100)

# Step 3: Compute del_phi
S_phi_vals = []

for phi in phi_vals:
    exp_i_phi = cmath.exp(1j * phi)
    exp_neg_i_phi = cmath.exp(-1j * phi)

    # Numerator components
    term1 = alpha**2 * (1 + exp_neg_i_phi)**2
    term2 = 2 * (1 + exp_i_phi) * (1 + exp_neg_i_phi) * (1 + alpha**2)
    term3 = 2*(1 - exp_i_phi) - (1 - exp_neg_i_phi) * (n + 1)

    numerator = cmath.sqrt(term1 + term2 + term3) * np.sqrt(alpha**2 + n)

    # Denominator
    denominator = abs(alpha*np.sin(phi))

    S_phi = numerator/denominator
    S_phi_vals.append(S_phi)

# Step 4: Plot
plt.figure(figsize=(8, 5))
# Normalize phi to [0, 1] for the x-axis
phi_normalized = phi_vals / (np.pi / 2)
plt.plot(phi_normalized, S_phi_vals, label=f'α={alpha}, n={n}')
plt.xlabel('φ (radians)')
plt.ylabel('S(φ)')
plt.title('S(φ) vs. φ')
plt.grid(True)
plt.legend()

# Save plot
filename = f"S_phi_alpha_{alpha}_n_{n}.png"
plt.savefig(filename)
print(f"Plot saved as {filename}")
