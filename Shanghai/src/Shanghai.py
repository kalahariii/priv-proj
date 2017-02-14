from User import *
from Game import *

class Shanghai:
    #game

    # recalls main() if the first char is an y/Y
    def rematch(self, remStr):
        if (remStr[0] == 'y' or remStr[0] == 'Y'):
            self.main()
    
    def main(self):
        # Have the user set his players
        userStr = input("Sie die Namen aller Spieler ein, trennen sie diese durch Kommata:\n")
        # The String will now be parsed and the game gets started
        users   = User(userStr)
        print("I have parsed the input sting and created a User object")
        game = Game(users)
        print("I have constructed a game")
        game.start()
        # After the game the user is left with the option of a rematch, only if he fancies though..
        remStr  = input("rematch? (y/N)\n")
        self.rematch(remStr)

game = Shanghai()
game.main()
