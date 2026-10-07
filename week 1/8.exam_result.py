print ("=====Student Information=====\n")

name = input("Enter full name: ")
PyScore = float(input("Enter your Python score: "))
engScore = float(input("Enter your English score: "))
mathScore = float(input("Enter your Mathematics score: "))

avrg = (PyScore + engScore + mathScore)/3

print ("$="*25)
print("\t\t STUDENT RESULT")
print ("$="*25,"\n")

print (f"Student: ", name,"\n")

print (f"Python:  ",PyScore)
print (f"English:  ", engScore)
print (f"Mathematics: ", mathScore)

print ("•"*25)
print (f"Average:  ", avrg)
