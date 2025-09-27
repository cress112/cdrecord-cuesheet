from typing import Any
from numpy import ndarray
import pyloudnorm

class LoudnessCalculator:

    def __init__(self, sampling_rate: float) -> None:
        self.meter = pyloudnorm.Meter(sampling_rate)

    def calculate(self, data: ndarray) -> float:
        return self.meter.integrated_loudness(data)

