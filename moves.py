
class Move():
    entity = None
    accuracy = None

class Tackle(Move):
    accuracy = 100
    damage = 35

    def do(self,target):
        # TODO self.applybuffs()
        # TODO self.applydebuffs
        rolled = dice.roll(1,100)
        if self.accuracy >= rolled
            target.hp -=


class Growl(Move):
    pass

class Scratch(Move):
    pass

