a = "amit"
print(len(a))

a = [1,2,3,4,5]

print(len(a))

a = {
    "name":"hari",
    "address":"kathmandu"
}

print(len(a))


class car():
    def test(self):
        print("move")
        

class plane():   
    def test (self):
        print("fly")
        

obj1 = car()
obj2 = plane()

for i in (obj1, obj2):
    print(i.test)
    