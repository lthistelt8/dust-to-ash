'''Controls turn order in combat'''
from entities import enemy_characters, player_characters

def get_turn_order(fighters):
    '''Returns turn order'''
    
    fighters = [player_characters.char1] + [enemy_characters.enemy1]

    turn_order = sorted(fighters, key= lambda c: c.speed, reverse=True)
    return turn_order
