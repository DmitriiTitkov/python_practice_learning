import random
import math


class GuessingGame:
    def __init__(self):
        self.numberToGuess = random.randint(0, 100)
        self.guessHistory = list()

    def compare(self, user_guess):
        if not isinstance(user_guess, int):
            raise ValueError("user guess argument should be int")
        if not self.guessHistory:
            difference = math.fabs(self.numberToGuess - user_guess)
            if difference == user_guess:
                print("Unbelievable luck!! You guessed! From the first try! are you cheating??")
                return True
            elif difference < 10:
                print("Hell's flame")
            elif difference < 20:
                print("Hot")
            elif difference < 40:
                print("Warm")
            elif difference < 60:
                print("Cold")
            elif difference < 80:
                print("Arctic")
        else:
            if math.fabs(self.numberToGuess - self.guessHistory[-1]) == math.fabs(self.numberToGuess - user_guess):
                print("Correct!!")
                return True
            elif math.fabs(self.numberToGuess - self.guessHistory[-1]) < math.fabs(self.numberToGuess - user_guess):
                print("Colder")
            else:
                print("Warmer")
        self.guessHistory.append(user_guess)
        return False


if __name__ == '__main__':
    print("I come up with number from one to hundred. Try to guess?")
    print("Input your number below or type 'q' for quit:")
    guess_game = GuessingGame()
    while True:
        input_user_guess = input()
        if input_user_guess == 'q':
            break
        elif input_user_guess:
            isCorrect = guess_game.compare(int(input_user_guess))
            if isCorrect:
                extra_game_user_answer = input("Wpuld you like play one more?[y/n]:")
                while True:
                    if extra_game_user_answer == 'y':
                        print("Input your number below or type 'q' for quit:")
                        break
                    else:
                        exit(0)
