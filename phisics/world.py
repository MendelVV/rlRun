import const
from phisics.bodyr import BodyR
from rl.block import Block
from rl.player import Player


class World:

    def __init__(self, all_states):
        self.bodies = []
        self.running = True
        self.all_states = all_states

    def addBody(self, body):
        self.bodies.append(body)

    def removeBody(self, body):
        self.bodies.remove(body)

    def getNextBlock(self, px):
        blocks = list(
            filter(lambda x: type(x.parent) == Block and const.PLAYER_WIDTH/2 < x.getCenter()[0] - px < (const.REVIEW + 1) * const.BLOCK_SIZE,
                   self.bodies))
        return blocks[:const.REVIEW]

    def act(self, dt):
        for b in self.bodies:
            b.act(dt)
        self.collisions()

    def collisions(self):
        # проверяем столкновения
        player = list(filter(lambda x: type(x.parent) == Player, self.bodies))[0]
        blocks = list(
            filter(lambda x: type(x.parent) == Block and abs(x.getCenter()[0] - player.getCenter()[0]) < 30,
                   self.bodies))
        fall = True
        for block in blocks:
            if player.intersect(block):
                self.collision_handling(player, block)
                fall = False
        if fall:
            player.parent.fall()

    def collision_handling(self, player, block):
        px, py = player.getCenter()
        bx, by = block.getCenter()
        dx = px-bx#разность по длине
        dy = py-by#разность по высоте
        dw = (const.BLOCK_SIZE+const.PLAYER_WIDTH)/2
        dh = (const.BLOCK_SIZE+const.PLAYER_HEIGHT)/2
        if dy+dh < 2 and abs(dx) < dw:
            player.setCenter(px, by-const.BLOCK_SIZE/2-const.PLAYER_HEIGHT/2)
            player.parent.landing()#приземлились
        elif py-by < abs(const.PLAYER_HEIGHT/2+const.BLOCK_SIZE/2)-0.5 and abs(dx) > dw-1:
#            #врезался в блок впереди
            player.setCenter(bx-const.BLOCK_SIZE/2-const.PLAYER_WIDTH/2, py)
        elif abs(dx) < dw and 0.5 < dy < dh:
            player.setCenter(px, by+const.BLOCK_SIZE/2+const.PLAYER_HEIGHT/2)
            player.parent.smash()