import pickle
from warnings import catch_warnings
import numpy as np
from flask import Flask, redirect, render_template, request, jsonify, flash
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')
    

@app.route('/predict', methods=['GET', 'POST'])
def predictor():
    model = pickle.load(open('Loan.pickle', 'rb'))
    price = None
    message = -1
    if request.method == "POST":
        age = request.form.get("age")
        income = request.form.get("income")
        property = request.form.get("property")
        Intent = request.form.get("Intent")
        Amount = request.form.get("Amount")

        print(age,income,property,Intent,Amount)
        

        if(property=='rent'):
            property=0
        elif(property=='own'):
            property=1
        elif(property=='mortgage'):
            property=2
        else:
            property=3

         #PERSONAL':0,'EDUCATION':1,'MEDICAL':2,'VENTURE':3,'HOMEIMPROVEMENT':4,'DEBTCONSOLIDATION':5

        if(Intent=='personal'):
            Intent=0
        elif(Intent=='education'):
            Intent=1
        elif(Intent=='medical'):
            Intent=2
        elif(Intent=='venture'):
            Intent=3
        elif(Intent=='homeimprovement'):
            Intent=4
        else:
            Intent=5

        data=np.array([[age,income,property,Intent,Amount]])
        price =  model.predict(data)
        
        #return render_template("predict.html",message='Price Of House is {} lakhs'.format(mess),pric=price)
        return render_template("predict.html",pric=price)
        
    return render_template("predict.html",warning='12')

if __name__ == "__main__":
    app.run(debug=True)