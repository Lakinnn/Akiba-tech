print("==== Largest og three ====" )
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2 == num3:
    print("All three numbers are equal.")
elif num1 == num2 and num1 > num3:
    print("The first and second numbers are the largest.")
elif num1 == num3 and num1 > num2:
    print("The first and third numbers are the largest.")
elif num2 == num3 and num2 > num1:
    print("The second and third numbers are the largest.")
elif num1 > num2 and num1 > num3:
    print(f"The first number, {num1} is the largest.")
elif num2 > num1 and num2 > num3:
    print(f"The second number, {num2} is the largest.")
else:
    print(f"The third number, {num3} is the largest.")
