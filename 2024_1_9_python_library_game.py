# your current code below
'''
You are a hero in a dark system of caves full of trolls.
You have to find a magic spell book to destroy the caves and escape.
The game will involve an engine that runs a map full of rooms or scenes.
Each room will print its own description when the player enters it and
then tell the engine what room to run next out of the map.
'''

from random import randint #we only need the random integer function not the whole module
from sys import exit #we only need the exit function for quitting the game

class Hero():
    def __init__(self):
        self.book = None
        self.coin = 5
# starts the player out with 5 coins

class Engine():
    def __init__(self, scene_map):
        self.scene_map = scene_map
        # gets the game's map from instance "mymap," at bottom of this file
    def play(self):
        current_scene = self.scene_map.opening_scene()
        # see the Map object: this runs function named opening_scene()
        # this runs only once
        # this STARTS THE GAME

        while True:  # infinite loop to run the game - repeats until exit()
            print("\n--------")
            current_scene.enter()  # from Scene

            # note: will throw error if no new scene passed in by next line:
            next_scene_name = current_scene.action()

            # get the name of the next scene from the action() function that
            # runs in the current scene - what it returns

            current_scene = self.scene_map.next_scene(next_scene_name)
            #  here we use that val returned by current scene to go to
            #  the next scene, running function in Map

class Book(object):
    def __init__(self):
        self.activated = False

class Scene():
    name = 'unnamed scene'
    descrip = 'undescribed scene'

    def enter(self):
        print(self.name)
        print(self.descrip)

class GameOver(Scene):
    name = "You have died!"
    descrip = '''    You tried your best but did not succeed.\n'''

    def action(self):
        try:
            exit()  # exit the program
        except SystemExit:
            print("Game over.")

class CentralCorridor(Scene):
    '''
    A Troll is already standing here. Must be defeated
    before continuing.
    '''

    def __init__(self):
        self.troll = Troll()
        # initialize the corridor scene with a troll present

    name = "Central Corridor"
    descrip = '''    A broad passage extends in front of and behind you.
        There are doors to your left and right. There is a ladder going up and a slide going down.'''

    def action(self):
        if self.troll.present:
            print("    A troll is here.")
            self.troll.present, location = self.troll.fight(self.troll.stamina, self.troll.present)
            # catch the returns from fight() in Troll -
            # pass in stamina and present, get out present and current scene name
            return location
        else:
             while True:
                response = input("").lower()
                if "look" in response:
                    print(self.descrip)
                elif "up" in response:     # uncomment when implementing the Bridge scene
                    return 'bridge'
                elif "right" in response:
                    return 'library'
                elif "left" in response:   # uncomment when implementing the Cave scene
                    return 'cave'
                elif "down" in response:
                    return 'slide'
                elif "leave" in response or "exit" in response:
                    try:
                        exit()
                    except SystemExit:
                        print("Goodbye.")
                elif response != "":
                    print("Huh? I didn't understand that.")
                else:
                    print("Something went wrong ...")
                    return 'death'

class SpellBookLibrary(Scene):
    '''
    This is where the wizard gets a magic spell book to blow up the caves before
    getting to the escape route. It has a keypad you have to guess the number for.
    '''

    def __init__(self):
        self.doorlocked = True
        self.keycode = randint(1, 9) * 111  # 3 of the same number
        self.book = Book()
        # initialize the library scene with door locked and book here

    name = "SpellBook Library"
    descrip = '''    The door to this room is closed and locked.
    There is a digital keypad set into the wall.'''
    descrip2 = '''    Shelves and cases line the walls of this room.
    Spellbooks of every description fill the shelves and cases. '''

    def action(self):
        if self.doorlocked == True:
            self.keypad()
        while True:
            response = input(">").lower()
            if "look" in response:
                print(self.descrip)
            elif "book" in response and self.book:
                print("Searching the shelves, you discover a small red case.")
                print('On the case is a label: "Explodey Spell."')
                self.take_book()
            elif "book" in response and hero.book:
                print("You are carrying the book.")
            elif "leave" in response or "exit" in response:
                return 'corridor'
            elif response != "":
                print("Huh? I didn't understand that.")
            else:
                print("Something went wrong ...")
                return 'death'

    def take_book(self):
        while True:
            response = input(">").lower()
            if "case" in response or "open" in response:
                print("You open the case and look inside. Yep. It's a book!")
                print("You close the case. It has a convenient handle for carrying.")
            elif "take" in response or "pick up" in response:
                print("You pick up the case by its handle. It is not too heavy.")
                hero.book = self.book  # now book is being carried
                self.book = None  # and the book is no longer in the library
                return
            elif "activate" in response or "set" in response:
                print("I don't think you want to do that yet.")
            elif "book" in response:
                print("Do you want to do something with the book?")
            else:
                print("Huh? What?")

    # this should probably not be infinite - should have range instead
    # it does not let you out till you get it right
    def keypad(self):
        while self.doorlocked == True:
            print("The keypad has 9 buttons with numbers from 1 to 9.")
            print("3 numbers must be entered to unlock the door.")
            response = input(">").lower()
            if "leave" in response or "exit" in response:
                return 'corridor'
            elif not response.isdigit() or (int(response)> 999 or int(response) < 100):
                print("That is not a suitable number. Try again.")
            elif int(response) == self.keycode:
                self.doorlocked = False
                print("The door slides smoothly and quietly open.")
                self.descrip = self.descrip2  # switches the description text
                print(self.descrip)
            elif int(response)> self.keycode:
                print("That number is too high.")
            elif int(response) < self.keycode:
                print("That number is too low.")
            else:
                "No good. Try again with 3 numbers."

