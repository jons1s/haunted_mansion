class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description + "\n")

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    # character can't heal
    def healing(self,health):
        print(self.name +" says 'Heal yourself'. Health remains = ", health)
        return health
    
    
#create an enemy character
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.defeats = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def set_defeats(self, defeats):
        self.defeats = defeats

    def get_defeats(self):
        return self.defeats

    def fight(self, combat_item):
        if self.defeats > 0:
            print(self.name + " doesn't want to fight with you anymore")
            return True
        if combat_item == self.weakness:
            print("You fend off " + self.name + " with a " + combat_item)
            self.set_defeats(1)
            return True
        
        else:
            print(self.name + " crushes you, you puny wizard")
            return False

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def healing(self,health):
            health = health + 1
            print("Health is now ",health)
            return health
            
    
