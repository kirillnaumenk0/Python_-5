# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect


from random import sample


def list_words(a: int, b: str = 'абв'):
    my_list = []
    for i in range(a):
        enter = sample(b, 3)
        my_list.append("".join(enter))
    return " ".join(my_list)


def second_list_words(words: str):
    return " ".join(i for i in words.split() if i != "абв")


word = int(input("Число слов: "))
if word <= 0:
    print('The data is incorrect')
else:
    end_list = list_words(word)
    print(end_list)
    print(second_list_words(end_list))
