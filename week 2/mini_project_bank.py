print("#"* 45, "\n\t\tMINI PROJECT \n           BANK ACCOUNT SYSTEM\n","#"*45)

print("Welcome to Akiba Bank!\n")
Pin = 1234
balance = 1000
attempt = transaction = 0
max = 3
user = False

while attempt < max:
	pin= int(input("Please enter your PIN: "))
	
	if pin == Pin:
		print("Correct PIN.Your are in.")
		user = True
		break

	else:
			attempt +=1
			remain = max - attempt
			if remain >0:
				print("Incorrect PIN!\n  Attempt remaining: ",remain)
			else:
				print("-"*25,"\nToo many incorrect attempts.\nYour account is locked!\n")
				break
			
while user:
	print("-"*30,"\n\t","====AKIBA BANK====")
	print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Transaction made\n5. Exit\n","-"*30,"\n")
	choice= int(input("Choose an option: "))
	
	if choice==1:
		print("Your current balance is: ",balance,"Birr")
	
	elif choice==2:
		deposit = float(input("Enter deposit amount: "))
		if deposit >= 0:
			balance += deposit
			transaction +=1
			print("-"*20,"\nDeposit successful! \n  Your new balance is: ",balance,"Birr")
		else:
			print("Enter positive amount.")
		
	elif choice==3:
			withdraw = float(input("Enter withdrawal amount: "))
			if withdraw <= balance:
				balance -= withdraw
				transaction +=1
				print("Withdrawal successful! \n  Your new balance is: ",balance,"Birr")
			else:
				print("You have insufficient balance! Try again.")
				
	elif choice==4:
		print("Transactions made: " ,transaction)
		
		
	
	elif choice==5:
				print("Thank you for using Akiba Bank!\n\tGoodbye!")
				break
	else:
		print("Please choose a valid option.")