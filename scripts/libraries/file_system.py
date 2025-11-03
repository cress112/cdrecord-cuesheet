import pathlib
from typing import Generator


class FileSystem:
    @staticmethod
    def check_existance(path: str) -> bool:
        return pathlib.Path(path).exists()

    @staticmethod
    def is_dir(path) -> bool:
        return pathlib.Path(path).is_dir()

    @staticmethod
    def mkdir_recursively(path) -> None:
        return pathlib.Path(path).mkdir(parents=True)

    @staticmethod
    def list_dir(path) -> Generator[str, None, None]:
        for path_object in pathlib.Path(path).iterdir():
            yield str(path_object.resolve())

    @staticmethod
    def replace_path(base_file_path: str, target_dir_path: str) -> str:
        if not FileSystem.is_dir(target_dir_path):
            raise Exception(f"変換先がディレクトリじゃないぞ！: {target_dir_path}")
        base_file_name = pathlib.Path(base_file_path).name
        target_full_path = pathlib.Path(target_dir_path).resolve() / base_file_name
        return str(target_full_path)
