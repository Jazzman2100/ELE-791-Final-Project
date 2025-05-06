#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import cmath
import math

# Step 1: Prompt user input
alpha_min = float(input("Enter minimum alpha (e.g., 0): "))
alpha_max = float(input("Enter maximum alpha (e.g., 3.0): "))
phi = float(input("Enter phi (e.g., 2): "))
n = 0  # Fixed n value

# Step 2: Define alpha range and phi
n_hat_min = alpha_min**2 + n
n_hat_max = alpha_max**2 + n
n_vals = np.linspace(n_hat_min, n_hat_max)

if phi == 2:
  phi = np.pi/2
else:
  phi = 0

# Step 3: Compute del_phi for each alpha
del_phi_vals = []

for alpha in n_vals:
   term1 = (alpha**2) * (1 + ((1/2)*(math.cos(2*phi))) + (math.cos(phi)) - ((1/2)*(math.cos(phi)**2)))
   term2 = n*(1-(math.cos(phi)))
   term3 = 1

   numerator = math.sqrt(term1 + term2 + term3)
   denominator = abs((alpha/math.sqrt(2))*math.sin(phi))   
   del_phi = numerator/denominator
   del_phi_vals.append(del_phi)

# Step 4: Plot
plt.figure(figsize=(8, 5))
plt.plot(n_vals, del_phi_vals, label=f'n={n}, φ={phi}')
plt.xlabel(r'$\langle \hat{n} \rangle$')
plt.ylabel(r'$\Delta\phi$')
plt.title(f'Δφ vs. ⟨n̂⟩ at φ = {phi}')
plt.grid(True)
plt.xticks(np.arange(int(min(n_vals)), int(max(n_vals)) + 1, 1))
plt.ylim(0, 2)
plt.axvline(x=1, color='red', linestyle='--', linewidth=1, label=r'$\langle \hat{n} \rangle = 1$')
plt.legend()

filename = f"del_phi_alpha_{alpha}_n_{n}_LT_01.png"
plt.savefig(filename)
print(f"Plot saved as {filename}")
