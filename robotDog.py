class Robot_Dog:
    def __init__(self, name, bread):
        self.name = name
        self.bread = bread

    def bark(self):
        print('Woof Woof!')

myDog = Robot_Dog('Johny', 'Scotish')

print(myDog.name)
print(myDog.bread)
myDog.bark()

