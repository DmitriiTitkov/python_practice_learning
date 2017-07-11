import math

class DivisorFinder:
    #def __init__(self):

    @staticmethod
    def get_divisor(num):
        square_root = math.floor(math.sqrt(num))
        check_range = range(2, square_root)
        divisors = set()
        divisors.add(1)
        divisors.add(num)
        for check_num in check_range:
            remnant = num % check_num
            if remnant == 0:
                divisors.add(check_num)
                divisors.add(num//check_num)
        return divisors



