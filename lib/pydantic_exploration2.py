from typing import Union, Literal
from pydantic import BaseModel, Field


class SubType1(BaseModel):
    mytype: str = Literal["subtype1"]


class SubType2(BaseModel):
    mytype: str = Literal["subtype2"]


class Model(BaseModel):
    renderer: Union[SubType1, SubType2] = Field(..., discriminator="mytype")
    other: str


d = Model(renderer={"mytype": "subtype1"}, other="a")
print(d)
