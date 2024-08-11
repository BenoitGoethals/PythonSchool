import string

numbers = range(1, 100)

data = [n for n in numbers if n % 2 == 0]

print(data)

word = "Benoit"


def convert(l: str):
    if l in string.ascii_uppercase:
        return l.lower()
    else:
        return l.upper()


new_word = [convert(n) for n in word if n != 'e']
print(''.join(new_word))
