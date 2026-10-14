print ("="*5,"NUMBER GUESSING GAME", "="*5)

secret_num = 7
attempt = 0
max_attempts = 5

while attempt < max_attempts:
	guess = int(input("Guess the number: "))
	attempt +=1
	
	if guess == secret_num:
		print("Congratulations! You guessed the number in",attempt ,"attempts")
		break
		
	elif guess < secret_num:
		print("Too low. Try again.")
	else:
			print("Too high. Try again")
		
else:
		print("Game over!")
		print("The secret number was ", secret_num)