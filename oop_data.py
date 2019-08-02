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
# *etgar: sayMyName() - print
#       current person name
# create 2 persons
# set name default value 'Incognito'
