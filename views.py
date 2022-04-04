from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse

from login_management.models import Order,Transaction
from datetime import datetime

def time():
    current_time = datetime.now()
    date_time = current_time.strftime("YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")  
    return date_time
# Create your views here.
class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'hopping_cart.html', context=None)
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        context = {
            'name':name,
            'email':email,
            'phone':phone
        }
        template = loader.get_template('result.html')

        return HttpResponse(template.render(context,request))

    else :
            #if post request is not true
            #returning the form template
            template = loader.get_template('hopping_cart.html')
            return HttpResponse(template.render())

def checkout(request):
    if request.method == 'POST':
        amount = request.POST.getlist('amount[]')
        product_name = request.POST.getlist('product_name[]')
        price_totol = request.POST.get('total_amount')
        order_id = Order.objects.create(price_totol=price_totol) 
        
        for i in  range (len(amount)) :
            Transaction.objects.create(product_name=product_name[i] , quantity = 1 ,rice = amount[i] , order = order_id )
        

        context = {
            'amount':amount,
            'product_name':product_name,
           
        }
        template = loader.get_template('result.html')

        return HttpResponse(template.render(context,request))

    else :
            #if post request is not true
            #returning the form template
            template = loader.get_template('hopping_cart.html')
            return HttpResponse(template.render())

def dashboard(request):
    transaction_all =  Transaction.objects.all()
    context = {'transaction_all': transaction_all}
 
    template = loader.get_template('result.html')

    return HttpResponse(template.render(context,request))