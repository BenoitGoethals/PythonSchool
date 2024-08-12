#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas as pd


def read_dataframe(param):
    ret = pd.read_csv(param)
    return ret


def main():
    dat_dfa = read_dataframe("nato_phonetic_alphabet.csv")
    data = {value.letter: value.code for (index, value) in dat_dfa.iterrows()}
    word = input("Enter a word: ")
    nato_phonetic_alphabet = ' '.join([data.get(value.upper()) for value in word])
    print(nato_phonetic_alphabet)

if __name__ == '__main__':
    main()
