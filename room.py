#create rooms in haunted mansion
class Room():
    def __init__(self, room_name):
        self.name = room_name
        #set initial room descriptions to none or empty
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
    #setter and getter for room name    
    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name
    #setter and getter for room description
    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)
    #setter and getter for characters in room 
    def set_character(self, character_name):
        self.character = character_name

    def get_character(self):
        return self.character
    #setter and getter for items in room
    def set_item(self, item_name):
        self.item = item_name

    def get_item(self):
        return self.item
    #exits from room
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
    
    #getter for room directions
    def get_details(self):
        print("*********************")
        print(self.name)
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
        print("\n")
    #move to next room
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self



    
