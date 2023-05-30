from ..system import System

THETA = 0
THETA_DOT = 1

X_TAG = 0
V_TAG = 1
A_TAG = 2


class CarPlant(System):
    def __init__(
        self,
        dt: float,
        friction_base: float = 0,
        friction_v_multiplier: float = 0,
        theta0: float = 0,
        x0: float = 0,
        v0: float = 0,
        a0: float = 0,
        inp_type: int = THETA,
        theta_control: int = A_TAG,
        theta_multiplier: float = 0.1,
        output_tag: int = X_TAG,
    ) -> None:
        super().__init__(dt, use_integral=False, use_derivative=False)
        self.friction_base = friction_base
        self.friction_v_multiplier = friction_v_multiplier
        self.x = x0
        self.v = v0
        self.a = a0
        self.theta = theta0
        self.inp_type = inp_type
        self.theta_control = theta_control
        self.theta_multiplier = theta_multiplier
        self.output_tag = output_tag

    def _process(self, x: float, ix: float, dx: float) -> float:
        if self.inp_type == THETA:
            self.theta = x
        elif self.inp_type == THETA_DOT:
            self.theta += x
        if self.theta_control == X_TAG:
            self.x = self.theta * self.theta_multiplier
        elif self.theta_control == V_TAG:
            self.v = self.theta * self.theta_multiplier
        elif self.theta_control == A_TAG:
            self.a = self.theta * self.theta_multiplier

        s = 1 if self.v > 0 else (0 if self.v == 0 else -1)

        self.v += (
            self.a - s * self.friction - self.v * self.friction_v_multiplier
        ) * self.dt
        self.x += self.v * self.dt

        if self.output_tag == X_TAG:
            return self.x
        if self.output_tag == V_TAG:
            return self.v
        if self.output_tag == A_TAG:
            return self.a
        
        return self.x