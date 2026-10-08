print ("\t==== Prime Number Checker ====")

#  A prime number is a number greater than 1 that can only be divided exactly by 1 and itself.

num = int(input("Enter a number: "))

if num <= 1:
    print("The number is not a prime.")
elif num == 2:
    print("The number is prime.")
elif num % 2 == 0:
    print("The number is not a prime.")
else:
    prime = True
    
   # Since we already checked 'num % 2 == 0' above, we know the number is odd. 
   
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            prime = False
            break
   # Stepping by 2 lets us skip 4, 6, 8, etc., cutting our work in half.
            
    if prime:
        print("The number is prime.")
    else:
        print("The number is not a prime.")