class Troll():
    def __init__(self):
        self.present = True
        self.stamina = 10

    def report(self, s):
        if s> 8:
            print("The troll is strong! It resists your pathetic attack!")
        elif s> 5:
            print("With a loud grunt, the troll stands firm.")
        elif s> 3:
            print("Your attack seems to be having an effect! The troll stumbles!")
        elif s> 0:
            print("The troll is certain to fall soon!")
        else:
            print("That's it! The troll is finished!")

#This part

    def fight(self, stam, p):  # stamina and present
        while p == True:
            response = input(">").lower()
            # fight scene
            if "hit" in response or "attack" in response:
                less = randint(0, stam)
                stam -= less  # subtract random int from stamina
                self.report(stam)  # see above
                if stam <= 0:
                    p = False
                    coins_earned = randint(100, 500)  # Store the random coin amount in a variable
                    hero.coin += coins_earned  # Add this amount to the hero's total coins
                    print(f"You defeated the troll and found {coins_earned} coins! You now have {hero.coin} coins in total.")  # Display both amounts to the player
                    return p, 'corridor'

                else:
                    pass
            elif "fight" in response:
                print("Fight how? You have no weapons, silly hero!")
            else:
                print("The troll hits you with its powerful stick!")
                return p, 'death'  # new, lowered stamina number

class Bridge(Scene):
    '''
    Another battle scene with a troll before the hero can place the explosion spell here.
    '''

    def __init__(self):
        self.troll = Troll()
        # initialize the corridor scene with a troll present
        self.book = None

    name = "The Bridge"
    descrip = '''    This is a giant underground bridge. You can see hundreds of
    trolls swarming toward you. Now is the time to use your spell book!
    You can take the ladder down to get away from them.'''

    def action(self):
        if self.troll.present:
            print("    Another troll is here!")
            self.troll.present, location = self.troll.fight(self.troll.stamina, self.troll.present)
            # catch the returns from fight() in Troll - same as fight in
            # corridor
            return location
        else:
            while True:
                response = input("").lower()
                if "look" in response:
                    print(self.descrip)
                elif "down" in response:
                    return 'corridor'
                elif "book" in response and hero.book:
                    self.activatebook()
                elif "book" in response and not hero.book:
                    print("That spell is set to blow! Get out!!")
                    # the order above is very important
                elif response != "":
                    print("Huh? I didn't understand that.")
                else:
                    print("Something went wrong ...")
                    return 'death'

    def activatebook(self):
        print("You set the case down and open it. You see a big spell book ")
        print('You do something to activate the spell book.')
        hero.book.activated = True
        print()
        print("I think you'd better hurry to get out of the caves!")
        # drop the book on the bridge
        self.book = hero.book
        hero.book = None
        return

