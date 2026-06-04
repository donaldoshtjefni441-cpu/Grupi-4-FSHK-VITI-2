import os
import sys
import numpy as np
import matplotlib.pyplot as plt

script_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(script_dir)
sys.path.append(project_dir)

from src.attractors import lorenz, rossler, runge_kutta_4

dt = 0.01
steps = 8000

lorenz_initial = np.array([1.0, 1.0, 1.0])
lorenz_close_initial = np.array([1.001, 1.0, 1.0])

rossler_initial = np.array([1.0, 1.0, 1.0])

lorenz_traj = runge_kutta_4(lorenz, lorenz_initial, dt, steps)
lorenz_close_traj = runge_kutta_4(lorenz, lorenz_close_initial, dt, steps)
rossler_traj = runge_kutta_4(rossler, rossler_initial, dt, steps)

distance = np.linalg.norm(lorenz_traj - lorenz_close_traj, axis=1)
time = np.arange(steps) * dt

fig = plt.figure(figsize=(14, 10), dpi=120)

ax1 = fig.add_subplot(2, 2, 1, projection="3d")
ax1.plot(
    lorenz_traj[:, 0],
    lorenz_traj[:, 1],
    lorenz_traj[:, 2],
    color="darkblue",
    linewidth=0.5
)
ax1.set_title("Atraktori Lorenz")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

ax2 = fig.add_subplot(2, 2, 2, projection="3d")
ax2.plot(
    rossler_traj[:, 0],
    rossler_traj[:, 1],
    rossler_traj[:, 2],
    color="darkred",
    linewidth=0.5
)
ax2.set_title("Atraktori Rossler")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(time, distance, color="black", linewidth=1)
ax3.set_title("Ndjeshmeria ndaj kushteve fillestare")
ax3.set_xlabel("Koha")
ax3.set_ylabel("Distanca midis trajektoreve")
ax3.grid(True, linestyle="--", alpha=0.4)

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(
    lorenz_traj[:, 0],
    lorenz_traj[:, 2],
    color="purple",
    linewidth=0.6,
    label="Lorenz"
)
ax4.plot(
    rossler_traj[:, 0],
    rossler_traj[:, 2],
    color="orange",
    linewidth=0.6,
    label="Rossler"
)
ax4.set_title("Krahasim i projeksioneve x-z")
ax4.set_xlabel("x")
ax4.set_ylabel("z")
ax4.legend()
ax4.grid(True, linestyle="--", alpha=0.4)

plt.suptitle(
    "Atraktoret Lorenz dhe Rossler",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()

figures_dir = os.path.join(project_dir, "figures")
os.makedirs(figures_dir, exist_ok=True)

figure_path = os.path.join(figures_dir, "lorenz_rossler.png")
plt.savefig(figure_path, dpi=300)

print(f"Figura u ruajt me sukses te: {figure_path}")

plt.show()
