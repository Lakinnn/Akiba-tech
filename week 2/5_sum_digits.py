print("="*5,"SUM OF DIGITS","="*5)

num =int(input("Enter a number: "))
num =abs(num)
result= 0
while num > 0:
	digit =num%10
	result += digit
	num =num//10
print("Result = ",result)