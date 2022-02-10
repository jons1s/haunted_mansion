#import classes
from room import Room
from rpginfo import RPGInfo
from item import Item
from character import Friend
from character import Enemy
#create object haunted mansion
haunted_mansion = RPGInfo("____The Haunted Mansion____")
#call instance method welcome()
haunted_mansion.welcome()
haunted_mansion.instruction()
#call static game generator message 
RPGInfo.info()
#call room to make new rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
dungeon = Room("Dungeon")
#describe the rooms
kitchen.set_description("A dank and dirty place, buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks gaurd the door")
dining_hall.set_description("A large room with ornate golden decorations on each wall")
dungeon.set_description("A large echoing dark windowless space")
#link the rooms
kitchen.link_room(dining_hall,"south")
ballroom.link_room(dining_hall,"east")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ballroom,"west")
dining_hall.link_room(dungeon,"east")
dungeon.link_room(dining_hall,"west")
#define some unfriendly characters to fight
dave = Enemy("Dave","A smelly Zombie!")
dining_hall.set_character(dave)
dave.set_conversation("Aaaa.....gh, br.......ains")
dave.set_weakness("spell")
dave.set_defeats(0)

dragon = Enemy("A fire breathing dragon", "Sleeping soundly")
dungeon.set_character(dragon)
dragon.set_conversation("Zzzzzzz")
dragon.set_weakness("sword")
dragon.set_defeats(0)
#define some friendly characters to assist you
anna = Friend("Anna","A freindly ghost who once was a nurse")
ballroom.set_character(anna)
anna.set_conversation("You look poorly, can I assist?")
#define some items and where to find them
sword = Item("sword")
sword.set_description("A rusty, blunt old cutlass")
sword.set_colour("sky blue purple") 
kitchen.set_item(sword)

spell = Item("spell")
spell.set_description("An old well thumbed book of spells")
spell.set_colour("Silver") 
dining_hall.set_item(spell)

candelstick = Item("candlestick")
candelstick.set_description("It has three candles in it")
candelstick.set_colour("Golden") 
ballroom.set_item(candelstick)

gold = Item("gold")
gold.set_description("A dragons hoard of golden coins")
gold.set_colour("deepest gold")
dungeon.set_item(gold)

#set variables for player's health, location, wins and backpack contents
health = 5
wins = 0
current_room = kitchen
backpack = [ ]
#set flag to allow exit from main program loop
flag = True

#main program loop
while flag == True:
    #keep an eye on your health
    print("\n")
    print("your health is ",health)
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    wins = dave.get_defeats() + dragon.get_defeats()
    #check if you have won
    if wins >1:
        print("You have defeated ",wins," opponents.")
        print("**** Congratulations You Win the game ****\n\n")
        break
    #check who and what is in room
    if inhabitant is not None:
        inhabitant.describe()
    if item is not None:
        item.describe()
    #get player input
    command=input(">")
    if command in ["north","south","east","west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        inhabitant.talk()
    elif command == "fight":
        health = health - 2
        print("What will you fight with?")
        weapon = input()
        #check weapon in backpack
        if weapon in backpack:
            flag = inhabitant.fight(weapon)
        if weapon not in backpack:
            print("Ooops that's not in your backpack\n" + inhabitant.name + " attacks you")
            health = 0
        if health <= 0:
            print("Your health has now fallen too low so.....")
            break
    #replenish health
    elif command=="heal":
        health=inhabitant.healing(health)
    #pick up object and place in backpack
    elif command=="take":
        backpack.append(item.get_name())
        print("your backpack contains ",  backpack )
        current_room.set_item(None)
    
#check if exited main loop because won if not you lost
if wins < 2:
    print("You died.........\n***********************\n" )   
#print credits        
RPGInfo.author = "Raspberry Pi Foundation"
RPGInfo.credits()
