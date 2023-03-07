import os
import math
import collections
import itertools

def concat_tuple(t: tuple):
    """Concatenate all symbols in tuple. Need for creating keys.
    Itertool prod isn't correct for me
    """
    rez = ""
    for c in t:
        rez += c

    return rez

def count_n_gram_apearance(n: int, text: str, alphabet: str) -> dict:
    """Counts only apearance of letters and their number
    """
    n_gram_counter = collections.defaultdict(int)
    n_gram_letter_counter = dict()

    for key in itertools.product(alphabet, repeat=n):
        s_key = concat_tuple(key)
        reps = text.count(s_key)
        n_gram_counter[reps] += 1
        n_gram_letter_counter[s_key] = reps

    return n_gram_counter, n_gram_letter_counter

def count_n_gram(n: int, text: str) -> dict: 
    """Count apearance of all leters separately.
    """
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
        int: entroppy value
    """
    sum_of_symbols = 0
    for key in n_gram_counter:
        sum_of_symbols += key * n_gram_counter[key]

    H = 0
    for key in n_gram_counter:
        if key != 0:
            p_i = key/sum_of_symbols
            H -= (p_i) * math.log2(p_i) * n_gram_counter[key]

    return H

def create_text():
    """Convert file temp_text.txt to apropriate for me wiev and save it in rand_text.txt
    """
    file_text = get_text("cp_1/volynets_fi-03_cp1/temp_text.txt")

    ban = [",",
           ".",
           "\n",
           "!",
           "«",
           "»",
           "(",
           ")",
           "-",
           "=",
           ":",
           ";",
           "/",
           "§",
           "—",
           "_",
           "-",
           ]
    with open("cp_1/volynets_fi-03_cp1/rand_text.txt", "w") as file:
        for c in file_text:
            if c.isalpha():
                file.write(c.lower())

def get_text(src: str):
    with open(src, "r") as file:
        return file.read()
    
def write_n_gram_letter_counter(n_gram_letter_counter, n):
    """I will use that function to copy and paste text for table of
    calculated letter apearance for latex file
    """
    cnt = 0
    with open(f"cp_1/volynets_fi-03_cp1/table{n}.txt", "w") as table_file:
        table_file.write("\\begin{longtable}{rlrlrlrlrlrl}\n")
        for c, ap in n_gram_letter_counter:
            if cnt == 0:
                table_file.write(f"\t{c}: & {ap}")
            if cnt > 3:
                table_file.write(f" & {c}: & {ap} \\\\\n")
                cnt = 0
            else:
                table_file.write(f" & {c}: & {ap}")
                cnt += 1
        table_file.write(" \\\\\n\\end{longtable}\n")

def main():
        text = get_text("cp_1/volynets_fi-03_cp1/rand_text.txt")
    
        alphabet = "щцкяхмбавинлйшдыфъжспучэьтгорюзе"

        # Here i is a size of leters: 1 is leter, 2 is bigram, and other
        # should be in range(1, 3). In other way it will work forewer (wery long)
        for i in range(1, 3):
            n_gram_counter, n_gram_letter_counter = count_n_gram_apearance(n=i, text=text, alphabet=alphabet)

            
            # # Next line creates files for longtable in latex
            # n_gram_letter_counter = sorted(n_gram_letter_counter.items(), key=lambda x: x[1])
            # write_n_gram_letter_counter(n_gram_letter_counter, n=i)            

            print(f"Max(H): {math.log2(pow(len(alphabet), i))}")
            print(f"H = {calculate_H(n_gram_counter)}\n")

    

if __name__ == "__main__":
    # create_text()
    main()


