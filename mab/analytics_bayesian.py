from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

def bayesian_interference(data):
    N_mc = 10000
    proba_b_better_a = []
    expected_loss_a = []
    expected_loss_b = []

    for day in range(len(data)):
        u_a , var_a = stats.beta.stats(a = 1 + data.loc[day, 'acc_clicks_A'], 
                                       b = 1 + (data.loc[day, 'acc_visits_A'] - data.loc[day, 'acc_clicks_A'] ),
                                       moments = 'mv')

        u_b , var_b = stats.beta.stats(a = 1 + data.loc[day, 'acc_clicks_B'], 
                                       b = 1 + (data.loc[day, 'acc_visits_B'] - data.loc[day, 'acc_clicks_B'] ),
                                       moments = 'mv')
                                
        # Amostras da distribuição normal A
        x_a = np.random.normal(loc = u_a,
                               scale = 1.25 * np.sqrt( var_a),
                               size = N_mc)

        # Amostras da distribuição normal B
        x_b = np.random.normal(loc = u_b,
                               scale = 1.25 * np.sqrt( var_b),
                               size = N_mc)

        # Beta distribuition function of page A
        fa = stats.beta.pdf(x_a, 
                            a = 1 + data.loc[day, 'acc_clicks_A'], 
                            b = 1 + (data.loc[day, 'acc_visits_A'] - data.loc[day, 'acc_clicks_A'] ))

        # Beta distribuition function of page B
        fb = stats.beta.pdf(x_b, 
                            a = 1 + data.loc[day, 'acc_clicks_B'], 
                            b = 1 + (data.loc[day, 'acc_visits_B'] - data.loc[day, 'acc_clicks_B'] ))

        # Normal distribuition function of page A
        ga = stats.norm.pdf(x_a,
                            loc = u_a,
                            scale = 1.25 * np.sqrt( var_a))

        # Normal distribuition function of page B
        gb = stats.norm.pdf(x_b,
                            loc = u_b,
                            scale = 1.25 * np.sqrt( var_b))

        # Beta / Normal
        y = ( fa * fb) / (ga * gb)

        # Somente valores onde B é maior ou igual do que A
        yb = y[x_b >= x_a]

        # Probabilidade de B ser melhor do que A
        p = (1 / N_mc) * np.sum(yb)

        # Erro ao assumir B melhor do que A
        expected_loss_A = (1 / N_mc) * np.sum(((x_b - x_a) * y)[x_b >= x_a])
        expected_loss_B = (1 / N_mc) * np.sum(((x_a - x_b) * y)[x_a >= x_b])

        proba_b_better_a.append(p)
        expected_loss_a.append(expected_loss_A)
        expected_loss_b.append(expected_loss_B)
                                
    return proba_b_better_a , expected_loss_a , expected_loss_b

def animate(i):

    data = pd.read_csv('data_experiment.csv')

    # dtypes
    data['click'] = data['click'].astype(int)
    data['visit'] = data['visit'].astype(int)

    # pivot table

    data = data.reset_index().rename(columns={'index' : 'day'} )


    data = data.pivot( index = 'day' , columns = 'group' , values=['click' , 'visit']).fillna (0)
    data.columns = ['click_control' , 'click_treatment' , 'visit_control' , 'visit_treatment']

    data = data[['visit_control' , 'click_control' , 'visit_treatment' , 'click_treatment']]
    

    data['acc_visits_A'] = data['visit_control'].cumsum()
    data['acc_clicks_A'] = data['click_control'].cumsum()

    data['acc_visits_B'] = data['visit_treatment'].cumsum()
    data['acc_clicks_B'] = data['click_treatment'].cumsum()

    # inference bayesian

    p , expected_loss_a , expected_loss_b = bayesian_interference(data)

    x1 = np.arange(len(p))



    plt.cla()
    plt.plot(x1 , p , label = 'Probability B better A')
    plt.plot(x1 , expected_loss_a , label = 'Risk Chossing A')
    plt.plot(x1 , expected_loss_b , label = 'Risk Chossing B')
    plt.legend(loc = 'upper right')
    plt.tight_layout()

ani = FuncAnimation(plt.gcf() , animate , interval = 1000)

plt.tight_layout()

plt.show()

