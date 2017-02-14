from User       import *
from Table      import *
# Yes, here we go! This class carries the game
class Game:
        # Some local variables
        # not sure if you really don't have to set them private or something like that
        # for now I will enjoy some cheeky, non specified variables
        nextRound   = True
#        users
#        table
        i = 0
        zahlArr = [15,-1,2,-1]
        j = 0
        txtArr  = ["Double","Bullseye"]
#       numBool

        # simple constructor
        def __init__(self, users):
            self.users  = users.get_users()
            self.table  = Table(users.get_users())

        # this method is kind of the -Kick Off- of this game
        def start(self):
            self.user_display(self.users)
            self.thread()

        def thread(self):
            while self.nextRound:
                self.next_field()
            self.game_over()

        # displaying all players in the Game
        def user_display(self, uString):
            print "Game with:"
            for usr in uString:
                print usr + ', ',
            print

        # changes field
        def next_field(self):
            # every user will write his score
            # sets numBool, nextRound and prints Field
            self.check_field()
            if self.numBool:
                self.collect_scores_norm(self.zahlArr[self.i])
                self.i += 1
            else:
                self.collect_scores_spec()
                self.j += 1
                self.i += 1

        # collecting scores on ordinary turns
        def collect_scores_norm(self, num):
            for usr in self.users:
                if self.nextRound:
                    txt   = usr + " scores: "
                    score = input(txt)
                    self.check_shanghai(usr, score)
                    if self.nextRound:
                        self.table.update_table(usr, score, num)
            if self.nextRound:
                self.update_standings()

        # collecting scores on special turns
        def collect_scores_spec(self):
            txt = self.txtArr[self.j]
            if txt == "Double":
                self.collect_double()
            elif txt == "Bullseye":
                self.collect_bull()

        def collect_double(self):
            print("Write the Fields you hit like you did with the names.")
            for usr in self.users:
                if self.nextRound:
                    txt = usr + " scores: "
                    score = User.parse_str(input(txt))
                    self.check_shanghai(usr, score[0])
                    if self.nextRound:
                        if (len(score) > 3):
                            self.error_retry()
                        self.table.update_table_spec(usr, score, 2)
            if self.nextRound:
                self.update_standings()
                
        def collect_bull(self):
            self.collect_scores_norm(25)

        # In case one hits a triple, a double and a single 
        # he s``cores -Shanghai- and claims victory
        def check_shanghai(self, usr, score):
            scrStr = str(score)
            if (scrStr[0] == 'S' or scrStr[0] == 's'):
                print(usr + " has won the Game with a Shanghai, well done!")
                self.game_over()

        # checking for fieldposition
        def check_field(self):
            self.update()
            if self.zahlArr[self.i] < 0:
                print(self.txtArr[self.j])
                self.numBool = False
            else:
                print(str(self.zahlArr[self.i]))
                self.numBool = True

        # updates nextRound
        def update(self):
            if self.i >= (len(self.zahlArr) - 1):
                self.nextRound = False
            print "Another round\nNext Field: ",

        # telling the user, that the game has ended
        def game_over(self):
            self.nextRound = False
            print "Game over!\nFinal standings:\n"
            self.update_standings()

        # error message in case you should've typed something impossible
        def error_retry(self):
            print("invalid input, restarting Field")
            self.next_field()

        # getting the standing from the table object
        def update_standings(self):
            self.table.load_standings()
