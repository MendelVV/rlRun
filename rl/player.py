import const
from phisics.rectangle import Rectangle
from phisics.bodyr import BodyR
from rl.act_reward import ActReward
#from rl.state import get_state_many
from rl.state import get_state_many_2


class Player:
    # хранит в себе логику rl

    def __init__(self, x, y, world):
        self.world = world
        rect = Rectangle(x, y, const.PLAYER_WIDTH, const.PLAYER_HEIGHT)
        self.body = BodyR(rect, (0, const.GRAVITY))

        self.body.parent = self
        self.world.addBody(self.body)
        self.dt = 0
        self.act_dt = 0
        #        self.last_x = self.body.getCenter()[0]
        #        self.last_x = []#последние предпринятые действия
        self.act_rewards = []  # последние предпринятые действия

    def fall(self):
        self.body.set_action(BodyR.ACTION_FALL)

    def smash(self):
        self.body.set_action(BodyR.ACTION_SMASH)

    def landing(self):
        self.body.set_action(BodyR.ACTION_RIGHT)

    def jump(self):
        self.body.set_action(BodyR.ACTION_JUMP)

    def double_jump(self):
        self.body.set_action(BodyR.ACTION_DOUBLE_JUMP)

    def act(self, dt):
        self.act_dt += dt
        self.updateRewards(dt)
        if self.act_dt >= const.ACT_DT:
            if self.body.getCenter()[0] < -const.PLAYER_WIDTH:
                # проиграли и об этом нужно сказать вознаграждению
                self.world.running = False
                return
            elif self.body.getCenter()[1] > const.HEIGHT:
                self.lose_reward()
                self.world.running = False
                return

            if self.body.action != BodyR.ACTION_RIGHT:
                return

            # вознаграждение за прошлое действие
            #            self.updateRewards(dt)
            # берем случайное действие
            blocks = self.world.getNextBlock(self.body.getCenter()[0])
            state = get_state_many_2(self.body.getCenter(), blocks, -1)
            a = self.world.all_states.getActions(state)

            self.body.set_action(a)
            last_action = get_state_many_2(self.body.getCenter(), blocks, a)
            self.act_rewards.append(ActReward(last_action, 0, self.body.getCenter()[0]))
            self.act_dt = 0

    def updateRewards(self, dt):
        if len(self.act_rewards) == 0:
            return
        rv = []
        for ar in self.act_rewards:
            ar.addT(dt, self.body.getCenter()[0])
            if ar.end:
                state = ar.state
                rew = ar.reward
                self.world.all_states.addReward(state, rew)
                rv.append(ar)
        for r in rv:
            self.act_rewards.remove(r)
#        if self.act_rewards[0].count >= const.REWARD_DT:
#            last_action = self.act_rewards.pop(0)
#            state = last_action.state
#            rew = last_action.reward
       #     if state[-1] == 1:
       #         print("add reward", last_action.count, round(last_action.reward, 2))
#            self.world.all_states.addReward(state, rew)

    def lose_reward(self):
        if self.body.getCenter()[0] > 610:
            print("LOSE!!!", self.body.getCenter())
        for ar in self.act_rewards:
            state = ar.state
            ar.addT(1, 0)
#            print('lose reward', ar.reward)
            self.world.all_states.addReward(state, ar.reward)
