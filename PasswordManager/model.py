import random
import string
class PasswordGenerator:


    @staticmethod
    def GenerateRandomPassword(lenght_letters, lenght_numbers, lenght_symbols):
        count_letters = 0
        count_numbers = 0
        count_symbols = 0
        password = ""
        while (lenght_letters + lenght_numbers + lenght_symbols) > (count_letters + count_numbers + count_symbols):
            choice_type = random.randint(0, 2)
            if choice_type == 0 and count_letters < lenght_letters:
                password += random.choice(string.ascii_letters)
                count_letters += 1
            elif choice_type == 1 and count_numbers < lenght_numbers:
                password += random.choice(string.digits)
                count_numbers += 1
            elif choice_type == 2 and count_symbols < lenght_symbols:
                password += random.choice(string.punctuation)
                count_symbols += 1
        return password