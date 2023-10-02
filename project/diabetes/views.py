from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np
from .forms import checkdiabetesForm

def diabetes_prediction_model(request, f1, f2, f3, f4, f5, f6, f7, f8):
    data = pd.read_csv('diabetes//diabetes.csv')
    X = data.iloc[:, :-1]
    y = data['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    scale = StandardScaler()
    X_train = scale.fit_transform(X_train)
    X_test = scale.transform(X_test)  
    input_features = np.array([f1, f2, f3, f4, f5, f6, f7, f8]).reshape(1, -1)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    predict = model.predict(input_features)

    return predict

def index(request):
    predict=None
    if request.method=='POST':
        form=checkdiabetesForm(request.POST)
        if form.is_valid():
            form.save()
            f1=form.cleaned_data['Pregnancies']
            f2=form.cleaned_data['Glucose']
            f3=form.cleaned_data['BloodPressure']
            f4=form.cleaned_data['SkinThickness']
            f5=form.cleaned_data['Insulin']
            f6=form.cleaned_data['BMI']
            f7=form.cleaned_data['DiabetesPedigreeFunction']
            f8=form.cleaned_data['age']
            predict=diabetes_prediction_model(request,f1,f2,f3,f4,f5,f6,f7,f8)
            if int(predict)==1:
                predict='diabetes'
            else:
                predict='no diabetes'
    else:
        form=checkdiabetesForm()
    context={
        'form':form,
        'predict':predict
    }
    return render(request,'index.html',context)


