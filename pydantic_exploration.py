from enum import Enum
from typing import Dict, Optional, List, Union, Literal
from pydantic import BaseModel, Field


class SubType1(BaseModel):
    mytype: Literal['subtype1']


class SubType2(BaseModel):
    mytype: Literal['subtype2']


class Model(BaseModel):
    renderer: Union[SubType1, SubType2] = Field(..., discriminator='mytype')
    other: str


m = Model(renderer={'mytype': 'subtype2'}, other='a')
print(m)
