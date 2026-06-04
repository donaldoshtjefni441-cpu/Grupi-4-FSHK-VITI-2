import numpy as np

def pagerank(matrix, personalization=None,
             alpha=0.85,
             max_iter=100,
             tol=1e-8):

    n = matrix.shape[0]

    out_degree = matrix.sum(axis=1)
    out_degree[out_degree == 0] = 1

    transition = matrix / out_degree[:, None]

    if personalization is None:
        personalization = np.ones(n) / n

    rank = np.ones(n) / n

    for _ in range(max_iter):

        new_rank = (
            alpha * transition.T @ rank
            + (1 - alpha) * personalization
        )

        if np.linalg.norm(new_rank - rank, 1) < tol:
            rank = new_rank
            break

        rank = new_rank

    return rank / rank.sum()
