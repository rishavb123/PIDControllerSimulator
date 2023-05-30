import numpy as np

from systems import PID, Error, System, CompositeSystem


def run_simulation(
    dt: float,
    plant: System,
    goal_output: float,
    initial_output: float,
    Kp: float = 0,
    Ki: float = 0,
    Kd: float = 0,
    max_t: float = None,
    max_steps: float = 100,
):
    if max_t is None:
        max_t = dt * max_steps
    s = CompositeSystem(
        dt=dt,
        systems=[
            Error(dt=dt, goal=goal_output),
            PID(dt=dt, Kp=Kp, Ki=Ki, Kd=Kd),
            plant,
        ],
    )

    ts = np.arange(0, max_t, dt)
    ys = np.zeros_like(ts)
    ys[0] = initial_output

    n = len(ts)

    for i in range(1, n):
        ys[i] = s(ys[i - 1])

    return ts, ys
