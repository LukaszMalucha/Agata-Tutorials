from django.shortcuts import render
from dashboard.models import PropertyModel
import pandas as pd





def dashboard(request):
    dataset=pd.read_csv('cork_sales_2018.csv', encoding="utf-8")
    properties = dataset.to_dict('records')
    property_average = dataset["price"].mean()

    # all_properties=PropertyModel.objects.values('name','city','price','sold')
    # dataset=pd.DataFrame(list(all_properties), columns=['name','city','price','sold'])
    # property_average=dataset["price"].mean()
    #
    # properties=dataset.to_dict('records')



    return render (request, 'dashboard.html', {'properties': properties, 'property_average':property_average})

