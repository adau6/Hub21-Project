
"""
You have a friend who wants to do a job depending on the topic he/she likes. For all the topics in the 'topic_list', ask him/her if he/she likes the topic. After learning what he/she likes, for each topic he/she likes, suggest a job.

Hint: You can use .index(elt) method to find the index of elt in the list.

"""

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
  print("You can be a ",job_list[top_index])
"""
"""
You and your friend is playing a card game where the players put a card in the middle in turns. If one card is greater than the other, the player with the greater card wins a point. For instance, J would win over 10. Your and your friends’ hands are given as a list below, decide how wins!
"""
your_hand = [2, 10, 3, 'K', 7,  'K', 6, 2]
friends_hand = [5, 9, 'Q', 'K', 'J',  3, 5, 2]

for card in your_hand:
  if card == "J":
    card_index = your_hand.index(card)
    your_hand[card_index] = 11
  if card == "Q":
    card_index = your_hand.index(card)
    your_hand[card_index] = 12
  if card == "K":
    card_index = your_hand.index(card)
    your_hand[card_index] = 13

for card in friends_hand:
  if card == "J":
    card_index = friends_hand.index(card)
    friends_hand[card_index] = 11
  if card == "Q":
    card_index = friends_hand.index(card)
    friends_hand[card_index] = 12
  if card == "K":
    card_index = friends_hand.index(card)
    friends_hand[card_index] = 13
  

print(your_hand)
print(friends_hand)
yours_score = 0
friends_score = 0


for i in range(len(your_hand)):
  your_card = your_hand[i] 
  friends_card = friends_hand[i] 

  if your_card > friends_card:
    yours_score += 1
  elif friends_card>your_card:
    friends_score += 1

if yours_score > friends_score:
  print("You win!")
elif yours_score == friends_score:
  print("İts a tie")
elif yours_score < friends_score:
  print("You loseeee")

# a = []
# a.append(1)
# a.index(x)
# a[5] = 10

