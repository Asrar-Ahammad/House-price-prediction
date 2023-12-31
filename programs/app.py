from flask import Flask, render_template, request
import pandas as pd
import pickle as pkl

app = Flask(__name__)
data = pd.read_csv('/Users/shaikmohammadasrarahammad/Downloads/data_science/Projects/house_price_prediction/programs/clean_data.csv')
pipe = pkl.load(open('/Users/shaikmohammadasrarahammad/Downloads/data_science/Projects/house_price_prediction/programs/ridgeModel.pkl','rb'))

@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations = locations)

@app.route('/predict', methods = ['POST'])
def predict():
    location = request.form.get('location')
    bhk = float(request.form.get('bhk'))
    bath = float(request.form.get('bath'))
    sqft = float(request.form.get('total_sqf'))

    print(location, bhk, bath, sqft)
    input = pd.DataFrame([[location,sqft, bath, bhk]], columns = ['location','total_sqft','bath','bhk'])
    prediction = pipe.predict(input)[0]
    return str(prediction)

if __name__ == '__main__':
    app.run(debug= True, port = 5001)