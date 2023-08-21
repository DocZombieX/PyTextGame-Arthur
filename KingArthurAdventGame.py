weapon = False
armor = False
bless = False
shield = False

#I felt it would be easier to read typing by definition and everything is for the most part self-contained.
def victory():
    print('Congratulations, Hero, you have defeated the demon and saved the world. Thank you for playing.')


def cathpalug():
    actions = ['fight', 'flee']
    global weapon
    print('A massive black and white spotted cat, much like a lion appears, a mouth lined with sharp teeth, '
          'three tails that split off from a single point, and six legs, it gives you a death stare.'
          'What would you like to do?')
    userInput = ''
    while userInput not in actions:
        print('options: fight/flee')
        userInput = input()
        if userInput == 'fight':
            if weapon:
                print('With one skillful swing of the Holy Sword Excalibur, a wound straight down the middle '
                      'of the fierce demon, shrieking in pain it crumbles to nothing')
            else:
                print('You and your soul have been vanquished by the demon, Hero no-more. The world comes to an end.')
                quit()
        elif userInput  == 'flee':
            print('A Hero does not run, the spirit of Cath Palug grabs your heart and consumes your soul.')
            quit()
        else:
            print('Enter a valid option.')

def holight():
    actions = ['fight', 'flee']
    global weapon
    print('An undead soldier that once was among your ranks, skilled in sword combat and clad in white shining armor'
          'Against pale, lifeless, torn flesh.')
    userInput = ''
    while userInput not in actions:
        print('options: fight/flee')
        userInput = input()
        if userInput == 'fight':
            if weapon:
                print('The Holy Sword glows with light as you swing it against the weak spot of the knight, '
                      'he crumbles into nothing')
            else:
                print('Lancelot, Tristan, and Percival would be disappointed. Goodbye would-be Hero. ')
                quit()
        elif userInput == 'flee':
            print('A Hero does not run, the spirit of Cath Palug grabs your heart and consumes your soul.')
            quit()
        else:
            print('Enter a valid option.')

def skeleton():
    actions = ['fight', 'flee']
    global weapon
    print('An undead who has risen from a grave. WIll you put them back in their place?')
    userInput = ''
    while userInput not in actions:
        print('options: fight/flee')
        userInput = input()
        if userInput == 'fight':
            if weapon:
                print('The Holy Sword glows with light as you swing it against the bones of the skeleton'
                      'cracking them to bits as the sword cuts it in two.')
            else:
                print('Lancelot, Tristan, and Percival would be disappointed. Goodbye would-be Hero. ')
                quit()
        elif userInput == 'flee':
            print('A Hero does not run, the spirit of Cath Palug grabs your heart and consumes your soul.')
            quit()
        else:
            print('Enter a valid option.')

def zombie():
    actions = ['fight', 'flee']
    global weapon
    print('An undead citizen of Camelot. Will you put them to rest?')
    userInput = ''
    while userInput not in actions:
        print('options: fight/flee')
        userInput = input()
        if userInput == 'fight':
            if weapon:
                print('The Holy Sword glows with light as you swing it against the decaying flesh of the dead'
                      'they feel nothing, for Arthur of Camelot has vanquished them.')
            else:
                print('Lancelot, Tristan, and Percival would be disappointed. Goodbye would-be Hero. ')
                quit()
        elif userInput == 'flee':
            print('A Hero does not run, the spirit of Cath Palug grabs your heart and consumes your soul.')
            quit()
        else:
            print('Enter a valid option.')

def monspi():
    actions = ['fight', 'flee']
    global weapon
    print('Once a normal spider, now it has both grown thorns and two feet taller, you steady your sword')
    userInput = ''
    while userInput not in actions:
        print('options: fight/flee')
        userInput = input()
        if userInput == 'fight':
            if weapon:
                print('The Holy Sword feels faster now against the creature, as you swing it and tear through its '
                      'thorny body, you feel the weight on you own shoulders.')
            else:
                print('Lancelot, Tristan, and Percival would be disappointed. Goodbye would-be Hero. ')
                quit()
        elif userInput == 'flee':
            print('A Hero does not run, the spirit of Cath Palug grabs your heart and consumes your soul.')
            quit()
        else:
            print('Enter a valid option.')

def devcat():
    actions = ['fight', 'flee']
    global weapon
    print('A monstrous black cat with acid drooling out of its mouth! Be careful!')
    userInput = ''
    while userInput not in actions:
        print('options: fight/flee')
        userInput = input()
        if userInput == 'fight':
            if weapon:
                print('The Holy Sword feels faster now against the creature, as you swing it and tear through its '
                      'thorny body, you feel the weight of death on your own shoulders.')
            else:
                print('Lancelot, Tristan, and Percival would be disappointed. Goodbye would-be Hero. ')
                quit()
        elif userInput == 'flee':
            print('A Hero does not run, the spirit of Cath Palug grabs your heart and consumes your soul.')
            quit()
        else:
            print('Enter a valid option.')

