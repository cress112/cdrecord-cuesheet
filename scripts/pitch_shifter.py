import os
import sys
import re

from scripts.config import AudioFormatConfig
from scripts.libraries import AudioReader, AudioCalculator, AudioWriter


class App:
    __SHIFT_WIDTH_PATTERN = r"^(\+|-)(\d+)$"
    __OUTPUT_FILE_SUFFIX = "_shifted"

    @staticmethod
    def main():
        input_file_name, output_file_name, shift_width = App.__parse_args()
        sample_rate = AudioReader.read_metadata(input_file_name).samplerate
        audio_data = AudioReader.read_data(input_file_name)
        new_sample_rate = AudioCalculator.calc_shifted_sample_rate(
            sample_rate, shift_width
        )
        AudioWriter.write(
            output_file_name,
            audio_data,
            new_sample_rate,
            subtype=AudioFormatConfig.OUTPUT_SUBTYPE,
        )

    @staticmethod
    def __parse_args() -> tuple[str, str, int]:
        """
        parse target audio file name from argv
        Returns:
            ( input_file_name, output_file_name, shift_width )
        """
        if len(sys.argv) != 3:
            raise Exception("specify audio file name(*.wav) and shift width(+/-n)")

        input_file_name = sys.argv[1]
        if not input_file_name.endswith(".wav"):
            raise Exception('this script can accept "*.wav" files only')
        if not os.path.isfile(input_file_name):
            raise Exception(f"{input_file_name} does not exist")

        output_file_name = re.sub(
            r"([^.]+).wav",
            r"\1{}.wav".format(App.__OUTPUT_FILE_SUFFIX),
            input_file_name,
        )
        assert input_file_name != output_file_name

        shift_width = sys.argv[2]
        if not re.fullmatch(App.__SHIFT_WIDTH_PATTERN, shift_width):
            raise Exception("invalid shift width format")
        parsed_shift_width = int(shift_width)

        return (input_file_name, output_file_name, parsed_shift_width)


if __name__ == "__main__":
    App.main()
