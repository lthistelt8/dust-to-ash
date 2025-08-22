'''Blueprint for player and enemy characters'''
class Character():
    '''Methods shared across enemies and players'''
    def __init__(self, name, health=1, attack=1, defense=1, speed=1):
        self.name: str = name
        self.health: int = health
        self.attack: int = attack
        self.defense: int = defense
        self.speed: int = speed

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
    pass

class EnemyCharacter(Character):
    '''Enemy character methods'''
    super(Character)
    pass

char1 = PlayerCharacter('char1')
enemy1 = EnemyCharacter('enemy1')
char1.attack_enemy('enemy1')
enemy1.take_damage(enemy1)