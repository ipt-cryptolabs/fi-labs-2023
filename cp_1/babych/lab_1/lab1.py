import codecs
import math
from collections import Counter
import re


my_text = open("my_text.txt", "r+", encoding='utf-8')
text = my_text.read()
my_text.close()

dictionary = "абвгдежзийклмнопрстуфхцчшщыьэюя"  # without space
dictionary1 = "абвгдежзийклмнопрстуфхцчшщыьэюя "  # with space
number = "0123456789"


def edit_text(text, dictionary1):

    for letter in text:
        text = text.lower()
        if letter == "ё":
            text = text.replace('ё', 'е')
        elif letter == "ъ":
            text = text.replace('ъ', 'ь')
        elif letter not in dictionary1 and not letter.isupper():
            text = text.replace(letter, '')
    new_text = open('clear_text1.txt', 'w')
    new_text.write(text)
    new_text.close()
    return text


print("Edited text without space", edit_text(
    text, dictionary))  # without space
print("Edited text with space", edit_text(text, dictionary1))  # with space


def FrequencyLetter(text):
    c = Counter(text)
    freq_letter = dict(c)
    for i in freq_letter:
        freq_letter[i] = (freq_letter[i]/len(text))
    return dict(sorted(freq_letter.items()))


def FrequencyBigram(text):

    freq_bigram = {}
    for i in range(len(text)):
        bigram = text[i: i + 2]
        if bigram in freq_bigram:
            freq_bigram[bigram] += 1
        else:
            freq_bigram[bigram] = 1

    for i in freq_bigram:
        freq_bigram[i] = freq_bigram[i] / len(text)

    return dict(sorted(freq_bigram.items()))


def EntropyBigram(frequency):
    n = 2
    for i in frequency:
        frequency[i] += -frequency[i]*math.log2(frequency[i])
    entropy = 0
    for i in frequency:
        entropy += frequency[i]
    res = entropy/n
    return res


def EntropyLetter(frequency):
    entropy = 0
    for i in frequency:
        entropy += frequency[i]*math.log2(frequency[i])
    return -entropy/2


def RedundancyWithSpace(entropy):  # i=32 with space and 31 - without
    redundancy = 1 - (entropy/math.log2(32))
    return redundancy


def RedundancyWithoutSpace(entropy):
    redundancy = 1 - (entropy/math.log2(31))
    return redundancy


# Frequency
print("Frequency monogram with space",
      FrequencyLetter(edit_text(text, dictionary1)))
print("Frequency monogram without space",
      FrequencyLetter(edit_text(text, dictionary)))

print("Frequency bigram with space",
      FrequencyBigram(edit_text(text, dictionary1)))
print("Frequency bigram without space",
      FrequencyBigram(edit_text(text, dictionary)))

# Entropy
print("Entropy monogram with space", EntropyLetter(
    FrequencyLetter(edit_text(text, dictionary1))))
print("Entropy monogram without space", EntropyLetter(
    FrequencyLetter(edit_text(text, dictionary))))

print("Entropy bigram with space", EntropyBigram(
    FrequencyBigram(edit_text(text, dictionary1))))
print("Entropy bigram without space", EntropyBigram(
    FrequencyBigram(edit_text(text, dictionary))))

# Redundancy
print("Redundancy monogram with space", RedundancyWithSpace(
    EntropyLetter(FrequencyLetter(edit_text(text, dictionary1)))))
print("Redundancy monogram without space", RedundancyWithoutSpace(
    EntropyLetter(FrequencyLetter(edit_text(text, dictionary)))))

print("Redundancy bigram with space", RedundancyWithSpace(
    EntropyLetter(FrequencyLetter(edit_text(text, dictionary1)))))
print("Redundancy bigram without space", RedundancyWithoutSpace(
    EntropyLetter(FrequencyLetter(edit_text(text, dictionary)))))
