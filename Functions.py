#Functons
def calculate_discount(original_price,discount_percentage=10):
    discounted_price = original_price - (original_price*discount_percentage/100)
    return discounted_price
#Function with default parameters
price = calculate_discount(100)
print("Discounted price = ",price)

