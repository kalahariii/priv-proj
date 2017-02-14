from User import *
from Table import *
# Yes, here we go! This class carries the game
class Game:
        # Some local variables
        # not sure if you really don't have to set them private or something like that
        # for now I will enjoy some cheeky, non specified variables
        counter     = 0
        nextRound   = True
#        users
#        table

        # simple constructor
        def __init__(self, users):
            self.users  = users.get_users()
            self.table  = Table(users.get_users())

        # this method is kind of the -Kick Off- of this game
        def start(self):
            self.user_display(self.users)
            while self.nextRound:
                self.next_field()
                self.counter += 1
            self.game_over()

        # displaying all players in the Game
        def user_display(self, uString):
            print "Game with:"
            for usr in uString:
                print usr + ', ',
            print

        # changes field
        # TODO: Find a smart way to change between the fields. If there's one..
        def next_field(self):
            print "Another round"
            if self.counter > 4:
                self.nextRound = False
            # as long as the counter is smaller than 5
            # every user will write his score
            for usr in self.users:
                txt   = usr + " scores: "
                score = input(txt)
                self.table.update_table(usr, score)
            self.update_standings()

        def game_over(self):
            print "Game over!\nFinal standings:\n"
            self.update_standings()

        # getting the standings from the table object
        def update_standings(self):
            self.table.load_standings()