def stronghold():
    cathpalug_defeated = False

    while True:
        directions = ['forward']
        print('You feel insanity chipping away at your mind. You can only go forward.')
        userInput = ''
        while userInput not in directions:
            print('Options: forward')
            userInput = input()
            if userInput == 'forward':
                if not cathpalug_defeated:
                    cathpalug()
                    cathpalug_defeated = True
                elif cathpalug_defeated:
                    victory()
                continue
            else:
                print('Please enter a valid option.')

def thornpa():
    holight_defeated = False

    while True:
        directions = ['forward']
        print('The feeling of eyes watching you rips at your heart, a ghostly pressure makes you tense.')
        userInput = ''
        while userInput not in directions:
            print('Options: forward')
            userInput = input()
            if userInput == 'forward':
                if not holight_defeated:
                    holight()
                    holight_defeated = True
                elif holight_defeated == True:
                    stronghold()
                continue
            else:
                print('Please enter a valid option.')

def forest():
    monspi_defeated = False

    while True:
        directions = ['forward', 'return', 'check tree']
        print('Eyes fill the line of the forest. You can only go forward and turn back with return. A tree farther back'
              'looks suspicious, you may need to investigate.')
        userInput = ''
        while userInput not in directions:
            print('Options: forward, return, check tree')
            userInput = input()
            if userInput == 'forward':
                if not monspi_defeated:
                    monspi()
                    monspi_defeated = True
                continue
            elif userInput == 'return':
                camelot() # return to the main area
                return
            elif userInput == 'check tree':
                global armor
                armor = True
                print('You have received the golden armor of the legendary hero of Camelot, you feel the weight behind '
                      'the lost souls.')
            else:
                print('Please enter a valid option.')

def dungeon():
    zombie_defeated = False
    skeleton_defeated = False
    monspi_defeated = False

    while True:
        directions = ['forward', 'return']
        print('You feel the darkness surrounding you. You can only go forward and turn back with return.')
        userInput = ''
        while userInput not in directions:
            print('Options: forward, return')
            userInput = input()
            if userInput == 'forward':
                if not zombie_defeated:
                    zombie()
                    zombie_defeated = True
                if not skeleton_defeated:
                    skeleton()
                    skeleton_defeated = True
                if not monspi_defeated:
                    monspi()
                    monspi_defeated = True
                continue
            elif userInput == 'return':
                camelot() # return to the main area
                return
            else:
                print('Please enter a valid option.')


def cemetery():
    zombie_defeated = False
    skeleton_defeated = False

    while True:
        directions = ['forward', 'return', 'check grave']
        print('You see graves surrounding you, the dead scratching at the nerves on your neck, you can go forward and '
              'return. Weird, one of those graves is tilted, maybe you should check it.')
        userInput = ''
        while userInput not in directions:
            print('Options: forward, return, check grave')
            userInput = input()
            if userInput == 'forward':
                if not zombie_defeated:
                    zombie()
                    zombie_defeated = True
                if not skeleton_defeated:
                    skeleton()
                    skeleton_defeated = True

                continue
            elif userInput == 'check grave':
                global bless
                bless = True
                print('The blessing of the Hero fills your spirit!')
            elif userInput == 'return':
                camelot() # return to the main area
                return
            else:
                print('Please enter a valid option.')


def camelot():
    print('You see the chaos around you and the town square top be destroyed.')
    print('Options: north: A dark dungeon, south: a treacherous forest, west: A fiendish cemetery, east: ONE WAY, '
          'The Thorned Path. There\'s a sword in a mound, check the sword?')
    userInput = input()
    if userInput == 'check sword':
        global weapon
        weapon = True
        print('You have obtained the Holy Sword!')
        return camelot()
    elif userInput == 'north':
        return dungeon()
    elif userInput == 'south':
        return forest()
    elif userInput == 'west':
        return cemetery()
    elif userInput == 'east':
        return thornpa()
    else:
        print('Please enter a valid option.')
        return 'camelot'

# Other location functions similarly return next location

# Main game loop
if __name__ == "__main__":
    print("Welcome!")
    print('As the king of Camelot, you have returned from an adventure to find your kingdom overrun, can you save '
          'your kingdom and find what lay beyond?')
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " + name + ".")

    # Starting location
    location = camelot()

    # Main game loop
    while True:
        if location == 'camelot':
            location = camelot()
        elif location == 'forest':
            location = forest()
        elif location == 'dungeon':
            location = dungeon()
        elif location == 'cemetery':
            location = cemetery()
        elif location == 'thorned path':
            location = thornpa()
        elif location == 'stronghold':
            location = stronghold()
        break
