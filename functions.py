def count_elements (data):
    """Counts frequency of each element in file
    - required 1 parametr: list of values 
    - returns dictionary
        - keys represent elements from file
        - values represent elements frequency"""
    freq_dict = {}
    # iterrating trough list of unsorted data
    for element in data:
        if element not in freq_dict:
            freq_dict[element] = 1
        else:
            freq_dict[element] += 1
    return freq_dict

def find_modus (dict_frequency):
    mod_val = 0 # frequency
    for cycle in range(2):
        if cycle == 0: # interrating trough dictionary
            for key in dict_frequency:
                if dict_frequency[key] > mod_val:
                    mod_val = dict_frequency[key] #the highest frequency
        else: # finds every modes in list
            print(f"Mode in list:")
            for key in dict_frequency:
                if dict_frequency[key] == mod_val:        
                    print(f"    {key}")
    print(f"frequency: {mod_val}")