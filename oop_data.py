class Computer():
    # called when creating instance
    def __init__(self, color = 'black'):
        self.color = color
    def turnOn(self):
        print("On...")

lenovo = Computer() # creating instance
mac = Computer('blue') # creating instance with color blue
lenovo.turnOn()
lenovo.color = 'red'
print(lenovo.color)
print(mac.color)

# create Person class
# func: sayHello()
# data: name , __init__  parameter
# data: age , __init__  parameter
# *etgar: sayMyName() - print
#       current person name
# create 2 persons
# set name default value 'Incognito'
class Person():
    def __init__(self,
                 time,
                 name = 'Incognito'
                 , age = 0):
        self.__time = time
        self.name = name
        self.age = age
    def sayMyName(self):
        print(f'name = {self.name}')
    def getTime(self):
        return self.__time + ' GMT+3'

dana = Person('13:00', 'Dana', 33)
print(dana.name, dana.age)
dana.sayMyName()
print(dana.getTime())



