import random


def _digit_validator(func):
    def _decorator(self, *args):
        if type(self.playTable[args[0]]) is list:
            return func(self, *args)
        else:
            return func(self, args[0] + 1)
    return _decorator


class CowsAndBulls:
    def __init__(self, length=4):
        self.set_number(length)
        self.playTable = list()
        self.lastBet = ""
        self.currentBet = ""
        self.cows = 0
        self.bulls = 0
        self._rolledDigit = ''

    def set_number(self, length):
        str_min = "1"
        str_max = ""
        for i in range(0, length - 1):
            str_min += "0"
        for i in range(0, length):
            str_max += "9"
        self._number = random.randint(int(str_min), int(str_max))

    def guess(self, num=''):
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

    def play(self, length, cows=0, bulls=0):
        bet = list()
        #playTable is not defined. The first guess
        if not self.playTable:
            self._set_playtable(length)
            return self._bet_constructor('firstBet')
        else:
            # rolledDigit is '' so it must be second guess
            if isinstance(self._rolledDigit, str):

                return self._bet_constructor('roll', cows=cows, bulls=bulls)
            #Number of cows has changed
            if cows > self.cows:
                self.playTable[self._rolledDigit] = self.currentBet[self._rolledDigit]
                return self._bet_constructor('roll', cows=cows, bulls=bulls)
            elif cows < self.cows:
                self.playTable[self._rolledDigit] = self.lastBet[self._rolledDigit]
                self.currentBet[self._rolledDigit] = self.lastBet[self._rolledDigit]
                return self._bet_constructor('roll', cows=self.cows, bulls=bulls)
            else:
                if self.bulls == bulls:
                    return self._bet_constructor('roll', cows=cows, bulls=bulls)
                if self.bulls > bulls:
                    return self._bet_constructor('swap', cows=cows, bulls=bulls)
                else:
                    ""
    def _set_playtable(self, length):
        for i in range(0, length):
            self.playTable.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    def _bet_constructor(self, action, **kwargs):
        for name, value in kwargs.items():
            self.__setattr__(name, value)
        if action == "firstBet":
            bet = list()
            for i in range(0, len(self.playTable)):
                self.currentBet = bet
                bet.append(random.choice(self.playTable[i]))
            return bet
        if action == 'roll':
            if self._rolledDigit == '':
                self.lastBet = self.currentBet[:]
                self.currentBet[0] = self._roll_digit(0)
                return self.currentBet
            else:
                self.currentBet[self._rolledDigit] = self._roll_digit(self._rolledDigit)
                return self.currentBet
        if action == 'swap':
            return self._swap_digit(self, self._rolledDigit + 1)

    @_digit_validator
    def _roll_digit(self, position):
        self._rolledDigit = position
        if len(self.playTable[position]) > 1:
            self.playTable[position].remove(int(self.currentBet[position]))
            return random.choice(self.playTable[position])
        else:
            print('Are you cheating?')

    @_digit_validator
    def _swap_digit(self, position):
        copy_var = self.currentBet[self._rolledDigit]
        self.currentBet[self._rolledDigit] = self.currentBet[position]
        self.currentBet[position] = copy_var
        return  self.currentBet






#if __name__ == '__main__':
cowsAndBulls = CowsAndBulls(5)
print(cowsAndBulls.play(4))
#print(cowsAndBulls.play(4, 1, 0))
#print(cowsAndBulls.play(4, 0, 0))
#print(cowsAndBulls.play(4, 3, 0))
#print(cowsAndBulls.play(4, 4, 0))

#print("I picked up a {0}-digit number. Can you guess it?".format(length))
