
import numpy as np

class OmniscientAgent (object):
    def __init__(self , prob_list):
        self.prob_list = prob_list
    
    def pull(self , bandit_machine):
        if np.random.random() < self.prob_list[bandit_machine]:
            reward = 1
        else:
            reward = 0
        return reward

# probabilidade de ter um resultado positivo da página

prob_list = [ 0.25 , 0.30]



# paramentros do experimento

trials = 1000
episodes = 200
# agent
bandit = OmniscientAgent(prob_list)


prob_reward_array = np.zeros(len(prob_list))
accumulate_reward = list()
avg_accumulate_reward_array = list()
for episode in range(episodes):
    reward_array = np.zeros(len(prob_list))
    bandit_array = np.full(len(prob_list) , 1.0e-5)
    accumulate_reward_array = 0

    for trial in range(trials):
        
        # agent - escolha
        bandit_machine = np.argmax(prob_list)


        # agent - recompensa
        reward = bandit.pull(bandit_machine)

        # agent - guarda recompensa
        reward_array[bandit_machine] += reward
        bandit_array[bandit_machine] +=1
        accumulate_reward_array += reward

    prob_reward_array += reward_array / bandit_array
    accumulate_reward.append(accumulate_reward_array)
    avg_accumulate_reward_array.append(np.mean(accumulate_reward_array))

prob01 = 100 * np.round(prob_reward_array[0] / episodes , 2)
prob02 = 100 * np.round(prob_reward_array[1] / episodes , 2)


print('\nProb Bandit 01: {}% - Prob Bandit 02: {}%'.format(prob01 , prob02))
print('\nAvg accumulated reward: {}\n'.format(np.mean(accumulate_reward_array)))