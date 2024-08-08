from domain import Person, Employee

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  pers=Person("benoit","goethals")
  print(pers.say_hello())
  print(pers)
  pers.name="test"
  print(pers.name)
  print(pers)

  emplo=Employee("benoit","goethals",None,"0475981572")
  print(emplo)
  print(emplo.say_hello())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
