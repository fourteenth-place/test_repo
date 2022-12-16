class MyClass:
    _my_att: dict = None
    
    @property
    def my_att(self):
        if self._my_att is None:
            self._my_att = {}
        return self._my_att
    
    @my_att.setter
    def my_att(self, value: dict):
        self._my_att = value


c = MyClass()
c.my_att = {1: 1}
print(c.my_att)
c.my_att[1] = 'a'
print(c.my_att)