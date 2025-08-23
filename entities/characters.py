'''Blueprint for player and enemy characters'''
class Character():
    '''Methods shared across enemies and players'''
    def __init__(self, name, health=1, attack=1, defense=1, speed=1, resistances = None, weaknesses = None, attack_type = None):
        self.name: str = name
        self.health: int = health
        self.attack: int = attack
        self.defense: int = defense
        self.speed: int = speed
        self.attack_type = attack_type

        resistances = resistances if not None else []
        weaknesses = weaknesses if not None else []

    def take_damage(self, damage):
        '''Take damage, reducing health'''
        self.health -= damage
        self.health = max(self.health, 0)

    def attack_enemy(self, enemy):
        '''Attack enemy based on health and defense'''
        damage = max(0, self.attack - enemy.defense)
        enemy.take_damage(damage)
        return damage

class PlayerCharacter(Character):
    '''Player character methods'''
    super(Character)

class EnemyCharacter(Character):
    '''Enemy character methods'''
    super(Character)
