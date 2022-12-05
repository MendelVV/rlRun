import const
import random
from actors.block_actor import BlockActor


class AreaActor:

    BLOCK_TYPE = 1

    def __init__(self, world, group):
        self.world = world
        self.blocks = []
        self.group = group
        self.generateStart()

    def generateStart(self):
        # генерируем просто набор блоков
        dx = 0
        for i in range(10):
            self.generateBlock(dx, 0)
            dx += BlockActor.SIZE

        #for i in range(100):
        #    dx = self.generateSituation(dx)
        while dx < const.WIDTH * 1.5:
            self.generateBlock(dx, AreaActor.BLOCK_TYPE)
            dx += BlockActor.SIZE

    def generateSituation(self, x):
        #генерируем сразу ситуации
        y = 1*BlockActor.SIZE + const.HEIGHT - 1.5 * BlockActor.SIZE
        for i in range(6):
            block = BlockActor(x, y, self.world, self)
            self.blocks.append(block)
            self.group.add(block)
            x+=BlockActor.SIZE

        y = 0 * BlockActor.SIZE + const.HEIGHT - 1.5 * BlockActor.SIZE
        for i in range(1):
            block = BlockActor(x, y, self.world, self)
            self.blocks.append(block)
            self.group.add(block)
            x += BlockActor.SIZE
        return x

    def generateBlock(self, x, r):
        # генерация одного блока на какойто высоте
        y = (2-random.randint(0, r)) * BlockActor.SIZE + const.HEIGHT-2.5*BlockActor.SIZE
        block = BlockActor(x, y, self.world, self)
        self.blocks.append(block)

        self.group.add(block)

    def remove(self, block):
        self.group.remove(block)
        self.blocks.remove(block)

        #должны добавить новый блок, только понять куда
        x = self.blocks[-1].body.getCenter()[0]+BlockActor.SIZE
#        print('old x = ',self.blocks[-1].rect.x, 'new x = ', x)
        self.generateBlock(x, AreaActor.BLOCK_TYPE)