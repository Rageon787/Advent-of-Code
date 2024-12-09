# Given a string computer instructions 
# Extract all instructions mul(x,y), where x and y are integers
# Sum the product of these multplication instructions 
import re 

with open("input.txt", "r") as f: s = f.read() 

multiplication_instructions = re.findall("mul\(\d+,\d+\)", s)       # Regex expression to extract all "mul(x,y)" instructions       

ans = 0
for instruction in multiplication_instructions:                    
    nums = [int(x) for x in instruction[4:len(instruction) - 1].split(",")]            # convert the string "mul(x,y)" -> [x, y]
    ans += nums[0] * nums[1]                                                           # Sum the product  

print(ans)