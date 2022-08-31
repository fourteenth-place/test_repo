from enum import Enum
from typing import Optional, List
from pydantic import BaseModel


class SomeOptsEnum(str, Enum):
    # poly: Polygon
    # line: Line
    poly = 'poly'


class ParentModel(BaseModel):
    # some_opts: Optional[List[SomeOpts]]
    fruit: SomeOptsEnum


data = {'so': 'poly'}

ParentModel(fruit='poly')

print(1)
