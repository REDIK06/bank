class Bank:
    def __init__(self, name, age, money, key):
        self._name = name
        self._age = age
        self.__money = money
        self.__key = key

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key


class Storage(Bank):
    @property
    def money(self):
        return self.get_money()

    @money.setter
    def money(self, value):
        self.set_money(value)

    @property
    def key(self):
        return self.get_key()

    @key.setter
    def key(self, value):
        self.set_key(value)


class Data(Storage):
    @property
    def name(self):
        return self.get_name()

    @name.setter
    def name(self, value):
        self.set_name(value)

    @property
    def age(self):
        return self.get_age()

    @age.setter
    def age(self, value):
        self.set_age(value)


instance = Data("Стол", 98, 1, "ножка")

print(instance.name)
print(instance.age)
print(instance.money)
print(instance.key)

instance.name = "Крипта"
instance.age = 14
instance.money = 43047
instance.key = "bitcoin"

print(instance.name)
print(instance.age)
print(instance.money)
print(instance.key)