class Employee:
    pass

john = Employee()

john.name = 'jd'
john.dept = 'it'
john.salary = 1000





class Bag:
    def __init__(self):
        self.data = []

    def add(self,x):
        self.data.append(x)

    def twice(self,x):
        self.add(x)
        self.add(x)

a = Bag()
a.add('zzz')
a.twice('qqq')

print(a.data)