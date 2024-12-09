# Given 1000 reports (where each report is represted as a list of integers) 
# A report is safe if:
    # Increasing or decreasing, and  
    # The absolute Difference between adjacent elements is in the range [1, 3]
# Otherwise unsafe  
# Hence, find the number of safe reports 


f = open("input.txt", "r")                  # Open the input file 
reports = []                                        # List to store our reports
for line in f:
    reports.append([int(x) for x in line.split()])  # Split into a list and convert the integer strings to integers

safe = 0                                            # Counter for the number of safe reports 
for report in reports:                              # Process each report 
    
    incr, decr = True, True                         # Booleans for whether a sequence increasing or decreasing 
     
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]            # Difference between adjacent elements 
        if diff < 1 or diff > 3:                    # If sequence is increasing but diff is in range (-inf, 1) U (3, inf)
            incr = False 
        if diff > -1 or diff < -3:                  # If sequence is decreasing but dif is in the range (-inf, -3) U (-1, inf)
            decr = False
    
    if incr or decr:                               # If the sequence is increasing or decreasing
        safe += 1                                  # Then the report is safe 

print(safe)


