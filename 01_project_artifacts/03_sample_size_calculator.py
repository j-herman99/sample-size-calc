import pandas as pd
import numpy as np
import math

# Define populatin sizes and marigins of error

population_sizes = [100, 500, 1000, 3000, 10000, 100000, 1000000]
margins_of_error = [0.01, 0.03,0.05, 0.1]

# Z-score for 95% confidence level

Z = 1.96
p = 0.5  #Est. proportion (max variability)

# Function to calculate sample size for infinite population

def calc_m(E):
    return (Z**2 * p * (1-p)) / (E**2)

# Function to adjust sample size for finite population

def calc_n(m, N):
    return m / (1 + ((m-1)/N))

# Build sample size table

data = []
for E in margins_of_error:
    m = calc_m(E)
    row = []
    for N in population_sizes:
        n = calc_n(m, N)
        row.append(math.ceil(n)) # Round up to nearest whole number
    data.append(row)

# Create a labeled dataframe

df = pd.DataFrame(
    data,
    columns=[f"N={n}" for n in population_sizes],
    index=[f"±{int(E * 100)}%" for E in margins_of_error]
)

# Print table

df.to_csv("/Documents/sample-size-calculator/sample_size_reference_table.csv", index=True)



