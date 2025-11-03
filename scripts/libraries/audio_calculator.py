class AudioCalculator:
    @staticmethod
    def calc_shifted_sample_rate(sample_rate: int, shift_width: int) -> int:
        return round(sample_rate * (2 ** (shift_width / 12)))
