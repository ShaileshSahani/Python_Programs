class Argument:
    @classmethod
    def add(cls, *args):
        s = 0
        for i in args:
            s += i
        print(s)


Argument.add(1, 2, 3, 4)
Argument.add(1, 2, 3)
