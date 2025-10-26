from math import inf
import numpy

from numpy import ndarray
from scripts.models import AudioAmplitudeModel
from scripts.libraries import LoudnessCalculator, AudioReader, Logger, LoudnessArranger, AudioWriter
from scripts.config import AudioFormatConfig


class EditAudioFileService:

    NORMALIZED_RANGE = AudioFormatConfig.NORMALIZED_RANGE
    OUTPUT_SUBTYPE = AudioFormatConfig.OUTPUT_SUBTYPE

    @classmethod
    def initialize(cls) -> None:
        cls.logger = Logger(cls.__name__)

    @classmethod
    def get_min_loudness_of_range_normalized_files(cls, files: list[AudioAmplitudeModel]) -> float:
        # 振幅範囲を正規化してラウドネス取得 -> 最小値を返す
        min_loudness: float = inf
        for file in files:
            sampling_rate, data = EditAudioFileService.__read_audio_file(file)
            file.input_file_loudness = EditAudioFileService.__get_raw_loudness(sampling_rate, data)
            range_normalized_loudness = EditAudioFileService.__get_range_normalized_loudness(sampling_rate, data)
            cls.logger.debug(f"Loudness {file.input_file_loudness} -> {range_normalized_loudness}: {file.input_file_path}")

            if range_normalized_loudness < min_loudness:
                min_loudness = range_normalized_loudness

        return min_loudness

    @classmethod
    def normalize_audio_files(cls, files: list[AudioAmplitudeModel], target_loudness: float) -> None:
        for file in files:
            if file.input_file_loudness is None:
                raise Exception(f"ラウドネスが設定されてないよ！！: {file.input_file_path}")

            desired_increment = target_loudness - file.input_file_loudness
            sampling_rate, data = EditAudioFileService.__read_audio_file(file)
            normalized_data = LoudnessArranger.arrange_amplitude(data, desired_increment)
            cls.logger.debug(f"{numpy.max(numpy.abs(normalized_data))}: {file.output_file_path}")
            AudioWriter.write(file.output_file_path, normalized_data, sampling_rate, subtype=EditAudioFileService.OUTPUT_SUBTYPE)

        return

    @staticmethod
    def __read_audio_file(file: AudioAmplitudeModel) -> tuple[float, ndarray]:
        metadata = AudioReader.read_metadata(file.input_file_path)
        data = AudioReader.read_data(file.input_file_path)
        return metadata.samplerate, data

    @staticmethod
    def __get_raw_loudness(sampling_rate: float, data: ndarray) -> float:
        # 生データのラウドネス
        return LoudnessCalculator(sampling_rate).calculate(data)

    @staticmethod
    def __get_range_normalized_loudness(sampling_rate: float, data: ndarray) -> float:
        # 値範囲を統一したときのラウドネス
        range_normalized_data = data / numpy.max(numpy.abs(data)) * EditAudioFileService.NORMALIZED_RANGE
        return LoudnessCalculator(sampling_rate).calculate(range_normalized_data)


EditAudioFileService.initialize()