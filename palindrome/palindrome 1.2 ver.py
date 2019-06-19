def palindrome(word):
    word_list = list(word)
    if word_list == word_list[::-1] and len(word) > 1:
        return "слово полидром"
    elif len(word) == 1:
        return "слово не состоит из 1 буквы"
    else:
        return "слово не полидром"

input_word = input("Введите слово, проверим на полидромность\n")
print(palindrome(input_word))
