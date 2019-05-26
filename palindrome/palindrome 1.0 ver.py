import math

def palindrome(word):
    rezult = True
    word_list = list(word.lower())
    n = math.floor(len(word_list)/2)

    for i in range(n):
        if word_list[i] != word_list[len(word) - 1 - i]:
            rezult = False
    return rezult


input_word = input("Введите слово, проверим на полидромность\n")
print(palindrome(input_word))
