import random

import const
from rl.reward import Reward


def state_equals(state, pos):
    b = True
    n = len(pos)-1
#    print('on eq',state, pos)
    for i in range(n):
        b = b and state[i] == pos[i]
    return b


class AllStates:
    # состояние это три пары чисел
    # координата шарика, скорость шарика, координата плашки
    # нужен словарь словарей вознаграждений
    RANDOM = 0
    GREEDY = 1
    EPSILON_GREEDY = 2

    def __init__(self, type, static=False):
        self.states = {}
        self.type = type
        self.static = static

    def addReward(self, state, rew):
        if self.static:
            return
        if len(state) < (const.REVIEW*2)+1:
            return
        if not (state in self.states):
            self.states[state] = Reward()
        self.states[state].addReward(rew)

    def fillState(self, pos):
        a = [1, 3]
        for act in a:
            state = list(pos)
            state[-1] = act
            self.addReward(tuple(state), 2)

    def getActions(self, pos):
        if self.type == AllStates.RANDOM:
            return self.getActionsRandom(pos)
        elif self.type == AllStates.GREEDY:
            return self.getActionsGreedy(pos)
        elif self.type == AllStates.EPSILON_GREEDY:
            return self.getActionsEpsilonGreedy(pos)

    def getActionsRandom(self, pos):
        a = random.randint(1, const.PLAYER_ACTIONS)
        return a

    def getActionsGreedy(self, pos):
        # оставляем только такие сосояния у которых состояние совпадает с текущим
        states = list(filter(lambda x: state_equals(x, pos), self.states.keys()))

        if len(states) == 0:
#            print("no states!")
            self.fillState(pos)
            return self.getActionsRandom(pos)

        mx = -200
        a = []

        for state in states:
            if self.states[state].reward > mx:
                mx = self.states[state].reward
                # print('Change action!', state, mx)
                a.clear()
                a.append(state[-1])
            elif self.states[state].reward == mx:
                a.append(state[-1])

#        print('select action', a, round(mx,2),len(states))
#        if a[0]==3:
#            for state in states:
#                print(state, round(self.states[state].reward,2))

        if len(a) == 0:
            # случайное действие
#            raise Exception("no actions!!!")
            print("no action!!!", states)
            act = self.getActionsRandom(pos)
        elif len(a) == 1:
            act = a[0]
        else:
            act = a[random.randint(0, len(a) - 1)]

        return act

    def getActionsEpsilonGreedy(self, pos):
        e = random.randint(1, 100)
        if e <= 100*const.EPSILON:
            return self.getActionsRandom(pos)
        else:
            return self.getActionsGreedy(pos)

    def show(self):
        for key in self.states.keys():
            print(key, self.states[key].reward)
        print('end!\n')

    def saveCSV(self, f_name):
        f = open(f_name, 'w')
        for key in self.states.keys():
            line = '*'.join(list(map(str, key)))
            line += ',' + str(self.states[key].reward) + '*' + str(self.states[key].count)
            f.write(line + '\n')
        f.close()

    def readCSV(self, f_name):
        f = open(f_name, 'r')
        for line in f:
            a = line.split(',')
            state = a[0].split('*')
            state = tuple(map(int, state))
            r = tuple(map(float, a[1].split('*')))
            reward = Reward()
            reward.reward = r[0]
            reward.count = int(r[1])
            self.states[state] = reward
