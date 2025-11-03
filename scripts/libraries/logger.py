from typing import Any, Optional

from scripts.config.common import CommonConfig
from scripts.consts.log_level import LogLevel


class Logger:
    DEFAULT_CONTEXT = "Default"
    LOG_LEVEL = CommonConfig.LOG_LEVEL
    LOG_LEVEL_ORDER = (
        LogLevel.ERROR,
        LogLevel.WARN,
        LogLevel.LOG,
        LogLevel.DEBUG,
        LogLevel.VERBOSE,
    )
    LOG_LEVEL_ORDER_INDEX = LOG_LEVEL_ORDER.index(CommonConfig.LOG_LEVEL)

    def __init__(self, context: Optional[str] = None) -> None:
        self.__context = context or Logger.DEFAULT_CONTEXT

    def error(self, *args: Any):
        self.__do_log(LogLevel.ERROR, *args)

    def warn(self, *args: Any):
        self.__do_log(LogLevel.WARN, *args)

    def log(self, *args: Any):
        self.__do_log(LogLevel.LOG, *args)

    def debug(self, *args: Any):
        self.__do_log(LogLevel.DEBUG, *args)

    def verbose(self, *args: Any):
        self.__do_log(LogLevel.VERBOSE, *args)

    def __do_log(self, log_level: str, *args: Any) -> None:
        if Logger.__should_log(log_level):
            built_log = self.__build_log(*args)
            print(built_log)

    @staticmethod
    def __should_log(log_level: str) -> bool:
        return Logger.LOG_LEVEL_ORDER.index(log_level) <= Logger.LOG_LEVEL_ORDER_INDEX

    def __build_log(self, *args: Any) -> str:
        return f"[{self.__context}] {str(args)}"
