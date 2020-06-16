from django.shortcuts import render
from django.http import HttpResponse
from .models import PageHitCounter
from django.template import loader
# Create your views here.

def counter(request):
    #_count=1
    template=loader.get_template(r'../templates/base.html')
    _count=PageHitCounter.update_count()
    # if PageHitCounter.objects.count() == 0:
    #     #Add field for counter
    #     count=PageHitCounter()
    #     count.counter=PageHitCounter.objects.count()
    #     count.save()
    # else:
    #     _count=PageHitCounter.count()
    #     _count=_count+1
    #     PageHitCounter.counter=_count


    return HttpResponse(template.render({'counter':_count},request))

