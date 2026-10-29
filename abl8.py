PASS_MARK = 40 
MAX_GRACE = 5 
SUBJECTS = 5 
marks = [] 
for i in range(SUBJECTS): 
    mark = int(input(f"Enter marks for subject {i + 1}: ")) 
    marks.append(mark) 
if any(mark < 0 or mark > 100 for mark in marks): 
    print("Invalid marks. Enter marks between 0 and 100.") 
else: 
    failed = [] 
for i in range(SUBJECTS): 
    if marks[i] < PASS_MARK: 
        failed.append(i) 
        grace_used = 0 
if len(failed) == 0: 
    result = "PASS" 
elif len(failed) == 1: 
    subject = failed[0] 
shortfall = PASS_MARK - marks[subject] 
if shortfall <= MAX_GRACE: 
    grace_used = shortfall 
    marks[subject] += grace_used 
    result = "PASS WITH GRACE MARKS" 
else: 
    result = "FAIL" 
    print("\n--- EXAMINATION RESULT ---") 
for i in range(SUBJECTS): 
    print(f"Subject {i + 1}: {marks[i]}") 
print("Grace marks used:", grace_used) 
print("Final Result:", result)