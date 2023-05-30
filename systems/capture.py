import numpy as np

from .system import System


class Capture(System):
    def __init__(self, dt: float, use_integral=False, use_derivative=False) -> None:
        super().__init__(dt, use_integral=use_integral, use_derivative=use_derivative)
        self.x_lst = []
        self.ix_lst = []
        self.dx_lst = []

    def reset(self) -> None:
        self.x_lst = []
        self.ix_lst = []
        self.dx_lst = []
        return super().reset()

    def _process(self, x: float, ix: float, dx: float) -> float:
        self.x_lst.append(x)
        self.ix_lst.append(ix)
        self.dx_lst.append(dx)
        return x

    def get_x_np(self) -> np.ndarray:
        return np.array(self.x_lst)

    def get_ix_np(self) -> np.ndarray:
        return np.array(self.ix_lst)

    def get_dx_np(self) -> np.ndarray:
        return np.array(self.dx_lst)
