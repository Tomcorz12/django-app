from django.shortcuts import render

# Create your views here.
def my_view(request):
    car_list = [
        {'title': "BMW"},
        {'title': "Mazda"}
    ]
    context = {
        'car_list': car_list
    }
    return render(request, "My_First_App/car_list.html", context)