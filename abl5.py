units = int(input("Enter number of units produced: ")) 
if units <= 0: 
    print("Units must be greater than zero.") 
else: 
    raw_material = float(input("Enter raw material cost: ")) 
labour = float(input("Enter labour cost: ")) 
overhead = float(input("Enter overhead cost: ")) 
selling_price = float(input("Enter selling price per unit: ")) 
if raw_material < 0 or labour < 0 or overhead < 0 or selling_price < 0: 
    print("Costs and selling price cannot be negative.") 
else: 
    total_cost = raw_material + labour + overhead 
cost_per_unit = total_cost / units 
revenue = units * selling_price 
print("\n--- Manufacturing Report ---") 
print("Total Manufacturing Cost:", total_cost) 
print("Cost Per Unit:", round(cost_per_unit, 2)) 
print("Total Sales Revenue:", revenue) 
if revenue > total_cost: 
    profit = revenue - total_cost 
    print("Profit:", round(profit, 2)) 
elif revenue < total_cost: 
    loss = total_cost - revenue 
    print("Loss:", round(loss, 2)) 
else: 
    print("Break-even: No profit, no loss.")