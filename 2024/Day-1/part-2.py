from collections import Counter
f = open("input.txt", "r")  

left_list = [] 
right_list = []
for line in f:                                  # Read line by line 
    line = line[:-1]                            # Remove the last character 
    pair = line.split("   ")                    # Remove the whitespaces in between the numbers  
    left_list.append(int(pair[0])) 
    right_list.append(int(pair[1])) 
    

freq = Counter(right_list)                      # Compute all the frequencies of values from the right list 

similarity_score = 0
for x in left_list:
    similarity_score += (x * freq[x])
print(similarity_score) 
   