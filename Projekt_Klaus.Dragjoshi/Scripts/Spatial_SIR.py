import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

script_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(script_dir)
sys.path.append(project_dir)

from src.sir_model import simulate

size = 60
steps = 120
beta = 0.35
gamma = 0.06
quarantine_factor = 0.55

final_grid, infected_history = simulate(
    size=size,
    steps=steps,
    beta=beta,
    gamma=gamma,
    quarantine_factor=quarantine_factor
)

time = np.arange(len(infected_history))

fig, axes = plt.subplots(1, 2, figsize=(13, 5), dpi=120)

cmap = ListedColormap(["#8bc34a", "#f44336", "#2196f3"])

axes[0].imshow(final_grid, cmap=cmap, vmin=0, vmax=2)
axes[0].set_title("Gjendja finale e rrjetes SIR")
axes[0].set_xticks([])
axes[0].set_yticks([])

axes[1].plot(
    time,
    infected_history,
    color="darkred",
    linewidth=2
)

axes[1].set_title("Evolucioni i numrit te te infektuarve")
axes[1].set_xlabel("Hapat kohore")
axes[1].set_ylabel("Numri i te infektuarve")
axes[1].grid(True, linestyle="--", alpha=0.4)

plt.suptitle(
    "Model SIR hapesinor ne rrjet me karantine",
    fontsize=15,
    fontweight="bold"
)

plt.tight_layout()

figures_dir = os.path.join(project_dir, "figures")
os.makedirs(figures_dir, exist_ok=True)

figure_path = os.path.join(figures_dir, "spatial_sir.png")
plt.savefig(figure_path, dpi=300)

print(f"Figura u ruajt me sukses te: {figure_path}")

plt.show()
