print ("="*5,"FIZZBUZZ Problem", "="*5)

start = int(input("Enter starting number: "))
end = int(input("Enter an ending number: "))

number = start
while number <= end:
	if number %3==0 and number % 5 ==0:
		print("FizzBuzz")
	elif number % 3 == 0:
		print("Fizz")
	elif number % 5 == 0:
		print("Buzz")
	else:
		print(number)
		
	number +=1