class EscapeCave(Scene):
    '''
    Where the hero escapes, but only after guessing the right escape cave.
    '''
    name = "Escape Cave"
    descrip = '''    There are five tunnels leading to the outside of the caves.
    The tunnels are numbered 1 through 5.'''

    # This function describes code for each player-entered action
    def action(self):
        cavenum = randint(1, 5) # generates a random number between 1 and 5
        while True:
            response = input("").lower() # takes player input for which action the player wants to take


            if "look" in response:# if player chooses to look, description is displayed
                print(self.descrip)
            elif "go" in response:# if player chooses to go, appropriate action is taken for correct tunnel and incorrect tunnel
                choice = int(input("Which tunnel? ").lower())
                if choice == cavenum:
                    self.cave_escape()
                elif choice > 5:
                    print("There are only 5 tunnels!")
                else:
                    print("That tunnel seems to be full of rocks you can't get past.")
            elif "leave" in response or "exit" in response: # if player wants to exit the program, user enters leave or exit
                return 'corridor'
            elif response != "": # if player inputs an invalid choice, error message is displayed
                print("Huh? I didn't understand that.")
            else: # if player enters the incorrect tunnel the player dies
                print("Something went wrong ...")
                return 'death'

    def cave_escape(self): # if player enters the correct tunnel this function is called
        print("You escaped into the sunlight!")
        book_on_bridge = Map.scenes['bridge'].book
        if book_on_bridge and book_on_bridge.activated: # if bridge is activated the player can use his power and destroy the cave
            print("The caves explode in a million pieces, destroying all of ")
            print("the trolls and magic spell books left behind!")
            print("Safe in the sunlight, you walk away to claim your reward.\n")
            try:
                exit()  # avoid a traceback by catching the exit error
            except SystemExit:
                print("Game over.")
        else: # if the bridge is not activated the player is unable to use his power and dies, game over
            print("But did you forget something? The trolls are throwing rocks")
            print("at you! You never used your magic spell to destroy them!")
            print("That is the end of you!\n")
            try:
                exit()  # avoid a traceback by catching the exit error
            except SystemExit:
                print("Game over.")

# Unit 5 Activity 3
class Dragon:
  def __init__(self):
      self.alive = True
      self.stamina = 10

  def attack(self):
    if self.alive == True:
          less = randint(0, self.stamina)
          self.stamina -= less  # subtract random int from stamina
          print("You've attacked the dragon. Current stamina: ",self.stamina)
          if self.stamina == 0:
              self.alive = False
              print('The dragon has been defeated')

class SlideRoom:
  '''
  Where the hero can travel to the library, but must defeat a foe first.
  '''
  def __init__(self):
      self.name = "Slide Room"
      self.descrip = '''    You have now entered the layer of the dragon!  He is ready to fight!.'''
      self.dragon = Dragon()


  def enter(self):
      print(self.name)
      print(self.descrip)

  def action(self):
      if self.dragon.alive:
          print("To slay the dragon, you must 'attack' or 'hit' it!")

      while self.dragon.alive:
          user_input = input()

          if user_input in ['attack','hit','hit it']:
              self.dragon.attack()
     # code after here for getting coins and entering the library
          coins_earned = randint(100, 500)  # Store the random coin amount in a variable
          hero.coin += coins_earned  # Add this amount to the hero's total coins
          print(f"You defeated the dragon and earned {coins_earned} coins! You now have {hero.coin} coins in total.")  # Display both amounts to the player
          return 'library'

class BookLore():
    def __init__(self):
        self.passage = [
            "Be careful of what lies ahead of you.  For these passgaes hold secrets."
        ]

    def get_passage(self):
        return self.passage
        print(self)

    def action(self):
        if self.doorlocked == True:
            self.keypad()
        while True:
            response = input(">").lower()
            if "look" in response:
                print(self.descrip)
            elif "book 2" in response:
                print("Searching the shelves, you discover another book.")
                print('This book appears to be old and worn')
                self.read_book()
            elif "book" in response:
                print("You are carrying the book.")
            elif "leave" in response or "exit" in response:
                return 'corridor'
            elif response != "":
                print("Huh? I didn't understand that.")
            else:
                print("Something went wrong ...")
                return 'death'

    def read_book(self):
        while True:
            response = input(">").lower()
            if "read" in response or "open" in response:
                print("You take the book off the selve and open it.  It is certainly old.  Some pages are torn but you can still make out one line.")
                print(get_passage)
                return

# Map tells us where we are and where we can go
# it does not make us move - Engine does that
class Map():
    scenes = {
        'death'   : GameOver(),
        'corridor': CentralCorridor(),
        'library' : SpellBookLibrary(),
        'bridge'  : Bridge(),
        'cave'    : EscapeCave(),
        'slide'   : SlideRoom(),
    }

    def __init__(self, start_scene_key):
        self.start_scene_key = start_scene_key
        # above we make a local var named start_scene_key
        # this is a string, same as the arg we passed in ('corridor')
        # start_scene_key remains unchanged throughout the game

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        # above is how we get value out of the dictionary named scenes
        return val
        # this function can be called repeatedly in the game,
        # unlike opening_scene, which is called only ONCE

    def opening_scene(self):
        return self.next_scene(self.start_scene_key)
        # this function exists only for starting, using the first
        # string we passed in ('corridor')
        # it combines the previous 2 functions and is called only once
        # (called in Engine)

hero = Hero()
mymap = Map('corridor')  # instantiate a new Map object
mygame = Engine(mymap)  # instantiate a new Engine object
mygame.play()  # call function from that Engine instance