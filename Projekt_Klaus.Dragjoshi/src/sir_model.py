import numpy as np

def initialize_grid(size=50):
    grid = np.zeros((size, size), dtype=int)

    center = size // 2
    grid[center, center] = 1

    return grid


def update_grid(grid, beta=0.3, gamma=0.05, quarantine_factor=0.5):
    size = grid.shape[0]

    new_grid = grid.copy()

    for i in range(size):
        for j in range(size):

            if grid[i, j] == 1:

                neighbors = [
                    ((i - 1) % size, j),
                    ((i + 1) % size, j),
                    (i, (j - 1) % size),
                    (i, (j + 1) % size)
                ]

                for ni, nj in neighbors:

                    if grid[ni, nj] == 0:

                        if np.random.rand() < beta * quarantine_factor:
                            new_grid[ni, nj] = 1

                if np.random.rand() < gamma:
                    new_grid[i, j] = 2

    return new_grid


def simulate(
    size=50,
    steps=100,
    beta=0.3,
    gamma=0.05,
    quarantine_factor=0.5
):
    grid = initialize_grid(size)

    infected_history = []

    for _ in range(steps):

        infected_history.append(
            np.sum(grid == 1)
        )

        grid = update_grid(
            grid,
            beta,
            gamma,
            quarantine_factor
        )

    return grid, infected_history
