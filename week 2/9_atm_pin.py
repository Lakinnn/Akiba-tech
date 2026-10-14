print ("="*5,"ATM PIN SYSTEM", "="*5)

correct_pin = 1234
max_attempt = 3
attempt = 0

while attempt < max_attempt:
	pin= int(input("Enter your 4 digit PIN: "))
	attempt += 1
	
	if pin == correct_pin:
		print("Correct PIN. You are In.")
		break
	else:
		remain = max_attempt - attempt 
		
		if remain > 0:
			print("Incorrect PIN. Remaining attempts: ",remain)
		else:
			print("Incorrect PIN. PIN is locked")