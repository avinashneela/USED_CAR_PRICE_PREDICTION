from flask import Flask,render_template
import pandas as pd
app=Flask(__name__)
car1=pd.read_csv('cleaned_cars.csv.csv')



@app.route('/')
def index():
    companies=sorted(car1['company'].unique())
    car_models=sorted(car1['name'].unique())
    years=sorted(car1['year'].unique() , reverse=True)
    fuel_types=car1['fuel_type'].unique()
    return render_template('index.html',companies=companies,car_models=car_models,years=years,fuel_types=fuel_types)

if __name__=='__main__':
    app.run(debug=True)