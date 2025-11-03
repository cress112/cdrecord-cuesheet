from numpy import ndarray
import pyloudnorm


class LoudnessCalculator:
    BLOCK_SIZE_RATIO = 0.9

    def __init__(self, sampling_rate: float, block_length: int) -> None:
        block_size = block_length / sampling_rate * LoudnessCalculator.BLOCK_SIZE_RATIO
        self.meter = pyloudnorm.Meter(sampling_rate, block_size=block_size)

    def calculate(self, data: ndarray) -> float:
        return self.meter.integrated_loudness(data)
