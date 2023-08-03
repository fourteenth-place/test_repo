from pydantic import BaseModel


class HazardAnalysis:
    param: dict = None
    extra_param: dict = None
    
    
    def do_something(self):
        print('doing something')


class CustomHazardAnalysis(BaseModel, HazardAnalysis):
    
    param: dict
    
    
data = {'param': {'a': 1}}
# data = {'param': 1}

inst = CustomHazardAnalysis(**data)

inst.do_something()
