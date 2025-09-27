from scripts.libraries import Logger
from scripts.services import AudioFilePathService, EditAudioFileService
"""
Usage: python -m src.loudness_normalizer <dir_including_wav_files> <dir_output>
"""

class App:
    @staticmethod
    def main():
        logger = Logger(App.__name__)
        # 引数が2つであることを確認, ディレクトリであることを確認, 変換対象wavパス一覧を取得
        logger.log("READING...")
        input_wav_files = AudioFilePathService.find_audio_files()
        # ファイル全件読み込み -> 最小ラウドネスを取得
        min_loudness = EditAudioFileService.get_min_loudness_of_range_normalized_files(input_wav_files)
        logger.debug(min_loudness)
        # すべてのファイルのラウドネスを最小値に正規化
        logger.log("NORMALIZING...")
        EditAudioFileService.normalize_audio_files(input_wav_files, min_loudness)


if __name__ == "__main__":
    App.main()
