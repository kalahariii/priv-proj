from User import *

# A class to store the scores to all players
class Table:
    table = {}
#    users

    def __init__(self, users):
        self.users = users
        # This one's actually pretty cool
        # Python seems to have this light version of a Hasmap
        # You can set your key an value with ease
        for usr in users:
            # setting all scores to 0 as you inialize the table
            self.table[usr] = 0

    # simple method to add score to a player
    def update_table(self, usr, value):
        self.table[usr] += value

    # prints entire table with all players and their scores
    def load_standings(self):
        for usr in self.users:
            print usr + str(self.table[usr])
        print "Game on!"
