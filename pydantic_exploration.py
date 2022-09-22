from enum import Enum
from typing import Dict, Optional, List
from pydantic import BaseModel


# class SomeOptsEnum(str, Enum):
    # poly: Polygon
    # line: Line
    # poly = 'poly'

class MyObj(BaseModel):
    something: str

class ObjWrap(BaseModel):
    arbstring: MyObj
    
class ParentModel(BaseModel):
    # some_opts: Optional[List[SomeOpts]]
    fruit: ObjWrap

sd = {'something': 'test'}
data = {'fruit': {'arbstring': sd}}

f = MyObj.parse_obj(sd)
d = ParentModel.parse_obj(data)

print(d)
