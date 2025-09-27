import numpy
import soundfile

class AudioReader:

    READ_DTYPE = numpy.float64.__name__

    @staticmethod
    def read_metadata(file_name: str) -> soundfile._SoundFileInfo:
        return soundfile.info(file_name)

    @staticmethod
    def read_data(file_name: str) -> numpy.ndarray:
        return soundfile.read(file_name, dtype=AudioReader.READ_DTYPE)[0]
