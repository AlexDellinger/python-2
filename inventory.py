"""Inventory related stuff
"""

class HasInventory():
    items = []

    def carry_weight(self):
        weight = 0
        for items in items:
            weight += item.weight
        return weight
