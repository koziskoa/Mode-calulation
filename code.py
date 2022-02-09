"""Mode calculation 
   - for unsorted data from list 
   - difficulty: 3 """
test = [5,8,1,1,6,3,4,7,9,9,5,12,45,65,7,3,8,7,2,6,5,4,9,8,10] #=> 
test2 = [1,3,9,45,1,2,7] # => 1

freq_dict = {}

# iterrating trough list of unsorted data
for i in test:
    if i not in freq_dict:
        freq_dict[i] = 1
    else:
        freq_dict[i] += 1

# defining variables
mod_key = 0
mod_val = 0

# interrating trough dictionary
for key in freq_dict:
    if freq_dict[key] > mod_val:
        mod_val = freq_dict[key]
        mod_key = key

print(f"The most frequent number in list: {mod_key}, frequency: {mod_val}")