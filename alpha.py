#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import cmath

# Step 1: Prompt user input
alpha_min = float(input("Enter minimum alpha (e.g., 0.1): "))
alpha_max = float(input("Enter maximum alpha (e.g., 3.0): "))
n = 1  # Fixed n value

# Step 2: Define alpha range and fixed phi
alpha_vals = np.linspace(alpha_min, alpha_max, 200)
phi = np.pi / 2

# Step 3: Compute del_phi for each alpha
del_phi_vals = []

for alpha in alpha_vals:
    exp_i_phi = cmath.exp(1j * phi)
    exp_neg_i_phi = cmath.exp(-1j * phi)

    # Numerator components
    term1 = alpha**2 * (1 + exp_neg_i_phi)**2
    term2 = 2 * (1 + exp_i_phi) * (1 + exp_neg_i_phi) * (1 + alpha**2)
    term3 = 2*(1 - exp_i_phi) - (1 - exp_neg_i_phi) * (n + 1)

    numerator = cmath.sqrt(term1 + term2 + term3)

    del_phi_vals.append(numerator)

# Step 4: Plot
plt.figure(figsize=(8, 5))
plt.plot(alpha_vals, del_phi_vals, label=f'n={n}, φ=π/2')
plt.xlabel('α')
plt.ylabel('Δφ')
plt.title('Δφ vs. α at φ = π/2')
plt.grid(True)
plt.legend()

# Step 5: Save plot
filename = f"del_phi_vs_alpha_from_{alpha_min}_to_{alpha_max}_n_{n}.png"
plt.savefig(filename)
