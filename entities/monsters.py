# == Trait Dictionary ==

MONSTER_TRAITS = {
    'puppet': {
        'resistances': ['blunt'],
        'weaknesses': ['slash', 'fire']
    }
}

class Monster:
    '''Monsters parameters are assigned here'''
    def __init__(mon, name: str, monster_type: str, attacks: str):
        mon.name = name
        mon.type = monster_type
        mon.attacks = attacks

        traits =  MONSTER_TRAITS.get(monster_type, {})
        mon.resistances = traits.get('resistances',[])
        mon.weaknesses = traits.get('weaknesses', [])

    def describe(mon):
        print(f"{mon.name} ({mon.type})")
        print(f"Attacks: {mon.attacks}")
        print(f"Resistances: {mon.resistances}")
        print(f"Weaknesses: {mon.weaknesses}")

class MonsterFactory:
    @staticmethod
    def create(monster_type, name, attacks):
        return Monster(name, monster_type, attacks)

marionette = MonsterFactory.create("puppet", "marionette", ['stab', 'electric'])

Monster.describe(marionette)