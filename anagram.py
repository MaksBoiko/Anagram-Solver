import numpy
import os

def find_indexes(sorted_words_list, sorted_user_word):
    for i in range(size):
        if(sorted_words_list[i] == sorted_user_word):
            found_index.append(i)
    return found_index

while(True):
    os.system("cls")
    words = ""
    words_list = []
    path = ""
    choose = ''
    print("Enter anagram seaching mode: complicated of simple(c/s)")

    while True:
        choose = input()

        if(choose[0] == 'c'):
            path = "1.1m_words.txt"

            break
        if (choose[0] == 's'):
            path = "100k_words.txt"

            break

    with open(path, "r") as f:
       words = f.read()

    words_list = words.split("\n")

    user_word = input("Enter word: ")
    user_word = user_word.lower()
    sorted_user_word = sorted(user_word)
    found_index = []
    found_words = []

    size = len(words_list)
    sorted_words_list = []

    for i in range(size):
        sorted_words_list.append(sorted(words_list[i]))




    f.close()
    find_indexes(sorted_words_list, sorted_user_word)


    for i in range(len(found_index)):
        found_words.append(words_list[found_index[i]])

    print("Anagrams for word ", user_word, end="")
    print(": ", end="")
    found_words = numpy.unique(found_words)
    for i in range(len(found_words)):
        if(found_words[i] != user_word):
            if(i == len(found_words)-1):
                print(found_words[i], end="")
            else:
                print(found_words[i], end=", ")



