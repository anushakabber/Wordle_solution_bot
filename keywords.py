import nltk
from nltk.corpus import words
import re
nltk.download('punkt')
nltk.download('words')


def catchKeywords(info)

    sentence = info
    word_list = words.words()
    five_letter_words = [i for i in word_list if len(i)==5]
    key_words = {"containing":1, "contains":1, "starts with":3, "ends with":4, "not containing":-1, "having":1, "starting with":3, "beginning with":3, "ending with":4, "first":5, "second":6, "third":7, "fourth":8, "fifth":9, "not having":-1, "not containing":-1, "not starting":-3, "not ending":-4, "not beginning":-3}

    indicative_letters = {}
    for i in key_words.keys():
        value = []
        if i in sentence:
            k = sentence.index(i)
            if key_words[i] in [1, -1, 3, 4, -4, -3]:
                temp = ""
                for m in range(k+len(i),len(sentence)):
                    if sentence[m]== ';':
                        break
                    temp += sentence[m]
                temp = temp.split(" ")
                for h in temp:
                    if '\'' in h:
                        value.append(h)
            else:
                hold = 0
                for m in range(0, k):
                    if sentence[m] == ';':
                        hold = m
                temp = sentence[hold+1:k]
                temp = temp.split(" ")
                for h in temp:
                    if '\'' in h:
                        value.append(h)
            indicative_letters[i] = value

    return (indicative_letters, five_letter_words, key_words)
