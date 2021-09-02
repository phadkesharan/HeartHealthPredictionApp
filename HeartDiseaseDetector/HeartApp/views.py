from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from . import models
import numpy as np
import joblib

# Create your views here.

# main page view
def main(request):
    return render(request, 'HeartApp/index.html')

# prediction page

def pred(request):

    # fetching patient details
    name = request.POST['full_name']
    city = request.POST['city']
    address = request.POST['address']

    # fetching the features

    # fetching age
    age = request.POST['age']

    # fetching sex 
    sex_temp = request.POST['sex']
    if sex_temp == 'male':
        sex = 1
    elif sex_temp == 'female':
        sex = 0

    # fetching cp
    cp_temp = request.POST['cp']
    print("cp : ", cp_temp)
    if cp_temp == 'cp_0':
        cp = 0
    elif cp_temp == 'cp_1':
        cp = 1
    elif cp_temp == 'cp_2':
        cp = 2
    elif cp_temp == 'cp_3':
        cp = 3

    # fetching trestbps 
    trestbps = request.POST['trestbps']

    # fetching chol
    chol = request.POST['chol']

    #fetching fbs 
    fb_temp = request.POST.get('fbs')
    print(fb_temp)
    if fb_temp == 'on':
        fbs = 1
    else:
        fbs = 0

    # fetching restecg
    restecg = request.POST['restecg']

    # fetching thalach
    thalach = request.POST['thalach']

    # fetching exang
    exang_temp = request.POST.get('exang')
    print(exang_temp)
    if exang_temp == 'on':
        exang = 1
    else:
        exang = 0

    
    # fetching oldpeak
    oldpeak = request.POST['oldpeak']

    # fetching slope
    slope_temp = request.POST['slope']
    if slope_temp == '0':
        slope = 0
    elif slope_temp == '1':
        slope = 1
    elif slope_temp == '2':
        slope = 2

    #fetching ca
    ca_temp = request.POST['ca']
    if ca_temp == '0':
        ca = 0
    elif  ca_temp == '1':
        ca = 1
    elif  ca_temp == '2':
        ca = 2
    elif ca_temp == '3':
        ca = 3

    # fetching thal 
    thal_temp = request.POST['thal']
    if thal_temp == '3':
        thal = 1
    elif thal_temp == '6':
        thal = 2
    elif thal_temp == '7':
        thal = 3   

    # Loading the ML model
    model = joblib.load("HeartApp\model\HeartApp\logistic_regression.sav")
    
    # Input features
    X = np.array((age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)).reshape(1, -1)

    prediction = int(model.predict(X)[0])

    # Saving into database
    newData = models.Heart(age=age, sex=sex, cp=cp, trestbps=trestbps, chol=chol,
        fbs=fbs, restecg=restecg, thalach=thalach,
        exang=exang, oldpeak=oldpeak, slope=slope, ca=ca, thal=thal, target=prediction, fullname=name, city=city, address=address)

    newData.save()

    result = ""
    if prediction == 0:
        result = "You have low risk of having a  heart disease"
    else:
        result = "You have high risk of having a heart disease, please consult a doctor"


    context = {'result':  result}
    return render(request, 'HeartApp/pred.html', context)




