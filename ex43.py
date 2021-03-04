from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()
class Death(Scene):

    quips = [
        "You died",
        "You lost"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("Central Corridor")
        print("")
        action = input("> ")
        if action == "shoot":
            print("You miss")
            print("You get eaten")
            return 'death'
        elif action == 'dodge':
            print("You slip and fall")
            print("You get crushed")
            return 'death'
        elif action == 'tell a joke':
            print("The alien finds you funny")
            print("You make it to the Weapons Armory")
            return 'laser_weapon_armory'    
        else:
            print("Error")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print("Guess the combination to the bomb in the armory")
        code = f"{randint(1,3)}{randint(1,3)}{randint(1,3)}"
        print(code)
        guess = input("[keypad]> ")
        num_guesses = 0

        while guess != code and num_guesses < 10:
            print("BZZZZZZZZZZZZ")
            num_guesses += 1
            guess = input("[keypad]> ")
        
        if (guess == code):
            print("You take the bomb to the bridge")
            return "the_bridge"
        else:
            print("The bomb blows up")
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print("You see 5 gothons")

        action = input("> ")

        if action == 'throw the bomb':
            print("The gothons shoot you")
            return 'death'
        elif action == 'slowly place the bomb':
            print("You place the bomb down and run away to the escape pod")
            return 'escape_pod'
        else:
            print("error")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print("pick an escape pod")

        good_pod = randint(1,5)
        guess = input("> ")
        if guess != good_pod:
            print("Your pod blows up")
            return 'death'
        else:
            print("You successfully escaped!")
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won!")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'finished' : Finished(),
        'death' : Death()

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)    

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()