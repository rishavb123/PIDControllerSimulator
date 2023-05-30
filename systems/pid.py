from .system import System


class PID(System):
    def __init__(self, dt: float, Kp: float = 0, Ki: float = 0, Kd: float = 0) -> None:
        super().__init__(dt, use_integral=Ki != 0, use_derivative=Kd != 0)
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

    def _process(self, x: float, ix: float, dx: float) -> float:
        return self.Kp * x + self.Ki * ix + self.Kd * dx
