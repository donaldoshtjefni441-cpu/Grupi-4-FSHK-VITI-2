import numpy as np

def lorenz(state, sigma=10.0, rho=28.0, beta=8.0 / 3.0):
    x, y, z = state

    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z

    return np.array([dx, dy, dz])


def rossler(state, a=0.2, b=0.2, c=5.7):
    x, y, z = state

    dx = -y - z
    dy = x + a * y
    dz = b + z * (x - c)

    return np.array([dx, dy, dz])


def runge_kutta_4(system, initial_state, dt, steps):
    trajectory = np.zeros((steps, 3))
    trajectory[0] = initial_state

    for i in range(1, steps):
        s = trajectory[i - 1]

        k1 = system(s)
        k2 = system(s + 0.5 * dt * k1)
        k3 = system(s + 0.5 * dt * k2)
        k4 = system(s + dt * k3)

        trajectory[i] = s + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    return trajectory
