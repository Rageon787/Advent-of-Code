# Given 1000 reports (where each report is represted as a list of integers) 
# A report is safe if:
    # Increasing or decreasing, and  
    # The absolute Difference between adjacent elements is in the range [1, 3]
# Otherwise unsafe  

# However it is possible to turn an unsafe report into a safe report by removing some elements from the array 

# Hence, find the number of reports that can be made safe by removing at-most 1 element  
#############################################################################################################

# Approach 1
# A naive approach is try and remove each element from the list and see if the sequence satisfies our conditions
# However, has a lower bound of O(N^3), therefore not really effiicent 




def isIncreasing(report, idx, removed):
    if idx == 0: 
        if report[idx] >= report[idx + 1]:
            return isIncreasing(report, idx + 1, True)              # Remove A[0] & Check if A[i+1..N] is increasing
        else:
            return isIncreasing(report, idx + 1, False)             # Check if A[i+1..N] is increasing

    elif idx == len(report) - 1:
        if report[idx] <= report[idx - 1]:
            return not removed                                      # We can't remove more than 2 elements
        else:
            diff = report[idx] - report[idx - 1] 
            if diff < 1 or diff > 3:
                return False
            return True                                             # We remove the last element, hence the report is now safe  

    else:
        diff = report[idx] - report[idx - 1]
        if (report[idx] <= report[idx - 1]) or (diff < 1 or diff > 3):                          # Remove A[i]
            diff = report[idx + 1] - report[idx - 1]                # A[i + 1] and A[i - 1] will be adjacent
            if removed or (diff < 1 or diff > 3):                  # if we've already removed or the difference is not in the range [1, 3]
                return False 
            else:
                return isIncreasing(report, idx + 1, True)          # Otherwise, we remove A[i] and check if A[i+1..n] is increasing
        else: 
            diff = report[idx] - report[idx - 1] 
            if diff < 1 or diff > 3:
                return False
            return isIncreasing(report, idx + 1, removed)                  # Check if A[i+1..N] is increasing

        
def isDecreasing(report, idx, removed):
    print(report[idx])
    if idx == 0:
        if report[idx] <= report[idx + 1]:
            return isDecreasing(report, idx + 1, True) 
        else:
            return isDecreasing(report, idx + 1, False) 

    elif idx == len(report) - 1:
        if report[idx] >= report[idx - 1]:
            return not removed 
        else:
            diff = report[idx] - report[idx - 1] 
            if (diff > -1 or diff < -3):
                return False
            return True
    else:
        diff = report[idx] - report[idx - 1]
        if (report[idx] >= report[idx - 1]) or (diff > -1 or diff < -3):
            diff = report[idx + 1] - report[idx - 1] 
            if removed or (diff > -1 or diff < -3):
                return False 
            else:
                return isDecreasing(report, idx + 1, True)         
        else:
            diff = report[idx] - report[idx - 1] 
            if (diff > -1 or diff < -3):
                return False
            return isDecreasing(report, idx + 1, removed)
        
# f = open("sample-input.txt", "r")
f = open("input/input-2.txt", "r")                   
safe = 0
for line in f:
    report = [int(x) for x in line.split()]
    print(report)
    if len(report) == 1:
        safe += 1
        print(safe)
    elif isDecreasing(report, 0, False) or isIncreasing(report, 0, False):
        safe += 1 
        print(safe)         
    else:
        print(safe)
        continue

print(safe)


