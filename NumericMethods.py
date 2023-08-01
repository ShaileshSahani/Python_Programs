class GetInput:
    def __init__(self):
        print("Enter The Coefficient values:")
        self.a = int(input("Enter The First Coefficient:"))
        self.b = int(input("Enter The Second Coefficient:"))
        self.c = int(input("Enter The Third Coefficient:"))
        self.iterator = int(input("Enter The Number of Iterations:"))
    def GetValue(self):
        self.dic = {}
        for i in range(-self.iterator,self.iterator+1):
            self.result = (self.a * i *i) + (self.b * i) + self.c
            if self.result == 0:
                print("\n\nRoot For the given Equation is:",i)
                self.dic[i] = self.result
                break
            else:self.dic[i] = self.result
        else:
            print("No solution of this Root try More Iterations")
        x = input("\nSee Other Iteration results(y/n):")
        if x == "y":
            for y in self.dic:
                print(y,":",self.dic[y])
        else:
            print("Fine")
while True:
    object = GetInput()
    object.GetValue()
    z = input('Go Further For More equation/more iterations:')
    if z == "y":
        pass
    else:
        print("You Exit")