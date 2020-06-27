from django.shortcuts import render, redirect
from django.urls import reverse
from dashboard import models
import pandas as pd



def dashboard(request):


    properties=models.PropertyModel.objects.values_list("area","property_type","price", "sold")
    dataset=pd.DataFrame(list(properties), columns=["area","property_type","price", "sold"])
    avg=dataset["price"].mean()
    properties=dataset.to_dict("records")


    if request.method == 'POST':

        form_area = request.POST['area']
        form_property_type = request.POST['property_type']
        form_price = request.POST['price']

        models.PropertyModel.objects.create(area=form_area, property_type=form_property_type, price=form_price)



        return redirect(reverse("dashboard"))





    return render(request,"dashboard.html", {'properties': properties, "avg": avg} )


