import abc
from typing import Any


class System(abc.ABC):
    def __init__(self, dt: float, use_integral=False, use_derivative=False, initial_val=None) -> None:
        super().__init__()
        self.dt = dt
        self.use_integral = use_integral
        self.use_derivative = use_derivative
        self.initial_val = initial_val
        self.reset()

    def reset(self) -> None:
        self.last_val = self.initial_val
        self.cur_integral = 0

    def calculate_integral(self, x: float) -> float:
        self.cur_integral += (self.last_val + x) * self.dt / 2
        return self.cur_integral

    def calculate_derivative(self, x: float) -> float:
        return (x - self.last_val) / self.dt

    def store_val(self, x: float) -> None:
        self.last_val = x

    def process(self, x: float) -> float:
        ix, dx = 0, 0
        if self.last_val is not None:
            if self.use_integral:
                ix = self.calculate_integral(x)
            if self.use_derivative:
                dx = self.calculate_derivative(x)
        self.store_val(x)
        return self._process(x=x, ix=ix, dx=dx)

    @abc.abstractmethod
    def _process(self, x: float, ix: float, dx: float) -> float:
        pass

    def __call__(self, x: float) -> float:
        return self.process(x)
