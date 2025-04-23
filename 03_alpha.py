#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import cmath

# Step 1: Prompt user input
alpha_min = float(input("Enter minimum alpha (e.g., 0.1): "))
alpha_max = float(input("Enter maximum alpha (e.g., 3.0): "))
phi_multiple = float(input("Enter phi in multiples of π (e.g., 2 for 2π): "))
n = 1  # Fixed n value

# Step 2: Define alpha range and phi
alpha_vals = np.linspace(alpha_min, alpha_max, 200)
phi = np.pi * phi_multiple

# Step 3: Compute del_phi for each alpha
del_phi_vals = []

for alpha in alpha_vals:
    term1 = alpha**2 * (1 + (1/2)*cmath.cos(2*phi) + cmath.cos(phi) - (1/2)*cmath.cos(phi)**2)
    term2 = n * (1 - cmath.cos(phi))
    term3 = 1

    numerator = cmath.sqrt(term1 + term2 + term3)
    del_phi_vals.append(numerator)


# Step 4: Plot
plt.figure(figsize=(8, 5))
plt.plot(alpha_vals, del_phi_vals, label=f'n={n}, φ={phi_multiple}π')
plt.xlabel('α')
plt.ylabel('Δφ')
plt.title(f'Δφ vs. α at φ = {phi_multiple}π')
plt.grid(True)
plt.legend()

# Step 5: Save plot with phi in filename
phi_str = str(phi_multiple).replace('.', ' ')
filename = f"del_phi_vs_alpha_from_{alpha_min}_to_{alpha_max}_n_{n}_phi_{phi_str}pi.png"
plt.savefig(filename)
