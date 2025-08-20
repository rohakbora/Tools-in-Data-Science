import marimo as mo

# Author: 23f1000897@ds.study.iitm.ac.in
# This Marimo notebook demonstrates interactive data analysis with variable dependencies.

# %% [markdown]
# # Interactive Data Analysis
# This notebook explores the relationship between variables in a dataset.
# It uses widgets for interactivity and dynamic markdown for self-documentation.

# %%
import numpy as np
import matplotlib.pyplot as plt

# Function to generate synthetic dataset
def generate_data(n):
    x = np.linspace(0, 10, n)
    y = np.sin(x) + np.random.normal(0, 0.1, n)
    return x, y

# Initial dataset
data_points = 100
x, y = generate_data(data_points)

plt.scatter(x, y, alpha=0.6)
plt.title("Synthetic Data")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# %%
# Interactive slider widget to control number of data points
num_points = mo.ui.slider(50, 500, value=100, label="Number of Data Points")
num_points

# %%
# Regenerate dataset based on slider state (dependency on num_points)
x, y = generate_data(num_points.value)

plt.scatter(x, y, alpha=0.6, c="tab:blue")
plt.title(f"Synthetic Data with n={num_points.value}")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

# %% [markdown]
# Dynamic markdown output based on widget state
mo.md(f"### Currently displaying dataset with **{num_points.value}** points")

# Comments:
# - The slider `num_points` controls dataset size.
# - Updating the slider triggers regeneration of x, y (dependency across cells).
# - Dynamic markdown reflects the state of the widget.
