class controller:
    def __init__(self, user):
        self.users = {user : "Greetings"}
    def play(self,user):
        self.users[user] = "Playing"
    def finish(self, user):
        self.users[user] = "Finish"