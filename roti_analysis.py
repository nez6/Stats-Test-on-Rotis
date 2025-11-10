# Roti Analysis


## This is the calculation of the sample size for a roti analysis

import math
import scipy.stats as stats
from scipy.stats import norm
import pandas as pd


effect_size = 0.8
# The effect size was determined as my mom - a Subject Matter Expert (SME) - suggested that there was a high correlation between the oil and no oil
alpha_level = 0.05
# This value is commonly used as the threshold for statistical significance
power = 0.8
# This value indicates an 80% chance of correctly rejecting the null hypothesis when it is false

def calculate_sample_size(effect_size, alpha_level, power):
    z_alpha = norm.ppf(1 - alpha_level / 2)
    z_beta = norm.ppf(power)
    sample_size = math.ceil(2 * ((z_alpha + z_beta) ** 2) / (effect_size ** 2))
    return int(sample_size)

sample_size = calculate_sample_size(effect_size, alpha_level, power)
print(f"Calculated sample size: {sample_size}")

# Read CSV files with Roti Information

oil_roti = pd.read_csv("2-1-oil.csv")
no_oil_roti = pd.read_csv("2-1-ratio.csv")


