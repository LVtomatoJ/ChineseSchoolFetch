from pydantic import BaseModel
from typing import Dict, List
from datetime import date, datetime


class SchoolInfo(BaseModel):
    school_id: str
    data_code: str
    name: str  # 大学名称
    belong: str  # 城市
    f985: str  # 是否985  2代表不是 1 代表是
    f211: str  # 是否211 同上
    create_date: str  # 建校时间
    is_fenxiao: str  # 是否分校
    update_time: datetime  # 更新时间
    short: str  # 简称 eg. "北工大,bjut,北京工业"
    ruanke_rank: str  # 软科排名
    level_name: str  # eg.普通本科
    type_name: str  # eg.理工类
    school_type_name: str  # eg. 普通本科  #FIXME 不知道为什么有两个type_name
    school_nature_name: str  # eg. 公办
    email: str  # 邮箱
    address: str  # 地址
    site: str  # 招生网站
    school_site: str  # 学校官网
    content: str  # 介绍
    province_name: str  # 省
    school_special_num: int  # 专业数量
    city_name: str  # 市
    town_name: str  # 区
    dual_class_name: str  # 如果是双一流这里会有双一流


class SchoolInfoData(BaseModel):
    code: str
    message: str
    data: SchoolInfo
