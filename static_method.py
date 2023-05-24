class MyClass:
    def __init__(self,value):
        self.value=value
        
    @staticmethod
    def get_highest(x,y):
        return max(x,y)
    


class Demo(MyClass):
    def __init__(self):
        pass
    

    
obj=MyClass(10)
print(obj.get_highest(1,2))
d=Demo()
print(d.get_highest(1,2))