""""
Requisitions_total
Author Charanpreet Singh
"""
def Requisitions_total():
    total_amount=0.0
    while True:
        price_input=input(": (or type 'finish' to end):")

        if price_input.lower()=='finish':
            break

        try:
            price=float(input(f"$ '{price_input}':"))
            total_amount+=price
        except ValueError:
            print("Invalid input, Please enter a value number.")

    print(f"${total_amount:.2f}")
    return total_amount
Requisitions_total()

