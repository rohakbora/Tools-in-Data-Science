# 23f1000897@ds.study.iitm.ac.in

import marimo as mo

# --- Cell 1: Define variables and interactive widget ---
# Data flow: This cell defines the slider, whose value is used in later cells.
slider = mo.ui.slider(1, 100, label="Number of points")

# --- Cell 2: Dependent computation ---
# Data flow: This cell depends on the slider value to generate data.
import numpy as np
x = np.linspace(0, 10, slider.value)
y = np.sin(x)

# --- Cell 3: Dynamic Markdown Output ---
# Data flow: Markdown depends on both the widget state and computed variables.
mo.md(f"""
### Interactive Sine Wave Analysis  
Slider Value: **{slider.value}**  
Number of Points: **{len(x)}**

Visualization: {"🟢" * (slider.value // 5)}
""")
