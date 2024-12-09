# We are given a string of instructions 
# if the instruction is do(), then sum the value given by future multiplication operations 
# if the instruction is don't(), then don't ignore every instruction until the next do()
import re 

with open("input.txt", "r") as f: s = f.read() 

instructions = re.split("(don't|do)", s)                # Splitting the instruction to a list seperated by do's and don'ts 

curr = "do"                                             # Start with instruction "do" 
ans = 0
for instruction in instructions:
    if instruction == "do" or instruction == "don't":   # change the current instruction
        curr = instruction
    else:
        if curr == "do":                                # Only apply multiplication instructions if the current instruction is do()
            multiplication_instructions = re.findall("mul\(\d+,\d+\)", instruction)    # Similar to part 2   
            for instruction in multiplication_instructions:
                    nums = [int(x) for x in instruction[4:len(instruction) - 1].split(",")]
                    ans += nums[0] * nums[1] 

        else:
            continue
    
        

print(ans)