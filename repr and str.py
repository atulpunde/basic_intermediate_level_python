class A(object):
    a = 9
    @staticmethod
    def disp():
        print("Im In display")

    def __repr__(self):
        return "This is returned1"

    def __str__(self):
        return "This is returned2"

a = A()
A.disp()
print([a])
print(a)
print(a.__class__.__name__)
print(a.__dict__)
