import numpy as np

from .system import System


class Capture(System):
    def __init__(self, dt: float) -> None:
        super().__init__(dt, use_integral=False, use_derivative=False)
        self.cur_lst = []

    def reset(self) -> None:
        self.cur_lst = []
        return super().reset()

    def _process(self, x: float, ix: float, dx: float) -> float:
        self.cur_lst.append(x)
        return x

    def get_np(self) -> np.ndarray:
        return np.array(self.cur_lst)
