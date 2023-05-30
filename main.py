import numpy as np
import matplotlib.pyplot as plt

from pid_simulation import run_simulation

from systems.plants import CarPlant
from systems.plants.car_plant import A_TAG, V_TAG, X_TAG


def main():
    dt = 0.1
    plant = CarPlant(
        dt=dt,
        friction_base=0.1,
        output_tag=V_TAG,
    )
    goal_output = 0.25
    max_steps = 1000

    Kp = -10
    Ki = -1
    Kd = 1

    ts, (es, pids, ys), (i_es, d_es, extra) = run_simulation(
        dt=dt,
        plant=plant,
        goal_output=goal_output,
        Kp=Kp,
        Ki=Ki,
        Kd=Kd,
        max_steps=max_steps,
    )

    fig, ax = plt.subplots(2, 3)

    ax[0][0].plot(ts, es)
    ax[0][0].set_title("Error vs Time")

    ax[0][1].plot(ts, pids)
    ax[0][1].set_title("PID output vs Time")

    ax[0][2].plot(ts, ys)
    ax[0][2].plot(ts, np.ones_like(ts) * goal_output)
    ax[0][2].set_title("Plant output vs Time")

    ax[1][0].plot(ts, i_es)
    ax[1][0].set_title("Error Integral vs Time")

    ax[1][1].plot(ts, d_es)
    ax[1][1].set_title("Error Derivative vs Time")

    ax[1][2].plot(ts, extra)
    ax[1][2].set_title("Extra vs Time")

    plt.show()


if __name__ == "__main__":
    main()