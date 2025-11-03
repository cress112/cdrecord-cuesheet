import numpy
import soundfile


class AudioReader:
    READ_DTYPE = numpy.float64.__name__

    @staticmethod
    def read_metadata(file_name: str) -> soundfile._SoundFileInfo:
        return soundfile.info(file_name)

    @staticmethod
    def read_data(file_name: str) -> numpy.ndarray:
        """
        音声データを2次元配列として返す
        Shape: ( int, 2 )
        """
        return soundfile.read(file_name, dtype=AudioReader.READ_DTYPE, always_2d=True)[
            0
        ]
