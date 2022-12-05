import const
import random
from rl.block import Block


class Area:

    def __init__(self, world, situation=None, add_actor=None):
        self.world = world
        self.situation = situation
        self.addActor = add_actor
        self.blocks = []
        self.situation_iterations = 0
        self.removed_series = 0
        self.generateStart()

    def generateStart(self):
        # генерируем просто набор блоков
        dx = 0
        for i in range(10):
            self.generateBlock(dx, 0)
            dx += const.BLOCK_SIZE

#        self.generateRandom(dx)
        if self.situation is not None:
            self.is_infinity = False
            self.situation_iterations = 18
            dx = self.generateSituation(dx)
            dx = self.generateSituation(dx)
            dx = self.generateSituation(dx)
        else:
            self.is_infinity = True
            self.generateRandom(dx)

    def generateRandom(self, x):
        while x < const.WIDTH * 1.5:
            self.generateBlock(x, const.BLOCK_TYPES)
            x += const.BLOCK_SIZE
        return x

    def generateSituation(self, x):
        for i in self.situation:
            y = (2-i) * const.BLOCK_SIZE + const.HEIGHT - 2.5 * const.BLOCK_SIZE
            block = Block(x, y, self)
            self.blocks.append(block)
            if self.addActor is not None:
                self.addActor(block)
            x += const.BLOCK_SIZE

        return x

    def generateBlock(self, x, r):
        # генерация одного блока на какойто высоте
        y = (2 - random.randint(0, r)) * const.BLOCK_SIZE + const.HEIGHT - 2.5 * const.BLOCK_SIZE
        block = Block(x, y, self)
        self.blocks.append(block)
        if self.addActor is not None:
            self.addActor(block)

    def remove(self, block):
        self.blocks.remove(block)
        # должны добавить новый блок, только понять куда
        if self.is_infinity:
            x = self.blocks[-1].body.getCenter()[0] + const.BLOCK_SIZE
            self.generateBlock(x, const.BLOCK_TYPES)
        if self.situation_iterations > 0:
            self.removed_series += 1
            if self.removed_series == len(self.situation):
                self.situation_iterations -= 1
                self.removed_series = 0
                x = self.blocks[-1].body.getCenter()[0] + const.BLOCK_SIZE
                self.generateSituation(x)

    def act(self, dt):
        for block in self.blocks:
            block.act(dt)