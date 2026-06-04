import os
import sys
import numpy as np
import matplotlib.pyplot as plt

script_dir = os.path.abspath(os.path.dirname(__file__))
project_dir = os.path.dirname(script_dir)
sys.path.append(project_dir)

from src.ranking import pagerank

adj = np.array([
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0]
], dtype=float)

labels = [
    "K1: Rrjetet",
    "K2: Modelet",
    "K3: PageRank",
    "T1: Rrjete Sociale",
    "T2: Teori Grafesh",
    "T3: Modele Fizike",
    "T4: Preferenca"
]

personalization = np.array(
    [0.05, 0.05, 0.05, 0.35, 0.10, 0.35, 0.05],
    dtype=float
)

personalization = personalization / personalization.sum()

standard_rank = pagerank(adj)

personalized_rank = pagerank(
    adj,
    personalization=personalization
)

x = np.arange(len(labels))

plt.figure(figsize=(12, 6), dpi=120)

plt.bar(
    x - 0.2,
    standard_rank,
    width=0.4,
    label="PageRank Standard",
    color="#6ec6ff",
    edgecolor="black",
    linewidth=1
)

plt.bar(
    x + 0.2,
    personalized_rank,
    width=0.4,
    label="Personalized PageRank",
    color="#ffa726",
    edgecolor="black",
    linewidth=1
)

plt.title(
    "Personalized PageRank per Rrjet Materialesh Kursi",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Materiale dhe Tema", fontsize=12)
plt.ylabel("Vlera e PageRank", fontsize=12)
plt.xticks(x, labels, rotation=30, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()

figures_dir = os.path.join(project_dir, "figures")
os.makedirs(figures_dir, exist_ok=True)

figure_path = os.path.join(figures_dir, "personalized_pagerank.png")
plt.savefig(figure_path, dpi=300)

print(f"Figura u ruajt me sukses te: {figure_path}")

plt.show()
