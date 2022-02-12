"""Mode calculation 
   - for unsorted data from list 
   - difficulty: 3 """
# defining variables
from functions import count_elements, find_modus

test = [5,8,1,1,6,3,4,7,9,9,5,12,45,65,7,3,8,7,2,6,5,4,9,8,10] #=> 5,7,8,9
test2 = [1,3,9,45,1,2,7, "blue", "blue"] # => 1, blue

modus_val = count_elements(test)

find_modus(modus_val)