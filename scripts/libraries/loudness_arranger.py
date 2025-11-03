from numpy import ndarray

from scripts.utilities import LogScale


class LoudnessArranger:
    @staticmethod
    def arrange_amplitude(data: ndarray, log_scaled_level_increment: float) -> ndarray:
        return data * LogScale.log10_scale_to_real_scale(
            log_scaled_level_increment / 20
        )
