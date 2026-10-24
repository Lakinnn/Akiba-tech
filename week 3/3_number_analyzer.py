print("=====Advanced Number Analyzer=====")

def is_prime(num):
	if num < 2:
		return False
	for i in range(2,num):
		if num%i == 0:
			return False
		return True
def get_divisor(num):
	divisors= []
	num = abs(num)

	if num == 0:
		return divisors

	for i in range(1, num+1):
		if num% i==0:
			divisors.append(i)
	return divisors

def sum_of_digits(num):
	num =abs(num)
	result= 0

	while num >0:
		digit = num%10
		result+= digit
		num= num//10
	return result

def reverse_num(num):
	num= abs(num)
	reverse = 0

	while num>0:
		digit= num%10
		reverse= reverse*10 + digit
		num= num//10
	return reverse

def analyze_number(num):
	if num%2== 0:
		even_or_odd= "Even"
	else:
		even_or_odd= "Odd"

	prime= is_prime(num)
	sum_digit = sum_of_digits(num)
	reversed = reverse_num(num)
	divisors= get_divisor(num)

	print("\n","==== Results ====","\n","-"*30)

	print("Number: ",num)
	print("Is it prime: ",prime)
	print("Even or Odd: ",even_or_odd)
	print("Reversed order: ",reversed)
	print("Divisors list: ",divisors)
	print("Sum of digits: ",sum_digit)
	print("-"*35)

number= int(input("Enter a number to be analyzed: "))
analyze_number(number)

