import string
import random


class PasswordGenerator:

    @staticmethod
    def generate_pswd(password_length):
        pswd = ""
        lowercase = list(string.ascii_lowercase)
        uppercase = list(string.ascii_uppercase)
        digits = list(string.digits)
        spec_characters = [punct for punct in string.punctuation if punct not in
                           ["!", "\"", "\'", "<", ">", "[", "]", "`", "~", "{", "}", "(", ")", "|",]]
        all_characters = {'lowercase': lowercase, 'uppercase': uppercase,
                          'digits': digits, 'spec_characters': spec_characters}
        for i in range(0, password_length):
            character_type = random.choice(list(all_characters.keys()))
            pswd += random.choice(all_characters[character_type])
        return pswd


print(PasswordGenerator.generate_pswd(100))
