class Rectangle():

    def input(self):
        self.length = int(input("length: "))
        self.breath = int(input("breadth: "))
    def output(self):
        print(self.length*self.breath)

x = Rectangle()
x.input()
x.output()