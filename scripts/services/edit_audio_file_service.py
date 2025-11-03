from typing import Generator
from math import inf, ceil
import numpy

from scripts.models import AudioAmplitudeModel
from scripts.libraries import (
    LoudnessCalculator,
    AudioReader,
    Logger,
    LoudnessArranger,
    AudioWriter,
)
from scripts.config import AudioFormatConfig
from scripts.utilities import NdarrayUtil


class EditAudioFileService:
    NORMALIZED_RANGE = AudioFormatConfig.NORMALIZED_RANGE
    OUTPUT_SUBTYPE = AudioFormatConfig.OUTPUT_SUBTYPE

    SHIFT_LENGTH = 300

    @classmethod
    def initialize(cls) -> None:
        cls.logger = Logger(cls.__name__)

    @classmethod
    def get_min_loudness_of_range_normalized_files(
        cls, files: list[AudioAmplitudeModel]
    ) -> float:
        # 振幅範囲を正規化してラウドネス取得 -> 最小値を返す
        min_loudness: float = inf
        for file in files:
            sampling_rate = EditAudioFileService.__read_audio_file_samplerate(file)
            file.input_file_normalized_max_loudness = (-1) * inf
            for data in EditAudioFileService.__read_audio_file_normalized_data_block(
                file
            ):
                block_loudness = EditAudioFileService.__get_raw_loudness(
                    sampling_rate, data
                )
                if file.input_file_normalized_max_loudness < block_loudness:
                    file.input_file_normalized_max_loudness = block_loudness

            # ここまでで、正規化されたデータの最大瞬間ラウドネスを取得済み
            cls.logger.debug(
                f"Max Loudness of Normalized Data = {file.input_file_normalized_max_loudness}: {file.input_file_path}"
            )
            if file.input_file_normalized_max_loudness < min_loudness:
                min_loudness = file.input_file_normalized_max_loudness

        return min_loudness

    @classmethod
    def normalize_audio_files(
        cls, files: list[AudioAmplitudeModel], target_loudness: float
    ) -> None:
        for file in files:
            if file.input_file_normalized_max_loudness is None:
                raise Exception(
                    f"ラウドネスが設定されてないよ！！: {file.input_file_path}"
                )

            desired_increment = (
                target_loudness - file.input_file_normalized_max_loudness
            )
            sampling_rate, data = (
                EditAudioFileService.__read_audio_file_normalized_data(file)
            )
            normalized_data = LoudnessArranger.arrange_amplitude(
                data, desired_increment
            )
            cls.logger.debug(
                f"{numpy.max(numpy.abs(normalized_data))}: {file.output_file_path}"
            )
            AudioWriter.write(
                file.output_file_path,
                normalized_data,
                sampling_rate,
                subtype=EditAudioFileService.OUTPUT_SUBTYPE,
            )

    @classmethod
    def __read_audio_file_normalized_data_block(
        cls,
        file: AudioAmplitudeModel,
    ) -> Generator[numpy.ndarray, None, None]:
        samplerate = EditAudioFileService.__read_audio_file_samplerate(file)
        slice_length: int = ceil(samplerate * EditAudioFileService.SHIFT_LENGTH * 1e-3)
        data = AudioReader.read_data(file.input_file_path)
        data = data / numpy.max(numpy.abs(data)) * EditAudioFileService.NORMALIZED_RANGE
        num_channels = data.shape[1]  # 最初に取得

        while len(data) >= slice_length:
            yield data[:slice_length, :]
            data = data[slice_length:, :]  # deleteの代わりにスライシング

        if len(data) > 0:  # 空でない場合のみパディング
            yield NdarrayUtil.pad_zeros(data, [slice_length, num_channels])

    @staticmethod
    def __read_audio_file_samplerate(file: AudioAmplitudeModel) -> int:
        metadata = AudioReader.read_metadata(file.input_file_path)
        return metadata.samplerate

    @staticmethod
    def __read_audio_file_normalized_data(
        file: AudioAmplitudeModel,
    ) -> tuple[float, numpy.ndarray]:
        metadata = AudioReader.read_metadata(file.input_file_path)
        data = AudioReader.read_data(file.input_file_path)
        data = data / numpy.max(numpy.abs(data)) * EditAudioFileService.NORMALIZED_RANGE
        return metadata.samplerate, data

    @staticmethod
    def __get_raw_loudness(sampling_rate: float, data: numpy.ndarray) -> float:
        # 生データのラウドネス
        return LoudnessCalculator(sampling_rate, len(data[:, 0])).calculate(data)


EditAudioFileService.initialize()
