print ("====USER INFORMATION====\n")

name = input("Enter your name: ")
weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(m): "))

bmi = weight/(height * height)

print("\n","$"*30)
print ("\t BMI REPORT")
print("$"*30,"\n")

print ("Name: ", name)
print ("Weight: ",weight)
print ("Height: ",height)

print ("-"*20)
print ("BMI: ",bmi)



