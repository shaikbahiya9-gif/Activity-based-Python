print("HOSPITAL BILLING SYSTEM") 
print("1. General Ward - Rs.1000 per day") 
print("2. Semi-Private - Rs.2000 per day") 
print("3. Private Room - Rs.3500 per day") 
name = input("Enter patient name: ") 
days = int(input("Enter number of admission days: ")) 
room_type = int(input("Enter room type (1/2/3): ")) 
medical_charges = float(input("Enter medical service charges: ")) 
if days <= 0 or medical_charges < 0: 
    print("Invalid admission days or medical charges.") 
elif room_type not in [1, 2, 3]: 
    print("Invalid room type.") 
else: 
    if room_type == 1: 
        room_charges = days * 1000 
        room_name = "General Ward" 
    elif room_type == 2: 
        room_charges = days * 2000 
        room_name = "Semi-Private Room" 
    else: 
        room_charges = days * 3500 
        room_name = "Private Room" 
        total_bill = room_charges + medical_charges 
    if total_bill < 5000: 
        category = "Basic" 
    elif total_bill <= 15000: 
        category = "Moderate" 
    else: 
        category = "High-cost" 
print("\n----- HOSPITAL BILL -----") 
print("Patient Name:", name) 
print("Room Type:", room_name) 
print("Room Charges: Rs.", room_charges) 
print("Medical Charges: Rs.", medical_charges) 
print("Total Bill: Rs.", total_bill) 
print("Patient Classification:", category) 