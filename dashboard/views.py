from django.shortcuts import render
from dashboard.models import PropertyModel
import pandas as pd



def dashboard(request):
    queryset=PropertyModel.objects.values_list("location", "property_type","price","sold")
    dataset=pd.DataFrame(list(queryset), columns=["location", "property_type","price","sold"])
    avg=dataset["price"].mean()
    queryset=dataset.to_dict("records")
    return render(request, 'dashboard.html', {'properties':queryset, 'avg':avg})



