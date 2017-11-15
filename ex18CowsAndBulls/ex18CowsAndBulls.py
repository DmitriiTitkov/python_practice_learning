import random


class CowsAndBulls:
    def __init__(self, length=4):
        self.set_number(length)
        self.playTable = list()
        self.lastBet = ""
        self.currentBet = ""
        self.cows = 0
        self.bulls = 0
        self._rolledDigit = int()

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
        bet = self.currentBet
        #playTable is not defined. The first guess
        if not self.playTable:
            for i in range(0, length):
                self.playTable.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
                bet += str(random.randint(0, 9))
            self.currentBet = bet
            return bet
        else:
            #Number of cows has changed
            if cows > self.cows:
                self.playTable[self._rolledDigit]= self.currentBet[self._rolledDigit]
            elif cows < self.cows
                self.playTable[self._rolledDigit] = self.lastBet[self._rolledDigit]
            else:
                if self._rolledDigit:
                    bet[self._rolledDigit] = self._rollDigit(self._rolledDigit)

    def _rollDigit(self, position):
        self._rolledDigit = position








#if __name__ == '__main__':
cowsAndBulls = CowsAndBulls(5)
cowsAndBulls.guess("56787")
cowsAndBulls.guess(56787)
print(cowsAndBulls.play(5))
#print("I picked up a {0}-digit number. Can you guess it?".format(length))
