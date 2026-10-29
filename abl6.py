budget = float(input("Enter travel budget in INR: ")) 
usd = float(input("Enter expense in USD: ")) 
usd_rate = float(input("Enter USD to INR exchange rate: ")) 
eur = float(input("Enter expense in EUR: ")) 
eur_rate = float(input("Enter EUR to INR exchange rate: ")) 
gbp = float(input("Enter expense in GBP: ")) 
gbp_rate = float(input("Enter GBP to INR exchange rate: ")) 
if (budget < 0 or usd < 0 or eur < 0 or gbp < 0 
or usd_rate <= 0 or eur_rate <= 0 or gbp_rate <= 0): 
    print("Invalid input. Check budget, expenses and exchange rates.") 
else: 
    usd_inr = usd * usd_rate 
eur_inr = eur * eur_rate 
gbp_inr = gbp * gbp_rate 
total = usd_inr + eur_inr + gbp_inr 
print("\n--- Travel Budget Report ---") 
print("USD expense in INR:", round(usd_inr, 2)) 
print("EUR expense in INR:", round(eur_inr, 2)) 
print("GBP expense in INR:", round(gbp_inr, 2)) 
print("Total travel expenditure:", round(total, 2)) 
if total > budget: 
    print("Budget exceeded by INR:", round(total - budget, 2)) 
elif total < budget: 
    print("Remaining budget in INR:", round(budget - total, 2)) 
else: 
    print("Budget fully utilized.") 