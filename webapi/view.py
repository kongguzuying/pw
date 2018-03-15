from django.http import HttpResponse
from tmodel.models import Goods

def hello(request):
    return HttpResponse('HelloWorld');


def save_goods(request):
    g = Goods(title='123', url='321')
    g.save()
    return HttpResponse('save success');
    

def get_goods(request):
    g = Goods.objects.filter(title='123')
    return HttpResponse(g)
