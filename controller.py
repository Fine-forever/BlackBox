class controller:
    _instance = None
    def __init__(self, user):
        self.users = {user : "Greetings"}
    def play(self,user):
        self.users[user] = "Playing"
    def finish(self, user):
        self.users[user] = "Finish"
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = controller(user)
        return cls._instance
