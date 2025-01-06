Num1 = float(input("Enter First Number Here : "))

Num2 = float(input("Enter Second Number Here : "))

operator = input("Enter operator(+, -, *, /) : ")

if operator == '+' :
    result = Num1 + Num2
    print(f"The Addition of the {Num1} and {Num2} is {result}")

elif operator == "-" :
    result = Num1 - Num2
    print(f"The Substraction of the {Num1} and {Num2} is {result}")

elif operator == "*" :
    result = Num1 * Num2
    print(f"The Multiplication of the {Num1} and {Num2} is {result}")

elif operator == "/" :
    result = Num1 / Num2
    print(f"The Division of the {Num1} and {Num2} is {result}")

else :
    print("Please Enter Appropriate Numbers and Oprator")
