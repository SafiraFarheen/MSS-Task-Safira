#Advanced-Data Structure
#Creating a dictionary
customer_info = {"name":"Safira","age":19,"purchase_history":["Shoes","Watch","Wallet"]}
#retrieving and printing customer's name and second purchase
customer_name = customer_info["name"]
print("Customer's name:",customer_name)

if len(customer_info["purchase_history"])>=2:
    second_purchase = customer_info["purchase_history"][1]
    print("Second_purchase:",second_purchase)
else:
    print("Customer's purchase history is not long enough...")
