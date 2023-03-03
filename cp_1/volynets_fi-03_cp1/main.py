import math
import collections
import itertools
import string

def concat_tuple(t: tuple):
    rez = ""
    for c in t:
        rez += c

    return rez

def count_n_gram_apiarance(n: int, text: str) -> dict:
    """Counts only apearance of letters and their number"""
    alpha = set()
    for i in text:
        if i not in alpha and i != '\n':
            alpha.add(i)

    # print(f"size of alphabet is: {len(alpha)}")

    n_gram_counter = collections.defaultdict(int)

    for key in itertools.product(alpha, repeat=n):
        s_key = concat_tuple(key)
        reps = text.count(s_key)
        n_gram_counter[reps] += 1
            # print(f">>{s_key}: {reps}")

    return n_gram_counter

def print_dict(d: dict, width: int=22):
    len_c = 0
    for key in d:
        # print(f"key: \"{key}\", value: {n_gram_counter[key]}.")
        s = f"key: \"{key}\", value: {d[key]}"
        print(f'{s:<24}', end="")
        if len_c > 3:
            len_c = 0
            print("")
        else:
            len_c += 1
    
    print("")


def count_n_gram(n: int, text: str) -> dict: 
    alpha = set()
    for i in text:
        if i not in alpha and i != '\n':
            alpha.add(i)

    n_gram_counter = dict()

    for key in itertools.product(alpha, repeat=n):
        s_key = concat_tuple(key)
        reps = text.count(s_key)
        if reps != 0:
            n_gram_counter[s_key] = reps
            # print(f">>{s_key}: {reps}")

    return n_gram_counter

def calculate_H(n_gram_counter: dict):
    """Calculaes entoppy
    
    Args:
        n_gram_counter (dict): diktionary with key as times that some
        symbol apears and value as number of symbols that appears key times
        
    Returns:
        int: entroppy value"""
    
    sum_of_symbols = 0
    for key in n_gram_counter:
        sum_of_symbols += key * n_gram_counter[key]

    # print(f"number of symbols is: {sum_of_symbols}")

    H = 0
    for key in n_gram_counter:
        if key != 0:
            H -= (key/sum_of_symbols) * math.log(key/sum_of_symbols) * n_gram_counter[key]

    return H



rand_text = """У меня большая семья из шести человек: я, мама, папа, старшая сестра,
бабушка и дедушка. Мы живем все вместе с собакой Бимом и кошкой Муркой в большом доме
в деревне. Мой папа встает раньше всех, потому что ему рано на работу. Он работает доктором.
Обычно бабушка готовит нам завтрак. Я обожаю овсяную кашу, а моя сестра Аня – блины.
После завтрака мы собираемся и идем в школу. Моя сестра учится в пятом классе, а я –
во втором. Мы любим учиться и играть с друзьями. Больше всего я люблю географию. Когда
мы приходим домой из школы, мы смотрим телевизор, а потом ужинаем и делаем уроки. Иногда
мы помогаем бабушке и маме в огороде, где они выращивают овощи и фрукты."""

def main():
    # n_gram_counter = count_n_gram(n=5, text=rand_text)

    # print_dict(n_gram_counter)

    # for key in n_gram_counter:
    #     print(f"{key} times apears {n_gram_counter[key]} symbols.")
    
    n_gram_counter = count_n_gram_apiarance(n=1, text=rand_text)
    print(f"H = {calculate_H(n_gram_counter)}")

    

if __name__ == "__main__":
    main()

