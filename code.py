"""Mode calculation 
   - for unsorted data from list 
   - difficulty: 3 """
# defining variables
test = [5,8,1,1,6,3,4,7,9,9,5,12,45,65,7,3,8,7,2,6,5,4,9,8,10] #=> 5,7,8,9
test2 = [1,3,9,45,1,2,7, "modrá", "modrá"] # => 1, modrá
freq_dict = {}
mod_val = 0 # frequency

# iterrating trough list of unsorted data
for element in test:
    if element not in freq_dict:
        freq_dict[element] = 1
    else:
        freq_dict[element] += 1

for cycle in range(2):
    if cycle == 0: # interrating trough dictionary
        for key in freq_dict:
            if freq_dict[key] > mod_val:
                mod_val = freq_dict[key] #the highest frequency
    else: # finds every modes in list
        print(f"Mode in list:")
        for key in freq_dict:
            if freq_dict[key] == mod_val:        
                print(f"    {key}")
print(f"frequency: {mod_val}")