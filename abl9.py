import math 
total_classes = int(input("Enter total classes conducted: ")) 
attended_classes = int(input("Enter classes attended: ")) 
target = float(input("Enter required attendance percentage: ")) 
if (total_classes <= 0 or attended_classes < 0 
or attended_classes > total_classes 
or target <= 0 or target > 100): 
    print("Invalid input. Please check the entered values.") 
else: 
    current = attended_classes / total_classes * 100 
print("\n--- ATTENDANCE RECOVERY REPORT ---") 
print("Total classes:", total_classes) 
print("Classes attended:", attended_classes) 
print("Current attendance:", round(current, 2), "%") 
print("Required attendance:", target, "%") 
if current >= target: 
    print("Status: Target attendance achieved.") 
elif target == 100: 
    print("100% attendance cannot be reached by attending") 
    print("future classes alone when classes were missed.") 
else: 
    numerator = target * total_classes - 100 * attended_classes 
    denominator = 100 - target 
    additional = math.ceil(numerator / denominator) 
print("Additional classes required:", additional) 
print("Status: Attendance recovery needed.") 