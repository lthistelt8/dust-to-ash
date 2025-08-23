'''Controls everything to do with the combat itself'''

from battle import attack_types, enemy_loot, turn_order
from entities import player_characters, enemy_characters



def combat_loop(char1, enemy1):
    '''Combat loop'''
    inCombat = True

    while inCombat:
        turn_order.get_turn_order(char1, enemy1)
        action_list = ['Attack', 'Item']
        for a, action in enumerate(action_list, 1):
            print(f"{a}. {action}.")

        print("What would you like to do?")
        try:
            choice = int(input("> "))
        except ValueError:
            print("Must choose from the listed numbers!")
            return None

        if choice == 1:
            damage = char1.attack_enemy(enemy1)
            print(f"{char1.name} attacks {enemy1.name} for {damage} damage!")
            if enemy1.health == 0:
                print(f"{enemy1.name} defeated!")
                inCombat = False
                break
