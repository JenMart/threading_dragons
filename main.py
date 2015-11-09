import threading
import time
import random


#
#   Dragon attributes
#
DRAGON_SCALES = ['gold', 'black', 'metallic', 'silver', 'shiny', 'stone', 'marble', 'obsidian', 'titanium', 'steel',
                'iron', 'rose gold', 'copper', 'bronze', 'shimmery', 'dusty', 'rusted', 'white', 'red', 'blue', 'green']
DRAGON_AGES = ['whelp', 'drake', 'dragon', 'dragon', 'dragon', 'wyrm']
DRAGON_POWERS = ['frost breath', 'fire breath', 'poison breath', 'sharp claws', 'barbed tail', 'gravity ball']

DRAGON_NAMES_PREFIX = ['Scale', 'Flame', 'Fire', 'Fury', 'Talon', 'Whip', 'Star', 'Vain', 'Glitter']
DRAGON_NAMES_SUFFIX = ['ette', 'seeker', 'breather', 'lasher', 'gloom', 'dust', 'ling']


#
#   Dragon
#   It's just a collection of random choices from the above lists.
#
class Dragon:
    def __init__(self, number):
        self.scales = random.choice(DRAGON_SCALES)
        self.age = random.choice(DRAGON_AGES)
        self.power = random.choice(DRAGON_POWERS)
        self.name = random.choice(DRAGON_NAMES_PREFIX) + random.choice(DRAGON_NAMES_SUFFIX)
        self.number = number

    def roar(self):
        print ' '.join(['The', self.scales, self.age, 'roars out, "I AM', self.name.upper() + '! BEWARE MY FEARSOME',
                        self.power.upper() + '!"'])

    def encounter(self):
        print ' '.join(['\nA', self.scales, self.age, 'emerges from the darkness.'])


#
#   spawn_dragon
#   Spawns a new dragon, makes it wait for an offset, then prints out its (semi) unique attributes.
#   Shows how threads can work simultaneously.
#
def spawn_dragon(i):
    d = Dragon(i)
    time.sleep(i)
    d.encounter()
    time.sleep(.5)
    d.roar()


#
#   main
#   Generates several threads.
#
def main():
    for i in range(5):
        t = threading.Thread(target=spawn_dragon, args=(i,))
        t.start()


main()
