from entity import Entity

class Creature(Entity):
    """Creature Base Class"""
    pass

class PitBog(Creature):
    """PitBog Creature"""
    hp = 50
    speed = 40
    attack = 70
    defense = 50
    special_defense = 50
    special_attack = 50

class FlameChick(Creature)
    """FlameChick Creature"""
    hp = 45
    speed =45
    attack = 60
    defense = 40
    special_defense = 40
    special_attack = 40
