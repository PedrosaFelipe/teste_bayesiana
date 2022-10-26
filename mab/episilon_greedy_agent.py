
import numpy as np

class EPSGreedyAgent (object):
    def __init__(self , prob_list):
        self.prob_list = prob_list
    
    def pull(self , bandit_machine):
        if np.random.random() < self.prob_list[bandit_machine]:
            reward = 1
        else:
            reward = 0
        return reward

# probabilidade de ter um resultado positivo da página

prob_list = [ 0.25 , 0.3]



# paramentros do experimento

trials = 1000
episodes = 200

eps_init = 1
decay = 0.05

# valores de decaimento de eps

eps_array = [(eps_init*(1 - decay))** i for i in range(trials)]



# agent
bandit = EPSGreedyAgent(prob_list)


prob_reward_array = np.zeros(len(prob_list))
accumulate_reward = list()
avg_accumulate_reward_array = list()

for episode in range(episodes):
    reward_array = np.zeros(len(prob_list))
    bandit_array = np.full(len(prob_list) , 1.0e-5)
    accumulate_reward_array = 0

    for trial in range(trials):
        
        # agent - escolha 
        eps = eps_array[trial]

        if eps >= 0.25: # exploração ou explotation
            # Fase de exploração
            bandit_machine = np.random.randint(low=0 , high=2 , size=1 )[0]
        else:
            # Fase de Explotation
            prob_reward = reward_array / bandit_array
            max_prob_reward = np.where(prob_reward ==  np.max(prob_reward))[0]
            bandit_machine = max_prob_reward[0]


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