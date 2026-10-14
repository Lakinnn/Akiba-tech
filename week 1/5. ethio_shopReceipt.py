print("+----------WELCOME TO OUR SHOP------------+\n")
name = str(input("Enter your name: "))
product = input("Enter product (separated with space): ").split()
price =input("Enter price (separated with space): ").split()
quant =input("Enter quantity (separated with space): ").split()


print ("\n============")
print ("RECEIPT")
print ("============\n")
 
print ("Customer: ",name.title(),"\n")

print(f"{'Product':<15} {'Price (ETB)':<12} {'Qty':<8} {'Total':<10}") 
print("-" * 50) 

grand_total = 0.0

for prod, p_str, q_str in zip(product, price, quant):
	price = float(p_str) 
	quantity = int(q_str) 
	item_total = price * quantity
	grand_total += item_total
	
	print(f"{prod:<15} {price:<12.2f} {quantity:<8} {item_total:<10.2f}") 
print("-" * 50) 
print(f"Total: {grand_total:.2f} ETB")
