class parent():
    a = 10
    b = 12
    
    def __init__(self,a):
        print("i am cons from parent class",a)

class child(parent):
    a = 11111
    b = 1
    def __init__(self,c):
        print("i am cons from child")
        
        super().__init__(1212)
        
obj = child(12) 























class person():
    def __init__(self,name):
        self.name = name
        
    def show_name(self):
        return self.name
    
class student(person):
    def __init__(self, name,student_id):
        self.student_id = student_id
        self.name = name
        super().__init__(name)
    
    def show_detail(self):
        return self.name, self.student_id
    
class Test(student):
    def hello(self):
        print("this is hello world")   
obj = Test("amit","1234")
print(obj.show_name())  
print(obj.show_detail())                    
obj.hello()         