# Given 1000 reports (where each report is represted as a list of integers) 
# A report is safe if:
    # Increasing or decreasing, and  
    # The absolute Difference between adjacent elements is in the range [1, 3]
# Otherwise unsafe  
# Hence, find the number of safe reports 
 
with open("input.txt", "r") as f: 
    for line in f:
        report = [int(x) for x in line.split()]
        n = len(report)
        prefix, suffix = [False] * n, [False] * n 
        
        prefix[0] = True, suffix[n - 1] = True 
        for i in range(1, n):
            if report[i] < report[i - 1]:
                prefix[i]
            