class Reward:

    def __init__(self):
        self.count = 0
        self.reward = 0

    def addReward(self, rew):
        self.reward = self.count * self.reward + rew
        self.count += 1
        self.reward = self.reward / self.count
#        print('New reward!', rew)