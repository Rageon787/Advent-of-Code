f = open("input.txt", "r")  

left_list = [] 
right_list = []
for line in f:                                  # Read line by line 
    line = line[:-1]                            # Remove the last character 
    pair = line.split("   ")                    # Remove the whitespaces in between the numbers  
    left_list.append(int(pair[0])) 
    right_list.append(int(pair[1])) 
    
left_list.sort() 
right_list.sort() 

distance = 0
for i in range(len(left_list)):
    distance += abs(left_list[i] - right_list[i]) 
print(distance)
    
