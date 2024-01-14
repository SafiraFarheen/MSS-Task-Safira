#Control flow

mixed_data = [7,1.8,"Python",34,56.5,"Data",False,"Java"]

def calculate_discount(original_price,discount_percentage=10):
    discounted_price = original_price - (original_price*discount_percentage/100)
    return discounted_price
discounted_price=calculate_discount(100)
if discounted_price<50:
    print("Low cost Item")
elif 50<=discounted_price<=100:
    print("Moderate cost Item")
else:
    print("High cost Item")

#loop to iterate through mixed data
for element in mixed_data:
    print("Element = ",element)
    print("DataType = ",type(element))
