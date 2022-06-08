"""
Create a non-empty list named 'my_list' and fill it with facts about yourself. Ask the user the index of the element he/she wants to reach and return the element at that index.
"""
lst = [4, 7, 1000, 99, "yes","no", "ada", True, 6.9, [1,2,3]]

my_list = [12, "ada", "7-C" ,10, "play station 4"]
#          0     1      2     3           4        items= 5
index = int(input("Enter an index"))
in_my_list = index<len(my_list)

if in_my_list:
  print(my_list[index])
else:
  print("You have passed the limit")
  

  
"""
You are given the 'numbers' which contains the numbers from 1 to 1000. Special numbers are the ones that can be divided by 2 but not by 7. To solve the puzzle you need to find all the special numbers in the given list and store them in special list. When you are finished, print special_numbers to the console.
"""
numbers = list(range(1, 1000)) 
special_numbers = []