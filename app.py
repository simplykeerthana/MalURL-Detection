import flask
import pandas as pd
import pickle
# Use pickle to load in the pre-trained model.
with open(f'model/final_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        url = flask.request.form['url']
       
        input_variables = pd.DataFrame([[url]],
                                       columns=['url'],
                                       dtype='|S6')
        prediction = model.predict(input_variables)[0]
        return flask.render_template('main.html',
                                     original_input={'url':url },
                                     result=prediction,
                                     )