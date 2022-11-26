cost_price = int(input("Enter a Cost Price: "))
selling_price = int(input("Enter a Selling Price: "))
if (cost_price > selling_price):
	amount = cost_price - selling_price
	print("Amount Loss: " + str(amount))
elif (cost_price < selling_price):
	amount = selling_price - cost_price
	print("You can booked your profit amount: " + str(amount))
else:
	 print("No Profit and No Loss!")