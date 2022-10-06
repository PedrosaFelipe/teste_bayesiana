from flask import Flask , render_template , redirect ,url_for
import numpy as np

app = Flask(__name__)

@app.route('/')

def index():

    if np.random.random() < 0.5: 
        return render_template('pg_layout_red.html')
    else:
        return render_template('pg_layout_blue.html')

@app.route('/yes' , methods=['POST'])

def yes_event():
    return redirect(url_for('index'))


@app.route('/no' , methods=['POST'])

def no_event():
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run()
