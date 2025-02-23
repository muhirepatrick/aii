from django.shortcuts import render

# Create your views here.

# ai_app/views.py
from django.shortcuts import render
from .models import create_model
import numpy as np

def predict(request):
    if request.method == 'POST':
        input_data = np.array([...])  # Get input data from request
        model = create_model()
        result = model.predict(input_data)
        return render(request, 'result.html', {'result': result})
    return render(request, 'input.html')
