# Challenge1:
number_list = []
# Take 3 numbers from the user that are between 1-1000 and add them to the 'number_list'.
# Later, find the maximum number in the list,
"""
first = int(input("Enter a number"))
number_list.append(first)
second = int(input("Enter a number"))
number_list.append(second)
third = int(input("Enter a number"))
number_list.append(third)

maximum = 0

for number in number_list:
    if maximum < number:
        maximum = number
print("Our maximum is", maximum)
"""

# Challenge2:
my_guesses = [10, 20, 30, 40, 50, 60]
my_friends_guesses = [17, 28, 50, 23, 10, 38]
# You and your friend try to guess the price of a hat your other friend bought. You have 6 chances and when you use all
# your chances, your friend with the hat says that "You both guessed it correctly!". 'my_guesses' and
# 'my_friends_guesses' contains the guesses. Checking both lists, try to find which values can be the price of the hat.
"""
for my_guess in my_guesses:
  #print(my_guess)
  for friends_guess in my_friends_guesses:
    #print(friends_guess)
    if my_guess == friends_guess:
      print("You both guessed it correctly!", my_guess)

"""
  


# Challenge3:
math_exam_notes = [92.8, 97]
# 'math_exam_notes' holds the grades for your first two math exams. To learn your final grade, you go to the teacher's
# office. First, ask your final grade and add it to your grade list. Later, find the average grade you will get from the
# course.
# Note: Your final grade does not have to be an integer.
exam = float(input("Enter your grade"))
math_exam_notes.append(exam)
exam_sum = 0
for grade in math_exam_notes:
  exam_sum += grade

print(exam_sum / len(math_exam_notes))

# Challenge4:
mixed = [
    "banana", "apple", "banana", "apple", "potato", "carrot", "potato",
    "carrot", "potato", "carrot"
]
# You have the mixed list, find how many vegetables and fruits there are in the mixed list and print it to
# the console.
veggies = ["potato", "carrot"]
fruits = ["banana", "apple"]
