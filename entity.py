"""Entity class (something that is alive-ish)
"""

from stats import HasStats
from inventory import HasInventory

class Entity(HasStats,HasInventory):
    pass
