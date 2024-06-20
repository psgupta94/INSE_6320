import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 40000  # Given risk tolerance
x = np.linspace(0, 250000, 1000)
U = 1 - np.exp(-x / R)

# Given data
EU_d1 = 0.974450239
EV = 146685.14
CE = 146685.0927
RP = EV - CE

# Plot the utility curve
plt.figure(figsize=(12, 8))
plt.plot(x, U, label='Risk Utility Curve', color='blue')

# Plot the expected utility line
plt.axhline(y=EU_d1, color='red', linestyle='--', label='Expected Utility (EU)')

# Plot the expected value line
plt.axvline(x=EV, color='orange', linestyle='-', label='Expected Value (EV)')

# Plot the certainty equivalent line
plt.axvline(x=CE, color='green', linestyle='-.', label='Certainty Equivalent (CE)')

# Mark the points
plt.scatter([EV], [EU_d1], color='orange', zorder=5)
plt.scatter([CE], [EU_d1], color='green', zorder=5)

# Annotate the points
plt.annotate(f'CE ({CE:.2f})', xy=(CE, EU_d1), xytext=(CE - 50000, EU_d1 - 0.1),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)
plt.annotate(f'RP ({RP:.2f})', xy=(CE, EU_d1), xytext=(EV - 100000, EU_d1 - 0.2),
             arrowprops=dict(facecolor='purple', shrink=0.05), fontsize=12)
plt.annotate('Risk-Averse', xy=(CE + 5000, EU_d1 - 0.05), color='purple', fontsize=12)

# Graph settings
plt.title('Risk Utility Curve')
plt.xlabel('Wealth (x)')
plt.ylabel('Utility')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
