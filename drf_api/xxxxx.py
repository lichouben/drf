from typing import Any


class foo(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age

        
    def show(self):
        return 456
    
    # 针对不存在的成员
    def __getattr__(self,item):
        print("----->",item)
        return 999
    
    # 会抢先执行
    def __getattribute__(self, item):
        print("----->",item)
        return 123
        
obj = foo("李嘉骏",20)
print(obj.name)
print(obj.show())
# print(obj.name)