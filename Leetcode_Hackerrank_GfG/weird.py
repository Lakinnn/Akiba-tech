n=int(input("enter number:"))

if n%2!=0:
    print("Weird")
elif n%2!=0 and n>=2 and n<=5:
    print("Not weird")
elif n>=6 and n<=20:
    print("Weird")
else:
    print("Not weird")
