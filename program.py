# print("Hello, please enter 5 words")

# list = []

# word1 = str(input("Enter word number 1: "))
# word2 = str(input("Enter word number 2: "))
# word3 = str(input("Enter word number 3: "))
# word4 = str(input("Enter word number 4: "))
# word5 = str(input("Enter word number 5: "))

# list.append(word1)
# list.append(word2)
# list.append(word3)
# list.append(word4)
# list.append(word5)


# for index, words, in enumerate(list):
#     word_length = len(words)
#     output = f"{index+1}:{words} ({word_length} letters)"
#     print(output)


from functools import reduce
import operator

skaiciai = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lyginiai_skaiciai = list(filter(lambda x: x % 2 == 0, skaiciai))
ave_lyginiai_skaiciai = reduce(lambda x, y : (x*y)/ len(lyginiai_skaiciai), lyginiai_skaiciai)

print(ave_lyginiai_skaiciai)

