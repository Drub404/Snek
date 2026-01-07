import random

def discountCalculation():
    try:
        full_price = int(input("How much does the article cost?: "))
        discount = int(input("How much % discount is there?: "))
    except ValueError:
        full_price = random.randint(1, 1000)
        discount = random.randint(1, 100)
        print("That is not a valid input! Using random assigned values instead...")
    
    calculated_discount = full_price - (full_price / 100 * discount)
    print(f"You should've paid €{full_price}, but due to a discount of %{discount} the article now costs: {calculated_discount}")


discountCalculation()
