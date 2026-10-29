print("CAMPUS EVENT FINANCIAL PLANNING") 
participants = int(input("Enter number of participants: ")) 
registration_fee = float(input("Enter registration fee per participant: ")) 
sponsorship = float(input("Enter sponsorship amount: ")) 
budget = float(input("Enter allocated budget: ")) 
venue = float(input("Enter venue expenses: ")) 
food = float(input("Enter food expenses: ")) 
decoration = float(input("Enter decoration expenses: ")) 
other = float(input("Enter other expenses: ")) 
if (participants <= 0 or registration_fee < 0 
or sponsorship < 0 or budget < 0 
or venue < 0 or food < 0 
or decoration < 0 or other < 0): 
    print("Invalid input. Check all entered values.") 
else: 
    registration_income = participants * registration_fee 
total_income = registration_income + sponsorship 
total_expenses = venue + food + decoration + other 
balance = total_income - total_expenses 
print("\n--- EVENT FINANCIAL REPORT ---") 
print("Registration Income: Rs.", round(registration_income, 2)) 
print("Sponsorship Income: Rs.", round(sponsorship, 2)) 
print("Total Income: Rs.", round(total_income, 2)) 
print("Total Expenses: Rs.", round(total_expenses, 2)) 
print("Allocated Budget: Rs.", round(budget, 2)) 
if balance > 0: 
    print("Profit: Rs.", round(balance, 2)) 
elif balance < 0: 
    print("Loss: Rs.", round(-balance, 2)) 
else: 
    print("Break-even: No profit, no loss.") 
if total_expenses > budget: 
    print("Budget exceeded by Rs.", 
round(total_expenses - budget, 2)) 
else: 
    print("Event expenses are within budget.") 
print("Unused budget: Rs.", 
round(budget - total_expenses, 2))