#You are given two lists, cities and landmarks. Add your city and a favorite landmark from it. Then ask the user which city they will go and suggest a landmark to visit. 
#Addition: If you don't have a suggestion ask where they will visit and add that to the list!
cities = ["London", "Toronto", "Paris"]
landmarks = ["The Big Ben", "CN Tower", "Eiffel Tower"]

cities.append("Istanbul")
landmarks.append("Bebek")
city_to_visit = input("Where would you like to go? London, Toronto, Paris or Istanbul: ")

if city_to_visit in cities:
  city_index = cities.index(city_to_visit)
  print("You should visit", landmarks[city_index])
else:
  answer = input("Do you have any suggestions? Yes/No ")
  if answer == "yes":
    new_landmark = input("What is you suggestion?")
    cities.append(city_to_visit)
    landmarks.append(new_landmark)
    print("Here is the updated lists")
    print(cities)
    print(landmarks)

"""
You prepared an online test for your friends to see how well they know you. In one of the questions, you ask them to write one of your favorite fruits, all of which is listed in 'my_favorite_fruits'. If they know the answer, congragulate them and list your other favorite fruits. Otherwise, tell that they are wrong and list your favorite fruits one by one.

Ex1: (if the answer is Erik) Output1: Correct! Here are the remaining fruits I like: Strawberry Peach

Ex2: (if the answer is orange) Output2: Not correct :(, possible answers are these: Strawberry Peach Erik
"""

my_favorite_fruits = ["Strawberry", "Peach", "Erik"]

guess = input("What are my favorite fruits?: ")
if guess in my_favorite_fruits:
  print("Correct")
else:
  print("No, No, No, my favorites are ")
  print()