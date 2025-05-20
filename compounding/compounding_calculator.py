# 📈 Compounding Calculator – Estimate Your Investment Growth Over Time

# 👉 Step 1: Edit the numbers below to try your own scenario.
# You can change the monthly investment, return rate, and duration.

monthly_contribution = 500        # Amount you invest every month ($)
years = 40                        # Number of years you invest for
annual_rate = 0.098               # Expected annual return (e.g. 0.098 = 9.8%)
contribution_increase = 0.10      # Yearly % increase in your monthly contribution (e.g. 0.10 = 10%)

# 👉 Step 2: Click the ▶️ "Run" button at the top left of this cell to generate your results.

# 📌 First time using Colab?
# - A warning may appear: click "Run anyway"
# - Wait a few seconds while it connects to the Python backend
# - After running, scroll down to see your personalized chart and summary table

# 🛠️ You can change the numbers and run it again as many times as you like!
################# Implementation – Do not edit below this line #################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Calculations
months = years * 12
monthly_rate = (1 + annual_rate)**(1/12) - 1
balances = []
contributions = []
balance = 0
total_contributed = 0
contribution = monthly_contribution

for month in range(months):
    if month > 0 and month % 12 == 0:
        contribution *= (1 + contribution_increase)
    balance = balance * (1 + monthly_rate) + contribution
    total_contributed += contribution
    balances.append(balance)
    contributions.append(total_contributed)

# Yearly Summary Table
years_range = np.arange(1, months + 1) / 12
df = pd.DataFrame({
    'Year': years_range,
    'Total Contributions': contributions,
    'Portfolio Value': balances
})

# Filter full years and reset index
df = df[df['Year'] % 1 == 0].reset_index(drop=True)
df['Growth (%)'] = 100 * (df['Portfolio Value'] - df['Total Contributions']) / df['Total Contributions']
df = df[['Year', 'Total Contributions', 'Portfolio Value', 'Growth (%)']]
df = df.round(2)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Portfolio Value'], label=f'{annual_rate*100:.1f}% Annual Return')
plt.title(f'Growth of ${monthly_contribution}/Month Over {years} Years\n'
          f'with {contribution_increase*100:.0f}% Annual Contribution Increase')
plt.xlabel('Years')
plt.ylabel('Portfolio Value ($)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Display the summary table
df
