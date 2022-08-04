# from xml.dom.minidom import Document
# from django.shortcuts import render

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# # Create your views here.
# def index(req) :
#     context = {
        
#     }
    
#     return render(req, 'ITSAC_WEB/index.html', context=context)

def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('ITSAC_WEB/home/dashboard.html')
    return HttpResponse(html_template.render(context, request))

def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('ITSAC_WEB/home/' + load_template + '.html')
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('ITSAC_WEB/home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('ITSAC_WEB/home/page-500.html')
        return HttpResponse(html_template.render(context, request))