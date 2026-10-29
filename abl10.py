balance = 5000.0 
while True: 
    print("\n--- ATM MENU ---") 
print("1. Balance Enquiry") 
print("2. Deposit Money") 
print("3. Withdraw Money") 
print("4. Exit") 
choice = input("Enter your choice: ") 
if choice == "1": 
    print("Available Balance: Rs.", round(balance, 2)) 
elif choice == "2": 
    amount = float(input("Enter deposit amount: Rs. ")) 
if amount <= 0: 
    print("Invalid amount. Enter a positive value.") 
else: 
    balance += amount 
print("Deposit successful.") 
print("Updated Balance: Rs.", round(balance, 2)) 
if amount <= 0: 
    print("Invalid amount. Enter a positive value.") 
elif amount > balance: 
    print("Insufficient balance.") 
else: 
    balance -= amount 
    print("Withdrawal successful.") 
    print("Updated Balance: Rs.", round(balance, 2)) 
print("Invalid choice. Please try again.")