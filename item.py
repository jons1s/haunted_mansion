#Create some items for inside the rooms
class Item():
    
    def __init__(self, item_name):
        self.name = item_name
        #set initial description to none
        self.description = None
        self.colour = None
    #setters and getters for item name
    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name
    #setters and getters for description of item
    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description
    #setters and getters for colour of item
    def set_colour(self, item_colour):
        self.colour = item_colour

    def get_colour(self):
        return self.colour
    #printing item and description
    def describe(self):
        print("You see a " + self.name)
        print(self.description)
        print("It is coloured " + self.colour + "\n")


