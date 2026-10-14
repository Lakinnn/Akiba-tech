print ("="*5,"COUNT NUMBERS Problem", "="*5)

N= int(input("Enter a positive number: "))

even= 0 
odd= 0
sum = 0

for i in range (1,N+1):
	
	sum += i
	if i %2==0:
		even +=1
	else:
		odd +=1
		
print("Total even numbers: ",even)
print ("Total odd numbers: ",odd)
print("Sum= ",sum)