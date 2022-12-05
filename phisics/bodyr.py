from phisics.rectangle import Rectangle
import const


class BodyR:
    ACTION_NONE = 0
    ACTION_RIGHT = 1
    ACTION_JUMP = 2
    ACTION_DOUBLE_JUMP = 3
    ACTION_FALL = 4
    ACTION_SMASH = 5

    def __init__(self, rect, v=(0, 0)):
        # rect - это прямоугольник
        self.rect = rect
        self.action = BodyR.ACTION_RIGHT
        self.velocity = list(v)
        self.parent = None
        self.current_inter = []

    def getCenter(self):
        return self.rect.x, self.rect.y

    def setCenter(self, x, y):
        self.rect.x, self.rect.y = x, y

    def act(self, dt):
        # выполняем текущее действие
        self.rect.x += self.velocity[0] * dt
        self.rect.y += self.velocity[1] * dt
        if self.velocity[1] * dt>2:
            print("exstra dy = "+str(self.velocity[1] * dt))
#            raise Exception("exstra","dy = "+str(self.velocity[1] * dt))
        if self.action == BodyR.ACTION_JUMP or self.action == BodyR.ACTION_DOUBLE_JUMP or self.action == BodyR.ACTION_FALL:
            self.gravity(dt)

    def intersect(self, other):
        return self.rect.intersect(other.rect)

    def set_action(self, action):
        if self.action == action:
            return
        if BodyR.ACTION_JUMP <= action <=BodyR.ACTION_FALL and BodyR.ACTION_JUMP <= self.action <= BodyR.ACTION_FALL:
            return
#        if action == BodyR.ACTION_JUMP and self.action == BodyR.ACTION_FALL:
#            return
        self.action = action
        if action == BodyR.ACTION_JUMP:
            # прыгаем до тех пор пока не приземлимся
            self.velocity[0] = -0.5
            self.velocity[1] = -1 * const.GRAVITY
        elif action == BodyR.ACTION_DOUBLE_JUMP:
            self.velocity[0] = -1
            self.velocity[1] = -1.5 * const.GRAVITY
        elif action == BodyR.ACTION_RIGHT:
            self.velocity[0] = 1.5
            self.velocity[1] = const.GRAVITY / 2
        elif action == BodyR.ACTION_FALL or action == BodyR.ACTION_SMASH:
            # прыгаем до тех пор пока не приземлимся
            self.velocity[0] = 0
            self.velocity[1] = const.GRAVITY

    def gravity(self, dt):
        self.velocity[1] += dt * const.GRAVITY

