"""Player entity.
"""

import roll
from entity import Entity


class Player(Entity):
    
    def __init__(self):
        self.hp = 100
        self.speed = roll.roll(2,6)

