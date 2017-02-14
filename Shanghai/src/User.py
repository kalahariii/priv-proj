# A class to parse the orignial input into an array of clean(no blanc spaces) strings
class User:
    users = ""

    def __init__(self, userString):
        self.users = self.parse_users(userString)

    def parse_users(self, uString):
        # fancy list comprehension magic, that looks like Haskell, but feels wrong
        return [x.strip() for x in uString.split(',')]

    def get_users(self):
        return self.users
#a test that WORKS!
#usr = User("Max, Karl")
#print(usr.get_users())
