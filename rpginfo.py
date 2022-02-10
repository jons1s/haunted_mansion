#This class will add titles and credits to the role playing game (RPG) using a
#combination of instance, class and static methods.

#First create the class
class RPGInfo():
#Now we creat an 'instance method' for the specific game we are playing
#it will give a different title depending on the game being played
    
    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        print("Welcome to " + self.title)

    def instruction(self):
        print("\n\nUse the following instructions to move around in\n" + self.title)
        print("south, north, west, east")
        print("\nUse the following commands to interact with characters in\n" + self.title)
        print("talk, fight, heal")
        print("\nTo pickup objects in "+ self.title +" use 'take'")
        print("\nYou must defeat at least two characters to win the game in\n" + self.title)
        print("\nDon't let your health drop too low!")
        print("Use heal to get friendly characters to boost your health")
        print("\n\n************Good Luck*******\n\n")
#Now we create a 'static method' for the game generator message which
#will always be the same if using this program to create the RPG

    @staticmethod
    def info():
        print("Made using the FutureLearn Pi OOP RPG generator")
#Lastly we create a 'class method' for the end credits. The author can vary
#between different games but the author can also be responsible for different
#games

    author = ("anonymous")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print("Created by " + cls.author)
    
