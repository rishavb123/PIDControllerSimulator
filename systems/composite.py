from typing import List

from . import System

class CompositeSystem(System):
    
    def __init__(self, dt: float, systems: List[System]=[]) -> None:
        super().__init__(dt, False, False)
        self.systems = systems

    def _process(self, x: float, ix: float, dx: float) -> float:
        z = x
        for s in self.systems:
            z = s(z)
        return z

