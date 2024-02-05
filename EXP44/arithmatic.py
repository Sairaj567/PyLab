from random import choice


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        raise "division by zero is not possible"
    else:
        return num1 / num2


num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
choice = 1
while choice != 0:
    choice = int(input("Enter the choice: "))
    if choice == 1:
        print(add(num1, num2))
    elif choice == 2:
        print(sub(num1, num2))
    elif choice == 3:
        print(mul(num1, num2))
    elif choice == 4:
        print(div(num1, num2))
