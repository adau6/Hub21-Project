"""
You prepared an online test for your friends to see how well they know you. In one of the questions, you ask them to write one of your favorite fruits, all of which is listed in 'my_favorite_fruits'. If they know the answer, congragulate them and list your other favorite fruits. Otherwise, tell that they are wrong and list your favorite fruits one by one.

Ex1: (if the answer is Erik) Output1: Correct! Here are the remaining fruits I like: Strawberry Peach

Ex2: (if the answer is orange) Output2: Not correct :(, possible answers are these: Strawberry Peach Erik
"""
"""
my_favorite_fruits = ["Strawberry", "Peach", "Erik"]

guess = input("What are my favorite fruits?: ")
if guess in my_favorite_fruits:
  print("Correct")
  # guess = "Peach"
  # my_favorite_fruits = ["Strawberry", "Peach", "Erik"]
  for fruit in my_favorite_fruits:
    if fruit != guess:
      print(fruit)
else:
  print("No, No, No, my favorites are ")

  for fruit in my_favorite_fruits:
    print(fruit)

"""

"""
You have a friend who wants to do a job depending on the topic he/she likes. For all the topics in the 'topic_list', ask him/her if he/she likes the topic. After learning what he/she likes, for each topic he/she likes, suggest a job.

Hint: You can use .index(elt) method to find the index of elt in the list.

"""
topic_list = ["math", "french", "english", "arts", "sciences"]
job_list = ["Banker", "Travel Guide", "Literature Teacher", "Artist", "Lab Assistant"]

topics = []
for topic in topic_list:
  question = "Do you like " + topic +"?"
  answer = input(question)
  if answer == "yes":
    topics.append(topic)
    
for top in topics:
  top_index = topic_list.index(top)
  print(top_index)