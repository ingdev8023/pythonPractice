from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]
    
    def make_move(self):
        move = random.choice(self.moves)
        self.position = tuple(map(sum, zip(self.position, move)))
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1), (0,-1),(-1, 0), (1, 0)]

    def level_up(self):
        self.moves.extend([(1,1), (1,-1), (-1,1), (-1,-1)])


test1 = Pawn()
test2 = [(0,1), (0,-1),(-1, 0), (1, 0)]
test3 = (-1,0)
test4 = random.choice(test2)

test3 = tuple(map(sum, zip(test3, test4)))
print(test1.make_move())
print(test1.make_move())
print(test1.make_move())
print(test1.make_move())
print(test1.position)
print(test1.path)
print(test1.moves)
test1.level_up()
print(test1.moves)


