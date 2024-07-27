Welcome = print("Welcome to your session of text-based 4-operation calculator, user.")
four_operations = ["Addition", "Subtraction", "Multiplication", "Division"]
choosing_operations = input("Choose your mode: \n")

#Addition = four_operations[0]
#Subtraction = four_operations[1]
#Multiplication = four_operations[2]
#Division = four_operations[3]

if choosing_operations == four_operations[0]:
    add_1st_num = (input("Enter your first number: \n"))
    add_2nd_num = (input("Enter your second number: \n"))
    total = print(int(add_1st_num), "+", int(add_2nd_num), "=", int(add_1st_num) + int(add_2nd_num))
    
elif choosing_operations == four_operations[1]:
    sub_1st_num = (input("Enter the number that is to be subtracted from: \n"))
    sub_2nd_num = (input("Enter the number that you will subtract: \n"))
    difference = print(int(sub_1st_num), "-", int(sub_2nd_num), "=", int(sub_1st_num) - int(sub_2nd_num))

elif choosing_operations == four_operations[2]:
    multiplicand = (input("Enter the multiplicand: \n"))
    multiplier = (input("Enter the multiplier: \n"))
    product = print(int(multiplicand), "×", int(multiplier), "=", int(multiplicand) * int(multiplier))

elif choosing_operations == four_operations[3]:
    dividend = (input("Enter the dividend: \n"))
    divisor = (input("Enter the divisor: \n"))
    quotient = print(int(dividend), "÷", int(divisor), "=", int(dividend) / int(divisor))

else:
    print("Please enter a valid operation name.")


    
