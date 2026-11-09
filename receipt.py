print("Hello, welcome to CATUC Restaurant")
num_items = int(input("Please enter how many items purchased: "))

items_name = {}
items_quantity = []
items_price = []
items_cost = []

for item in range(1, num_items + 1):
    print(f"Item{item}")
    name = input("Please enter item name: ")
    quantity = int(input("QUANTITY: "))
    price = float(input(f"PRICE {item}: "))

    cost = quantity * price

    items_name[item] = name
    items_quantity.append(quantity)
    items_price.append(price)
    items_cost.append(cost)

items_cost_total = sum(items_cost)
if items_cost_total > 10000:
    discount = 0.30 * items_cost_total
    total_cost = items_cost_total - discount
    print(f"Total purchase = {total_cost} frs\nThank you for coming!")
elif (len(items_cost) > 5) and (items_cost_total > 4000):
    discount = 0.15 * items_cost_total
    total_cost = items_cost_total - discount
    print(f"Total purchase = {total_cost} frs\nThank you for coming!")
elif items_cost_total > 5000:
    discount = 0.01 * items_cost_total
    total_cost = items_cost_total - discount
    print(f"Total purchase = {total_cost} frs\nThank you for coming")
else:
    discount = 0
    total_cost = items_cost_total - discount
print("\nS/N Description Quantity Unite Price Total Price")

for item in range(1, num_items+1):
    print(item,items_name[item], items_quantity[item-1],
          items_price[item-1], items_cost[item-1])
    
print("\nTotal Expenditure = ", items_cost_total, "frs")
print("\nDiscount= ", discount, "frs")
print("\nTotal Amount = ", total_cost, "frs")
print(f"Total purchase = {total_cost} frs\nThank you for coming")
