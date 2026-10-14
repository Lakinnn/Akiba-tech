print("#"*5,"NUMBER ANALYZER","#"*5)

nums= [ ]
print("Enter 10 numbers: ")
even = odd = sum= avg= 0

for i in range(10):
	num = int(input(f"Number {i+1}: "))
	nums.append(num)
	
	large = max(nums)
	small = min(nums)
	
	sum += num
	avg = sum/10
	    	
	if num % 2==0:
	    	even +=1
	else:
		odd +=1
	
		
print ("The largest number is ",large)
print ("The smallest number is ", small)
print("Sum = ",sum)
print("Average = ",avg)
print ("Total even numbers: ",even)
print("Total odd numbers: ",odd)