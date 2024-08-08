alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']



def encrypt(value, shift):
   a_value = [*value]
   for i,t in enumerate(a_value):
       a_value[i] = alphabet[alphabet.index(t)+shift]
   return ''.join(a_value)



def dencrypt(value, shift):
    a_value = [*value]
    for i, t in enumerate(a_value):
        a_value[i] = alphabet[alphabet.index(t)-shift]
    return ''.join(a_value)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26
if direction == 'encode' or direction == 'e':
    ret = encrypt(text, shift)
else:
    ret = dencrypt(text, shift)

print(ret)
