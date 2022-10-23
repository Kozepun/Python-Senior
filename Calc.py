def Calc():
    Number1 = int(input("1 Number -> "))
    Number2 = int(input("2 Number -> "))
    def Choise():
        print("+\n-\n*\n/\nChange Num\n Exit")
        Ans = input("Choose -> ")
        if (Ans == "+"):
            print(Number2 + Number1)
            Choise()
        elif (Ans == "-"):
            print(Number2 - Number1)
            Choise()
        elif (Ans == "*"):
            print(Number2 * Number1)
            Choise()
        elif (Ans == "/"):
            print(Number1 / Number2)
            Choise()
        elif (Ans.lower() == "change num"):
            Calc()
        elif (Ans.lower() == "exit"):
            print("Logged Out")
        else:
            print("Answer Is Invalid")
            Choise()
    Choise()
Calc()