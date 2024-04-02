import requests

from scheme.school_code import SchoolCodeData
from scheme.school_info import SchoolInfoData

headers = {
    "User-Agent": " Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3.1 Safari/605.1.15",
}


def get_school_code_list() -> dict:
    try:
        res = requests.get(
            "https://static-data.gaokao.cn/www/2.0/school/school_code.json"
        )
        return res.json()
    except Exception as e:
        print(f"Error occurred while fetching school code list: {e}")
        print(f"Response content: {res.content}")
        raise


def get_school_info(school_id: str) -> dict:
    try:
        res = requests.get(
            f"https://static-data.gaokao.cn/www/2.0/school/{school_id}/info.json"
        )
        return res.json()
    except Exception as e:
        print(
            f"Error occurred while fetching school info for school ID {school_id}: {e}"
        )
        print(f"Response content: {res.content}")
        raise


def get_school_special(school_id: str) -> dict:
    try:
        res = requests.get(
            f"https://static-data.gaokao.cn/www/2.0/school/{school_id}/pc_special.json"
        )
        return res.json()
    except Exception as e:
        print(
            f"Error occurred while fetching school special for school ID {school_id}: {e}"
        )
        print(f"Response content: {res.content}")
        raise


def get_special_info(special_id: str) -> dict:
    try:
        res = requests.get(
            f"https://static-data.gaokao.cn/www/2.0/special/{special_id}/pc_special_detail.json"
        )
        return res.json()
    except Exception as e:
        if(res.status_code==404):
            # 存在找不到的情况直接返回None跳过
            return None
        print(
            f"Error occurred while fetching special info for special ID {special_id}: {e}"
        )
        print(f"Response content: {res.content}")
        print(res.status_code)
        raise


# get_school_code_list()

# print(res.request.headers)
# data = res.json()
# print(data)
# print(len(data.data.item))
