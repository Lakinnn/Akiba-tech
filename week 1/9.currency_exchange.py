print ("=====CURRENCY EXCHANGE DESK=====\n")

amount = float(input("Enter USD amount: "))
#bonus
exg_rate = float(input("Enter Exchange rate: "))
rate =  150 

ETB_amount = amount * exg_rate

print ("\n","="*35)
print("\tCURRENCY EXCHANGE")
print ("="*35,"\n")


print (f"USD Amount: ",amount)
print (f"Exchange Rate: 1 USD = ", exg_rate,"ETB")

print("-"*20)
print (f"ETB Amount", ETB_amount,"ETB")
print("-"*20)
