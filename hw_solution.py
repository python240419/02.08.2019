# fucntion
def myPrint():
    pass

class Computer():
    def __init__(self):
        print("new computer was born")
    def turnOn(self):
        print("turning on...")
        self.__secretMethod()
    def __secretMethod(self):
        print("shhhhhh")

print('hello')   # function
lenovo = Computer()
lenovo.turnOn() # method

def sortToTuple(*args):
    return tuple(sorted(args))

print(sortToTuple(7,2,-3, 100))

def compareD(d, **kwargs):
    d == kwargs

compareD({'name' : 'itay'},
         name = 'itay')

#{ name : 'itay'} == {name : 'itay'}

class SuperHero():
    def __init__(self):
        print("new hero was born")
    def fly(self):
        print("flying....")
    def climb(self):
        print("climbing....")
    def forceSpeed(self):
        print("force Speed....")
        self.__heroResting()
    def __heroResting(self):
        print("resting....")
superMan = SuperHero()
superMan.fly()
superMan.__heroResting()
superMan.climb()
superMan.forceSpeed()
