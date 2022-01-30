from flask import Flask, render_template, url_for, request, redirect
import pickle
import math
import pandas as pd
import numpy as np

app = Flask(__name__)


predicted_score = None

@app.route('/')
def index():
	return render_template('index.html', score=predicted_score)

@app.route('/predict', methods=['GET', 'POST'])
def prediction():
	with open('models/model.pkl' , 'rb') as f:
		lr = pickle.load(f)
	global predicted_score
	if request.method == 'POST':
		req = request.form
		predict = pd.DataFrame()

		Marital_Status = int(req['Marital_Status'])
		if Marital_Status == 0:
			predict['D'] = [0]
			predict['M'] = [1]
			predict['S'] = [0]
			predict['U'] = [0]
		
		if Marital_Status == 1:
			predict['D'] = [0]
			predict['M'] = [0]
			predict['S'] = [1]
			predict['U'] = [0]
		
		if Marital_Status == 2:
			predict['D'] = [0]
			predict['M'] = [0]
			predict['S'] = [0]
			predict['U'] = [1]
		
		if Marital_Status == 3:
			predict['D'] = [1]
			predict['M'] = [0]
			predict['S'] = [0]
			predict['U'] = [0]

		Customer_Age = int(req['Customer_Age'])
		predict['Customer_Age'] = [Customer_Age]

		Gender = int(req['Gender'])
		predict['Gender'] = [Gender]

		Dependent_count = int(req['Dependent_count'])
		predict['Dependent_count'] = [Dependent_count]

		Education_Level = int(req['Education_Level'])
		predict['Education_Level'] = [Education_Level]

		########

		########

		Income_Category = int(req['Income_Category'])
		predict['Income_Category'] = [Income_Category]

		Card_Category = int(req['Card_Category'])
		predict['Card_Category'] = [Card_Category]

		Months_on_book = int(req['Months_on_book'])
		predict['Months_on_book'] = [Months_on_book]

		Total_Relationship_Count = int(req['Total_Relationship_Count'])
		predict['Total_Relationship_Count'] = [Total_Relationship_Count]

		Months_Inactive_12_mon = int(req['Months_Inactive_12_mon'])
		predict['Months_Inactive_12_mon'] = [Months_Inactive_12_mon]

		Contacts_Count_12_mon = int(req['Contacts_Count_12_mon'])
		predict['Contacts_Count_12_mon'] = [Contacts_Count_12_mon]

		Credit_Limit = int(req['Credit_Limit'])
		predict['Credit_Limit'] = [Credit_Limit]

		Total_Revolving_Bal = int(req['Total_Revolving_Bal'])
		predict['Total_Revolving_Bal'] = [Total_Revolving_Bal]

		Avg_Open_To_Buy = int(req['Avg_Open_To_Buy'])
		predict['Avg_Open_To_Buy'] = [Avg_Open_To_Buy]

		Total_Amt_Chng_Q4_Q1 = int(req['Total_Amt_Chng_Q4_Q1'])
		predict['Total_Amt_Chng_Q4_Q1'] = [Total_Amt_Chng_Q4_Q1]

		Total_Trans_Amt = int(req['Total_Trans_Amt'])
		predict['Total_Trans_Amt'] = [Total_Trans_Amt]

		Total_Trans_Ct = int(req['Total_Trans_Ct'])
		predict['Total_Trans_Ct'] = [Total_Trans_Ct]

		Total_Ct_Chng_Q4_Q1 = int(req['Total_Ct_Chng_Q4_Q1'])
		predict['Total_Ct_Chng_Q4_Q1'] = [Total_Ct_Chng_Q4_Q1]

		Avg_Utilization_Ratio = float(req['Avg_Utilization_Ratio'])
		predict['Avg_Utilization_Ratio'] = [Avg_Utilization_Ratio]
		predict = np.array(predict)
		with open('models/model.pkl' , 'rb') as f:
			lr = pickle.load(f)

		predicted = lr.predict(predict)
		if predicted[0] == 1:
			ans = "Customer is Eligible!!. Go for Pitching Product"
		else:
			ans = "Customer is not Eligible"
		return render_template('predict.html', score=ans)
		
	else:
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True, port=8000)
