print ("=====Employee Information=====")

name = input("Enter full name: ")
salary = float(input("Enter your basic salary: "))
transport = float(input("Enter transport allowance: "))
food = float(input("Enter your food allowance: "))

gross = salary + transport + food

print ("="*25)
print("Employee Payslip")
print ("="*25,"\n")

print (f"Employee: ", name,"\n")

print (f"Basic Salary: ",salary, "ETB")
print (f"Transport Allowance: ", transport, "ETB")
print (f"Food Allowance: ", food, "ETB\n")

print ("-"*25)
print (f"Gross Salary: ", gross, "ETB")