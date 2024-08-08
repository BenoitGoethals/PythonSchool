class Person:
    max_persons = 1000

    def __init__(self, name, for_name, adress=None):
        self._name = name
        self._forName = for_name
        self._adress = adress

    def __str__(self):
        return self._name + self._forName

    def say_hello(self):
        print("Hello " + self._name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newname):
        self._name = newname


class Employee(Person):
    max_persons = 100

    def __init__(self, name, for_name, adress=None, phone=None):
        super().__init__(name, for_name, adress)
        self.__phone = phone

    def __str__(self):
        return self._name + self._forName + self.__phone

    def say_hello(self):
        print("Hello " + self._name)
