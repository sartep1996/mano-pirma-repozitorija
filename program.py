print("Hello, please enter 5 words")

list = []

word1 = str(input("Enter word number 1: "))
word2 = str(input("Enter word number 2: "))
word3 = str(input("Enter word number 3: "))
word4 = str(input("Enter word number 4: "))
word5 = str(input("Enter word number 5: "))

list.append(word1)
list.append(word2)
list.append(word3)
list.append(word4)
list.append(word5)


for index, words, in enumerate(list):
    word_length = len(words)
    output = f"{index+1}:{words} ({word_length} letters)"
    print(output)
