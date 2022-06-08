#Let’s create favorite hobbies list and favorite foods list. Then form the ultimate favorites list by combining these two lists.

hobbies = ["eating", "baking", "being a ninja"]
fav_foods = ["chocolate" , "chocolate chips" , "chocolate chip cookies"]
favorites = hobbies + fav_foods 
print(favorites)
favorites_second = fav_foods + hobbies
print(favorites_second)

#You are in charge of the cake for your friend’s birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.
candles = [82, 49, 82, 82, 41, 82, 15, 63, 38, 25]
tallest =  max(candles)

total_number = candles.count(tallest)

print("They can blow out",total_number,"candles")

# Your sister wanted you to help with her homework. She is learning the vegetables and supposed to write down 7
# different vegetables. She wants you to check if she did everything correctly. First, remove the elements that are not
# vegetables. For every element you remove, you should add a new element to the list. Later, check the length of the
# list to make sure you have 7 elements. Finally, tell all the vegetables to your sister so that she can write them
# down.
vegies = ["eggplant", "pepper", "orange", "artichoke","potato", "pumpkin", "strawberry"]
vegies.remove("strawberry")
vegies.append("carrot")
vegies[2] = "ququmbah"
"""
vegies.remove("orange")
vegies.append("ququmbah")
"""

print(len(vegies))
print(vegies)

#You are given two lists, cities and landmarks. Add your city and a favorite landmark from it. Then ask the user which city they will go and suggest a landmark to visit. 
cities = ["London", "Toronto", "Paris"]
landmarks = ["The Big Ben", "CN Tower", "Eiffel Tower"]

cities.append("Istanbul")
landmarks.append("Bebek")
to_visit = input("Where would you like to go?London, Toronto, Paris or Istanbul")
