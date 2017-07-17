import random


class Player:

    def __init__(self, name):
        self.player_name = name
        self.gesture = ""

    def set_gesture(self, gesture):
        gestures = ('rock', 'scissors', 'paper', 'lizard', 'spock')
        if gesture not in gestures:
            raise ValueError('Wrong value passed as an argument. Applicable values are: %s' % ({gestures}))
        self.gesture = gesture

    def compare(self, player):
        if not isinstance(player, Player):
            raise Exception("Wrong argument was passed to the function")
        elif self.gesture == player.gesture:
            print("DRAW for {0} and {1} with {2}".format(self.player_name, player.player_name, self.gesture))
        else:
            rules = {
                'rock': ('scissors', 'lizard'),
                'scissors': ('paper', 'lizard'),
                'paper': ('rock', 'spock'),
                'lizard': ('spock', 'paper'),
                'spock': ('scissors', 'rock')
            }
            wins = rules[self.gesture]
            winner = player.gesture in wins and self or player
            loser = player.gesture not in wins and self or player
            print("{0} wins with {1} of {2} with {3}".format(winner.player_name, winner.gesture, loser.player_name, loser.gesture))
            return winner


class ComputerPlayer(Player):

    def __init__(self):
        self.player_name = "Computer"
        self.gesture = ""

    def set_gesture(self):
        gestures = ('rock', 'scissors', 'paper', 'lizard', 'spock')
        self.gesture = gestures[random.randint(0, 4)]


if __name__ == '__main__':
    while True:
        print("Would you like to play with human or computer? \n 1 - Human \n 2 - Coumputer \n q - quit")
        answer = input("Enter your choice :")
        if answer == '1' or answer == '2':
            print("Please enter players names:")
            player1 = Player(input("Player1 name:"))
            if answer == 1:
                player2 = Player(input("Player2 name:"))
            else:
                player2 = ComputerPlayer()
            print("GAME:")
            while True:
                while not player1.gesture:
                    try:
                        player1.set_gesture(input("{0} chose you move:".format(player1.player_name)))
                    except ValueError:
                        print("Enter other value. Availiable values are 'rock', 'scissors', 'paper', 'lizard', 'spock'")
                if answer == 1:
                    while not player2.gesture:
                        try:
                            player2.set_gesture(input("{0} chose you move:".format(player2.player_name)))
                        except ValueError:
                            print("Enter other value. Availiable values are 'rock', 'scissors', 'paper', 'lizard', 'spock'")
                else:
                    player2.set_gesture()
                player1.compare(player2)
                repeat = input("One more game?[y/n]:")
                if repeat == 'n':
                    break
                else:
                    repeat = ''
                    player1.gesture = None
                    player2.gesture = None
        if answer == '2':
            print("test")
        if answer == "q":
            break



