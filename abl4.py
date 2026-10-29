print("RETAIL BILLING SYSTEM") 
name = input("Enter customer name: ") 
amount = float(input("Enter total purchase amount: Rs. ")) 
if amount < 0: 
    print("Invalid purchase amount") 
else: 
    membership = input( 
"Is the customer a member? (yes/no): " 
).strip().lower() 
if membership not in ["yes", "no"]: 
    print("Invalid membership status") 
else: 
# Calculate purchase discount 
    if amount >= 5000: 
        purchase_discount = amount * 0.10 
    elif amount >= 2000: 
        purchase_discount = amount * 0.05 
    else: 
        purchase_discount = 0 
# Amount after purchase discount 
remaining = amount - purchase_discount 
# Calculate membership discount 
if membership == "yes": 
    member_discount = remaining * 0.05 
else: 
    member_discount = 0 
total_discount = purchase_discount + member_discount 
final_bill = amount - total_discount 
# Display the bill 
print("\n----- RETAIL BILL -----") 
print("Customer Name:", name) 
print("Purchase Amount: Rs.", round(amount, 2)) 
print("Purchase Discount: Rs.", 
round(purchase_discount, 2)) 
print("Membership Discount: Rs.", 
round(member_discount, 2)) 
print("Total Savings: Rs.", 
round(total_discount, 2)) 
print("Final Bill: Rs.", round(final_bill, 2)) 