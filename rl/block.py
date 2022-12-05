from phisics.bodyr import BodyR
from phisics.rectangle import Rectangle
import const


class Block:

    def __init__(self, x, y, area):
        self.world = area.world
        self.area = area
        rect = Rectangle(x, y, const.BLOCK_SIZE, const.BLOCK_SIZE)
        self.body = BodyR(rect, (-const.SPEED, 0))
        self.body.parent = self
        self.world.addBody(self.body)

    def act(self, dt):
        if self.body.getCenter()[0] < -100:
            #удаляем актера с поля
            self.world.removeBody(self.body)
            self.area.remove(self)
