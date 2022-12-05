import const


class ActReward:
    REWARD_DT_RIGHT = 2
    REWARD_DT_JUMP = 3
    REWARD_DT_SUPER_JUMP = 4

    # класс которых хранить вознаграждение за одно действие
    def __init__(self, state, rew, x):
        self.state = state
        self.reward = rew
        self.x = x
        self.t = 0
        self.all_t = 0
        self.count = 0
        self.end = False
        self.reward_dt = state[-1] + 2  # пока просто так, на 1 больше чем действие

    def addT(self, dt, new_x):
        self.t += dt
        self.all_t += dt
        if self.t >= 1:
            self.t -= 1
            rew = (new_x - self.x) * (const.GAMMA ** self.count)
            self.count += 1
            self.addReward(rew/self.count)
            self.x = new_x
            self.end = self.count == self.reward_dt

    def addReward(self, rew):
        self.reward += rew
