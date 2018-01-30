import pprint


class Poli:

    #    def __init__(self, a: int=0, b: int=0):
    #        self.a: int = a
    #        self.b: int = b

    #    def __init__(self, name: str=0):
    #        self.name: str = name

    def __init__(self, a: int=0, b: int=0, name: str=''):
        self.a: int = a
        self.b: int = b
        self.name: str = name

    @classmethod
    def from_number(cls, a: int):
        return cls(a=a)

    @classmethod
    def from_numbers(cls, a: int, b: int):
        return cls(a=a, b=b)

    @classmethod
    def from_name(cls, name: str):
        return cls(name=name)

    def do_something(self, a: int):
        print(" %d+%d=%d" %(self.a, a, self.a + a))

 #   def do_something(self, a: str):
 #       print("%s %s" %(a, self.name))

p1 = Poli.from_number(12)

print(p1.__dict__)

p2 = Poli.from_name(name="Ala ma kota")

print(p2.__dict__)


p1.do_something(14.234)
#p2.do_something("Hello")