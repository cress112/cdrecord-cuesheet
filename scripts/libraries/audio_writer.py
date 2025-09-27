from numpy import ndarray
import soundfile

class AudioWriter:
    @staticmethod
    def write(file_name: str, data: ndarray, sampling_rate: float, subtype: str) -> None:
        return soundfile.write(file_name, data, sampling_rate, subtype)