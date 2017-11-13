import random


class CowsAndBulls:
    def __init__(self, length=4):
        str_min = "1"
        str_max = ""
        for i in range(0, length - 1):
            str_min += "0"
        for i in range(0, length):
            str_max += "9"
        self._number = random.randint(int(str_min), int(str_max))

    def play(self, num=''):
        if not isinstance(num, str):
            num = str(num)
        cows = 0
        bulls = 0
        number_str = str(self._number)
        for i in range(0, len(number_str)):
            if number_str[i] == num[i]:
                cows += 1
            elif number_str[i] in num:
                bulls += 1
        if cows == len(number_str):
            print("Congratulations you won!")
        else:
            print("{0} cows and {1} bulls.".format(cows, bulls))


if __name__ == '__main__':
    cowsAndBulls = CowsAndBulls(5)
    cowsAndBulls.play("56787")
    cowsAndBulls.play(56787)
