from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

def plot_view(request):
    try:
        health_data=pd.read_csv("data.csv", header=0, sep=",")
    except FileNotFoundError:
        error_message="Data file not found!"
        return render(request, 'error.html',{'error': error_message})
    
    plt.figure()
    health_data.plot(x='Average_Pulse', y='Calorie_Burnage', kind='line')
    plt.ylim(ymin=0)
    plt.xlim(xmin=0)

    buffer= io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    buffer.close()
    graphic=base64.b64encode(image_png).decode('utf-8')
    return render(request, 'plot.html', {'graphic':graphic})

def index(request):
    return render(request, 'index.html')


