'''List of all player characters + attributes'''

from characters import PlayerCharacter
from battle.attack_types import ATTACK_TYPES

char1 = PlayerCharacter('char1')
char1.attack_type = 'blunt'
if char1.attack_type not in ATTACK_TYPES:
    char1.attack_type = 'strike'

print(char1)
