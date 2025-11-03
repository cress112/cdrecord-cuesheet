import sys
import os

from scripts.consts import LogLevel


class CommonConfig:
    LOG_LEVEL = os.getenv("LOG_LEVEL", LogLevel.LOG)  # デフォルトはlog

    INPUT_DIR = ""
    OUTPUT_DIR = ""

    @classmethod
    def validate(cls) -> None:
        args = sys.argv[1:]
        if len(args) != 2:
            raise Exception("実行引数は2つ！")
        cls.INPUT_DIR = args[0]
        cls.OUTPUT_DIR = args[1]


CommonConfig.validate()
