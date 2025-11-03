import re
from scripts.config import CommonConfig
from scripts.libraries import FileSystem, Logger
from scripts.models import AudioAmplitudeModel


class AudioFilePathService:
    AUDIO_FILE_PATTERN = re.compile(r"^.*\.(wav|WAV)$")

    @classmethod
    def initialize(cls) -> None:
        cls.logger = Logger(AudioFilePathService.__name__)

    @classmethod
    def find_audio_files(cls) -> list[AudioAmplitudeModel]:
        """指定ディレクトリに含まれる音声ファイル一覧を返します"""
        input_dir_name = CommonConfig.INPUT_DIR
        output_dir_name = CommonConfig.OUTPUT_DIR
        cls.logger.debug(input_dir_name, output_dir_name)

        if not FileSystem.is_dir(input_dir_name):
            raise Exception(f"指定ディレクトリがないよ！: {input_dir_name}")

        AudioFilePathService.__initialize_output_dir(output_dir_name)
        ret: list[AudioAmplitudeModel] = []
        for input_file_path in FileSystem.list_dir(input_dir_name):
            if (
                AudioFilePathService.AUDIO_FILE_PATTERN.fullmatch(input_file_path)
                is not None
            ):
                output_file_path = FileSystem.replace_path(
                    input_file_path, output_dir_name
                )
                ret.append(
                    AudioAmplitudeModel(
                        input_file_path=input_file_path,
                        output_file_path=output_file_path,
                    )
                )

        return ret

    @staticmethod
    def __initialize_output_dir(dir_path: str) -> None:
        if not FileSystem.check_existance(dir_path):
            FileSystem.mkdir_recursively(dir_path)
        if not FileSystem.is_dir(dir_path):
            raise Exception(f"出力ディレクトリの指定がおかしいよ！: {dir_path}")


AudioFilePathService.initialize()
