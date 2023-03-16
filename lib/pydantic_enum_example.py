from enum import Enum
from typing import List

from pydantic import BaseModel


class Tool(BaseModel):
    name: str
    kind: str


class FruitEnum(str, Enum):
    pear = "pear"
    banana = "banana"


class ToolEnum(Enum):
    spanner = Tool
    wrench = Tool


class CookingModel(BaseModel):
    fruit: FruitEnum = FruitEnum.pear
    # tool: ToolEnum = ToolEnum.spanner
    tools: List[Tool]


d = {
    "fruit": "pear",
    "tools": [{"name": "wrench", "kind": "a"}, {"name": "hammer", "kind": "b"}],
}


c = CookingModel(**d)
print(c)
