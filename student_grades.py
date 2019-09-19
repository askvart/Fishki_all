class Person:
    ''' Класс '''
    kaka = {}
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.data = []

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @age.setter
    def age(self,age):
        if age in range(1,100):
            self.__age = age
        else:
            print('age ERROR')

    def display_info(self):
        print(self.__name, self.__age)

    def hello(self):
        print('Hello world everybody!!!')

    def __repr__(self):
        return (f'Имячко:{self.__name} Возрасток:{self.__age}')

    def __str__(self):
        return ('Name:{} Age:{}'.format(self.__name,self.__age))


class Employee(Person):
    def __init__(self, name,age,company):
        Person.__init__(self,name,age)
        self.company = company

    def display_info(self):
        Person.display_info(self)
        print('Company:',self.company)

    def details(self,company):
        print('Товарищ:',self.name,self.age,'работает в компании',self.company)


class Student(Person):
    def __init__(self,name,age,university):
        Person.__init__(self,name,age)
        self.university = university

    def display_info(self):
        print('Студент:',self.name, 'учиться v Университет',self.university)


tom = Person('lJohn',18)
tom.hello()


