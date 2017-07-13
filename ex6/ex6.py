import math

class PalindromeFinder:
    @staticmethod
    def is_palindrome(phrase):
        phrase_length = len(phrase)
        half_to_check = math.ceil(phrase_length / 2)
        for character_index in range(0, half_to_check):
            if not phrase[character_index] == phrase[-character_index - 1]:
                print("This is not a palindrome")
                return False

                print("This is a palindrome")
