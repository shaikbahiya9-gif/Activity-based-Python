print("EMPLOYEE PAYROLL SYSTEM") 
name = input("Enter employee name: ") 
basic = float(input("Enter basic salary: Rs. ")) 
if basic <= 0: 
    print("Invalid basic salary") 
else: 
    hra = basic * 0.20 
da = basic * 0.10 
gross = basic + hra + da 
pf = basic * 0.12 
if gross > 30000: 
    tax = gross * 0.05 
else: 
    tax = 0 
deductions = pf + tax 
net_salary = gross - deductions 
if net_salary < 20000: 
    category = "Low" 
elif net_salary <= 40000: 
    category = "Medium" 
else: 
    category = "High" 
print("\n----- PAYROLL DETAILS -----") 
print("Employee Name:", name) 
print("Basic Salary: Rs.", round(basic, 2)) 
print("HRA: Rs.", round(hra, 2)) 
print("DA: Rs.", round(da, 2)) 
print("Gross Salary: Rs.", round(gross, 2)) 
print("PF Deduction: Rs.", round(pf, 2)) 
print("Tax Deduction: Rs.", round(tax, 2)) 
print("Total Deductions: Rs.", round(deductions, 2)) 
print("Net Salary: Rs.", round(net_salary, 2)) 
print("Salary Classification:", category) 