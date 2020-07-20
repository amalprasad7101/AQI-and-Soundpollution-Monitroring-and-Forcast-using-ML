from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')
def chart(request):
    return render(request, 'chart.html')
def forcast(request):
    return render(request, 'forcast.html')

def result(request):
   
    inputDate = request.POST["inputDate"]
    currentDate = datetime.today().strftime('%Y-%m-%d')
    date_format = "%Y-%m-%d"
    currentDate = datetime.strptime(currentDate, date_format)
    inputDate = datetime.strptime(inputDate, date_format)
    difference = inputDate - currentDate
    
    s=pd.read_csv("./assets/clim.csv")
    days = difference.days
    x=s[["days"]]
    y=s[["sound"]]
    w=s[["gas"]]
    v=s[["humidity"]]
    z=s[["temp"]]
    c=([[days]])
    r=LinearRegression()
    r.fit(x,y)
    p=r.predict(c)
    r.fit(x,w)
    q=r.predict(c)
    r.fit(x,v)
    t=r.predict(c)
    r.fit(x,z)
    n=r.predict(c)
    
    return render(request, 'result.html', {'date': inputDate, 'sound' :p, 'gas': q, 'humidity': t, 'temperature': n})
    
    