import math

class PalindromeFinder:
    @staticmethod
    def is_palindrome(phrase, ignore_spaces=True):
        if not isinstance(phrase, str):
            raise Exception("Wrong data type was passed as an argument")
        phrase = phrase.strip()
        if ignore_spaces:
            for character in phrase:
                if character == " ":
                    phrase = phrase.replace(character, "")
        phrase_length = len(phrase)
        half_to_check = math.ceil(phrase_length / 2)
        for character_index in range(0, half_to_check):
            if not phrase[character_index] == phrase[-character_index - 1]:
                print("This is not a palindrome")
                return
        print("This is a palindrome")
