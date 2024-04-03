from pydantic import BaseModel, Field, validator
from typing import Dict, List, Optional, Union


class SchoolSpecial(BaseModel):
    id: str
    code: str  # 专业代码 080902
    level2_name: str  # 工学
    level3_name: str  # 计算机
    limit_year: str  # 四年
    special_id: str
    special_name: str  # 软件工程
    type_name: str  # 本科
    level3_name: str  # 分类 机械类


class SchoolSpecialInfo(BaseModel):
    # 这里key是1的时候是全部的 并且有时候不存在1
    special_detail: Dict[int, Union[List[SchoolSpecial], List[Dict], str]]


class SchoolSpecialData(BaseModel):
    code: str
    message: str
    data: SchoolSpecialInfo
