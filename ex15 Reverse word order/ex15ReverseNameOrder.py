class ReversedString:

    @staticmethod
    def reverse_words(straight_string):
        words = list(straight_string.split())
        words.reverse()
        return " ".join(words)

print(ReversedString.reverse_words("This is a strange test string, a long one"))