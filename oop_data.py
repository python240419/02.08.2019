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
