a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print('''Choose an operater: 
      1.Addition
      2.Subraction
      3.Multiplication
      4.Division''')
oper1 = int(input("Enter your choice(1,2,3,4): "))
match oper1:
    case 1:
        print(f"The sum of {a} and {b} is {a + b}")
    case 2:
        print(f"The sub of {a} and {b} is {a - b}")
    case 3:
        print(f"The mul of {a} and {b} is {a * b}")
    case 4:
        print(f"The div of {a} and {b} is {a / b}")
    case _:
        print("Please select the correct number")
    