from flask import Flask , render_template , redirect ,url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')

def index():

        return render_template('pg_layout_blue.html')


@app.route('/yes' , methods=['POST'])

def yes_event():
    df = pd.read_csv('data_experiment.csv')
    click = 1
    visit = 1
    group = 'control'

    df_raw = pd.DataFrame({'click' : click , 'visit': visit , 'group':group} , index=[0] )

    df = pd.concat([df , df_raw])
    df.to_csv('data_experiment.csv' , index = False)
    return redirect(url_for('index'))


@app.route('/no' , methods=['POST'])

def no_event():
    df = pd.read_csv('data_experiment.csv')
    click = 0
    visit = 1
    group = 'control'

    df_raw = pd.DataFrame({'click' : click , 'visit': visit , 'group':group} , index=[0])

    df = pd.concat([df , df_raw])
    df.to_csv('data_experiment.csv' , index = False)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(port=5000)
