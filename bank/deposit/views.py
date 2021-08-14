from django.shortcuts import render

from django.http import JsonResponse
import pandas as pd
from .models import PredResults
import numpy as np

def deposit(request):
    return render(request, 'index.html')

def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        age = int(input("Enter your Age: "))
        job= int(input("Enter your job: "))
        marital= int(input("Enter your marital: "))
        education= int(input("Enter your education: "))
        balance= int(input("Enter your balance: "))
        housing= int(input("Enter your housing: "))
        loan= int(input("Enter your loan: "))
        contact= int(input("Enter your contact: "))
        day= int(input("Enter your day: "))
        month= int(input("Enter your month: "))
        duration= int(input("Enter your duration: "))
        campaign= int(input("Enter your campaign: "))
        previous= int(input("Enter your previous: "))
        poutcome= int(input("Enter your poutcome: "))

        # Unpickle model
        lg_model = pd.read_pickle(r"bank_model.pkl")
        # Make prediction
        result = lg_model.predict([[age,job,marital,education,balance,housing,loan,contact,day,month,
                                           duration,campaign,previous,poutcome]])

        classification = result[0]

        PredResults.objects.create(age=age,job=job,marital=marital,education=education,balance=balance,housing=housing,loan=loan,
                                   contact=contact,day=day,month=month,duration=duration,campaign=campaign,
                                   previous=previous,poutcome=poutcome)

        return JsonResponse({'result': classification,"age":age,"job":job,
              "marital":marital,"education":education,
              "balance":balance,
              "housing":housing,"loan":loan,
              "contact":contact,"day":day,
              "month":month,"duration":duration,
              "campaign":campaign,"previous":previous,
              "poutcome":poutcome},
                            safe=False)
def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)