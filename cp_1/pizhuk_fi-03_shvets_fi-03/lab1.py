from math import log2

CHARSET_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '


def clear_text(text: str, remove_spaces: bool = False) -> str:
    text = text.lower().replace('ъ', 'ь').replace('ё', 'е')
    text = text.replace(' ', '') if remove_spaces else text
    text = ' '.join(text.split())
    return ''.join([i for i in text if i in CHARSET_RU])



def count_letters(text: str) -> dict:
    frequencies = {}
    for letter in text:
        if letter in frequencies:
            frequencies[letter] += 1
        else:
            frequencies[letter] = 1
    return frequencies


def count_bigrams(text: str, separate: bool = False) -> dict:
    frequencies = {}
    for i in range(0, len(text)-1, 2 if separate else 1):
        bigram = text[i:i+2]
        # if ' ' not in bigram:
        if bigram in frequencies:
            frequencies[bigram] += 1
        else:
            frequencies[bigram] = 1
    return frequencies


def get_probability(frequencies: dict) -> dict:
    probs = {}
    for ngram in frequencies:
        probs[ngram] = frequencies[ngram]/sum(frequencies.values())
    return probs


def get_entropy(probabilities: dict, bigrams: bool = False) -> float:
    entropy = 0
    div = 2 if bigrams else 1
    for frequency in probabilities.values():
        entropy -= frequency*log2(frequency)/div
    return entropy


def get_redundancy(entropy: float, spaces: bool) -> float:
    return 1 - entropy/log2(31+spaces)


with open('text.txt', 'r', encoding="utf8") as fout:
    text = fout.read()


def get_sorted_probs(probabilities: dict) -> dict:
    return dict(sorted(probabilities.items(), key=lambda item: item[1], reverse=True))

#text with spaces
#монограми
cleaned_spaces = clear_text(text)
let_freq = count_letters(cleaned_spaces)
let_probs = get_probability(let_freq)
let_entropy = get_entropy(let_probs)
let_red = get_redundancy(let_entropy, True)
print(let_entropy)
print(let_red)
print(get_sorted_probs(let_probs))

#з перетинами
bi_freq = count_bigrams(cleaned_spaces)
bi_probs = get_probability(bi_freq)
bi_entropy = get_entropy(bi_probs, True)
bi_redundancy = get_redundancy(bi_entropy, True)
print(bi_entropy)
print(bi_redundancy)
print(get_sorted_probs(bi_probs))

#без перетинів
bi_freq_sep = count_bigrams(cleaned_spaces, True)
bi_probs_sep = get_probability(bi_freq_sep)
bi_entropy_sep = get_entropy(bi_probs_sep, True)
bi_redundancy_sep = get_redundancy(bi_entropy_sep, True)
print(bi_entropy_sep)
print(bi_redundancy_sep)
print(get_sorted_probs(bi_probs_sep))

print('\n\n\n')

#text without spaces
#монограми
cleaned_no_spaces = clear_text(text, True)
let_freq = count_letters(cleaned_no_spaces)
let_probs = get_probability(let_freq)
let_entropy = get_entropy(let_probs)
let_red = get_redundancy(let_entropy, False)
print(let_entropy)
print(let_red)
print(get_sorted_probs(let_probs))

#з перетинами
bi_freq = count_bigrams(cleaned_no_spaces)
bi_probs = get_probability(bi_freq)
bi_entropy = get_entropy(bi_probs, True)
bi_redundancy = get_redundancy(bi_entropy, False)
print(bi_entropy)
print(bi_redundancy)
print(get_sorted_probs(bi_probs))

#без перетинів
bi_freq_sep = count_bigrams(cleaned_no_spaces, True)
bi_probs_sep = get_probability(bi_freq_sep)
bi_entropy_sep = get_entropy(bi_probs_sep, True)
bi_redundancy_sep = get_redundancy(bi_entropy_sep, False)
print(bi_entropy_sep)
print(bi_redundancy_sep)
print(get_sorted_probs(bi_probs_sep))

