from .system import System

class Error(System):

    def __init__(self, dt: float, goal: float) -> None:
        super().__init__(dt, use_integral=False, use_derivative=False)
        self.goal = goal

    def _process(self, x: float, ix: float, dx: float) -> float:
        return x - self.goal