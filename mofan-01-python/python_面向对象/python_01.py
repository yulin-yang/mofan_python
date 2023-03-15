class Person:
    # 定义普通属性
    name = 'moss',
    age = 22,
    sex = '',
    _weight = ''
    # 私有变量，实例无法访问，只能通过内部方法访问
    __money = ' '

    def __init__(self, name, age, sex, weight, money):
        self.name = name,
        self.age = age,
        self.sex = sex,
        self._weight = weight
        self.__money = money

    def print(self):
        print('name:', self.name, 'age:', self.age, 'sex:', self.sex, self._weight, self.__money)

    def print_money(self):
        print(self.__money)


if __name__ == "__main__":
    tom = Person('tom', 23, 'man', 120, 5000)

    print(tom._weight)
    Person.print_money(tom)
