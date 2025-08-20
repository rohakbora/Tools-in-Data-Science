import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ---- Generate synthetic data ----
np.random.seed(42)
months = pd.date_range(start="2024-01-01", periods=12, freq="M")
segments = ["Premium", "Standard", "Budget"]

data = []
for seg in segments:
    base = np.linspace(50, 120, 12)  # growth trend
    seasonal = 10 * np.sin(np.linspace(0, 2*np.pi, 12))  # seasonal variation
    noise = np.random.normal(0, 5, 12)  # randomness
    revenue = base + seasonal + noise + (20 if seg=="Premium" else (0 if seg=="Standard" else -15))
    for m, r in zip(months, revenue):
        data.append({"Month": m, "Revenue": r, "Segment": seg})

df = pd.DataFrame(data)

# ---- Visualization ----
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # 512x512 px at dpi=64
sns.lineplot(data=df, x="Month", y="Revenue", hue="Segment", marker="o", palette="Set2")

plt.title("Monthly Revenue Trends by Customer Segment", fontsize=16, weight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue ($K)")
plt.xticks(rotation=45)

# ---- Save output ----
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
