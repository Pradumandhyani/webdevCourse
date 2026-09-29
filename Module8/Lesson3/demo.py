class john:
    def __init__(self,name,aim):
        self.name=name
        self.aim=aim

    def aims(self):
        return "hi my aim is {}".format(self.aim)

arthur=john("avinab","developer")
print(arthur.aims())