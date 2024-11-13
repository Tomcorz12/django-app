from django.shortcuts import render
from My_First_App.models import Car

# Create your views here.
def my_view(request):
    car_list = Car.objects.all()
    context = {
        'car_list': car_list
    }
    return render(request, "My_First_App/car_list.html", context)