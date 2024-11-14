from django.shortcuts import render
from My_First_App.models import Car, Author
from django.http import HttpResponse
from django.views.generic.base import TemplateView
# Create your views here.
def my_view(request):
    car_list = Car.objects.all()
    context = {
        'car_list': car_list
    }
    return render(request, "My_First_App/car_list.html", context)

class CarListView(TemplateView):
    template_name = "My_First_App/car_list.html"
    
    def get_context_data(self):
        car_list = Car.objects.all()
        return {'car_list': car_list}

def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")