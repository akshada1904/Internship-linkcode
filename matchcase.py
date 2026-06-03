print("calculator\n1.add\n2.sub\n3.mul\n4.div\n5.exit\n")
choice=int(input("enter your choice"))

match choice:
    case 1:
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        print(f"add of {num1} and {num2} is {num1+num2}")

    case 2:
         num1=int(input("enter num1"))
         num2=int(input("enter num2"))
         print(f"sub of {num1} and {num2} is {num1-num2}")

    case 3:
         num1=int(input("enter num1"))
         num2=int(input("enter num2"))
         print(f"mul of {num1} and {num2} is {num1*num2}")

    case 4:
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        print(f"div of {num1} and {num2} is {num1/num2}")

    case _ :
          print("invalid input")


