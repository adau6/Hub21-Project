

# strings
# 

# input("message here: ")
name = "Ada "
print(name)
"""
lst = [1,2,3]
lst[1] = 5
print(lst)
"""
surname = "Uysal"


full_name = name + surname
print("Full name: ",full_name)


upper_name = full_name.upper()
print(upper_name)

lower_name = full_name.lower()
print(lower_name)
string = "a b c d sdg g hs s f yhh tey wsyhbfr "

print(string.find("a"))
print(string.find("sdg"))
"""
# You are playing a game with 2 of your friends. Your first friend tell you a sentence secretly, and your second friend
# tries to guess a word from that sentence. You should let your second friend know if he/she finds a word.
"""
sentence = input("Give me your sentence")
sentence = sentence.lower()
word = input("Geuss a word.")
word = word.lower()
words_index = sentence.find(word)

print(words_index)

