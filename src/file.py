import json
from typing import Dict, Any
import os


def save_dict_to_json(data: Dict[str, Any], file_path: str):
    """
    将字典保存为JSON格式的文件。

    :param data: 要保存的字典数据。
    :param file_path: 保存的文件路径。
    """
    try:
        with open(file_path, "w+") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        raise


def read_json_to_dict(file_path: str) -> Dict[str, Any]:
    """
    从JSON文件中读取字典。

    :param file_path: 要读取的JSON文件路径。
    :return: 从JSON文件解析出的字典。
    """
    try:
        with open(file_path, "r") as file:
            loaded_data = json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        raise

    return loaded_data


def check_file_exist(file_path: str):
    """
    检查文件是否存在。
    :param file_path: 文件路径。
    :return: True表示文件存在，False表示文件不存在。
    """
    return os.path.exists(file_path)
