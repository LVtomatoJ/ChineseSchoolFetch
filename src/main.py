import os
import shutil
import threading
from typing import List
from fetch import (
    get_school_code_list,
    get_school_info,
    get_school_logo,
    get_school_special,
    get_special_info,
)
from file import check_file_exist, read_json_to_dict, save_dict_to_json
from scheme.school_code import SchoolCodeData
from scheme.school_info import SchoolInfoData
from scheme.school_special import SchoolSpecial, SchoolSpecialData

import concurrent.futures


def check_and_create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# 定义一个处理任务的函数
def init_school_task(school_code_info):
    thread_name = threading.current_thread().getName()
    print(
        f"当前线程: {thread_name}, 处理任务：{school_code_info.school_id}:{school_code_info.name}"
    )
    # 获取学校信息
    try:
        school_info_data = read_json_to_dict(
            f"data/school_info/{school_code_info.school_id}.json"
        )
    except Exception as e:
        school_info_data = get_school_info(school_code_info.school_id)
        save_dict_to_json(
            school_info_data, f"data/school_info/{school_code_info.school_id}.json"
        )
    school_info_data: SchoolInfoData = SchoolInfoData(**school_info_data)
    # 获取学校专业信息
    school_special_data = get_school_special(school_code_info.school_id)
    save_dict_to_json(
        school_special_data,
        f"data/school_special/{school_code_info.school_id}.json",
    )
    school_special_data: SchoolSpecialData = SchoolSpecialData(**school_special_data)
    school_special_list: List[SchoolSpecial] = school_special_data.data.special_detail[
        1
    ]
    for school_special in school_special_list:
        # FIXME 不知道为什么有时候school_special会变成dict类型
        if isinstance(school_special, dict):
            special_id = school_special["special_id"]
            special_name = school_special["special_name"]
        else:
            special_id = school_special.special_id
            special_name = school_special.special_name
        # 检查专业是否保存
        if not check_file_exist(f"data/special/{special_id}.json"):
            print(f"保存专业:{special_name}")
            special_data = get_special_info(special_id)
            if not special_data:
                # 存在找不到的的情况 保存一个空文件dict
                save_dict_to_json({}, f"data/special/{special_id}.json")
            save_dict_to_json(special_data, f"data/special/{special_id}.json")


def get_ont_school_logo(school_code_info):
    thread_name = threading.current_thread().getName()
    print(
        f"当前线程: {thread_name}, 处理任务：{school_code_info.school_id}:{school_code_info.name}"
    )
    if not check_file_exist(f"data/school_logo/{school_code_info.school_id}.jpg"):
        logo_data = get_school_logo(school_code_info.school_id)
        with open(f"data/school_logo/{school_code_info.school_id}.jpg", "wb") as f:
            shutil.copyfileobj(logo_data, f)
        print(f"保存学校logo:{school_code_info.school_id}:{school_code_info.name}")


# 初始化获取所有学校数据
def init():
    check_and_create_folder("data")
    check_and_create_folder("data/school_info")
    check_and_create_folder("data/school_special")
    check_and_create_folder("data/special")
    check_and_create_folder("data/school_logo")

    try:
        data = read_json_to_dict("data/school_code.json")
    except Exception as e:
        data = get_school_code_list()
        save_dict_to_json(data, "data/school_code.json")
    formate_data: SchoolCodeData = SchoolCodeData(**data)
    school_code_info_list = formate_data.data.values()
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        # 并行地处理每个 school_code_info 信息
        executor.map(get_ont_school_logo, school_code_info_list)


def main():
    init()


if __name__ == "__main__":
    main()
