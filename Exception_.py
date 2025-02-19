class Division:

    @staticmethod
    def div():
        try:
            a = int(input("Enter a number1 :"))
            b = int(input("Enter a number2 :"))
            try:
                print(f"The division is : {a / b}")
            except ZeroDivisionError:
                print("Zero")
        except ValueError:
            print(f"Not a number ")


Division.div()
