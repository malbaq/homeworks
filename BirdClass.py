class Bird:
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        print(f"{self.name} bird can fly")
    
    def walk(self):
        print(f"{self.name} bird can walk")

    def eat(self):
        print(f"It eats various things")
    
    def __str__(self):
        return f"{self.name} can walk and fly"

class FlyingBird(Bird):
    def eat(self):
        print(f"It eats mostly insects and small animals")

class NonFlyingBird(Bird):
    def fly(self):
        raise AttributeError(f"{self.name} bird can't fly")
    
    def eat(self):
        print(f"It eats mostly seeds and fruits")

class SwimmingBird(Bird):
    def fly(self):
        raise AttributeError(f"{self.name} bird can't fly")

    def walk(self):
        print(f"{self.name} bird can walk but not very well")
    
    def eat(self):
        print(f"It eats fish")

class SuperBird(FlyingBird, SwimmingBird):
    def __str__(self):
        return f"{self.name} can walk, fly, and swim"


b = Bird("Any")
b.walk()  # Any bird can walk
b.fly()   # Any bird can fly
b.eat()   # It eats various things
print(str(b))  # Any can walk and fly

p = SwimmingBird("Penguin")
p.walk()  # Penguin bird can walk
p.swim()  # Penguin bird can swim
p.fly()   # AttributeError: 'Penguin' object has no attribute 'fly'
p.eat()   # It eats fish

c = FlyingBird("Canary")
print(str(c))  # Canary can walk and fly
c.walk()  # Canary bird can walk
c.fly()   # Canary bird can fly
c.eat()   # It eats mostly insects and small animals

s = SeaGull("Gull")
print(str(s))  # Gull can walk, fly, and swim
s.walk()  # Gull bird can walk
s.fly()   # Gull bird can fly
s.swim()  # Gull bird can swim
s.eat()   # It eats fish

sb = SuperBird("Super")
print(str(sb))  # Super can walk, fly, and swim
sb.walk()  # Super bird can walk but not very well
sb.fly()   # Super bird can fly
sb.swim()  # Super bird can swim
sb.eat()   # It eats mostly insects and small animals