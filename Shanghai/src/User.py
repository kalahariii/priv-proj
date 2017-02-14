# A class to parse the orignial input into an array of clean(no blanc spaces) strings
class User:
    users = ""

    def __init__(self, userString):
        self.users = self.parse_str(userString)

    @classmethod
    def parse_str(cls, uString):
        #fancy list comprehension magic, looks like Haskell but feels wrong
        return [x.strip() for x in uString.split(',')]

    def get_users(self):
        return self.users
#a test that WORKS!
#usr = User("Max, Karl")
#print(usr.get_users())
