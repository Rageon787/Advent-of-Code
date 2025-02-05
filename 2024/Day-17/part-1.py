import sys 
import re 

filename = sys.argv[1]

with open(filename) as f:
    raw_input = f.read()
    raw_input = raw_input.split("\n")

    a = int(re.findall(r"\d+", raw_input[0])[0])
    b = int(re.findall(r"\d+", raw_input[1])[0])
    c = int(re.findall(r"\d+", raw_input[2])[0])
    instructions = [int(x) for x in re.findall(r"\d+", raw_input[-2])]
    print(a)
    print(b)
    print(c)
    print(instructions)

ans = []
ip = 0
while ip + 1 < len(instructions):
    
    opcode = instructions[ip]
    operand = instructions[ip + 1]   
    # For each instruction operand, we can get two types of operands: it's literal operand and it's combo operand
    literal_operand = operand   # The literal operand is just the value of the operand itself 

    # The combo operand is different depending on the value of the operand 
    if operand <= 3: combo_operand = operand                # If the operand <= 3, then the combo operand is it's literal operand 
    elif operand == 4: combo_operand = a                    # The combo operand is the value in register A
    elif operand == 5: combo_operand = b                    # The combo operand is the value in register B 
    elif operand == 6: combo_operand = c                    # The combo operand is the value in register C 
    else: combo_operand = operand   # According to the problem, we will not have combo operands for operand >= 7
    result = -1
    if opcode == 0: 
        # adv instruction: Performs division 
        # Numerator : Value in register A
        # Denominator: 2^combo_operand
        result = a / (2 ** combo_operand)
        # Result is stored in register A 
        # If the output is a decimal, truncate it to an integer 
        a = int(result)
    elif opcode == 1:            
        # bxl instruction
        result = b ^ literal_operand  # bitwise xor of value in register B and the literal operand 
        b = result  # Result is stored in register B 
    elif opcode == 2:
        # bst instruction 
        result = combo_operand % 8 # calculates the value of it's combo operand modulo 8
        b = result # Result is then stored in register B  
    elif opcode == 3:
        # jnz instruction
        # does nothing if a = 0 and jumps instruction by 2
        # else, jump the instruction to the literal operand 
        if a != 0:
            ip = literal_operand 
            continue 
    elif opcode == 4:
        # bxc instruction  
        result = b ^ c  # bitwise xor of register B and register C 
        b = result # Result is stored in register B 
    elif opcode == 5:
        # out instruction 
        result = combo_operand % 8  
        ans.append(result) # Just prints it and Does'nt store the result in any register
    elif opcode == 6:
        # bdv instruction
        result = a / (2 ** combo_operand) # exactly like the adv instruction 
        b = int(result) # but result is stored in register B instead 
    else:
        # cdv instruction 
        result = a / (2 ** combo_operand) # exactly like adv instruction 
        c = int(result) # but result is stored in register C instead 
    ip += 2
ans2 = ""
for i in range(len(ans)): 
    ans2 += str(ans[i])
    if i < len(ans) - 1: ans2 += ','
print(ans2)

