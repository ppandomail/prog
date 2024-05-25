import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def hola(request):
  doc_externo = open('django_02_template/hola.html')
  plt = Template(doc_externo.read())
  doc_externo.close()
  ctx = Context()
  doc = plt.render(ctx)
  return HttpResponse(doc)

def chau(request):
  doc_externo = open('django_02_template/chau.html')
  plt = Template(doc_externo.read())
  doc_externo.close()
  ctx = Context({'nom': 'Mundo'})
  doc = plt.render(ctx)
  return HttpResponse(doc)

def fecha(request):
  doc_externo = open('django_02_template/fecha.html')
  plt = Template(doc_externo.read())
  doc_externo.close()
  ctx = Context({'fecha': datetime.datetime.now()})
  doc = plt.render(ctx)
  return HttpResponse(doc)
  
def temas(request):
  doc_externo = open('django_02_template/temas.html')
  plt = Template(doc_externo.read())
  doc_externo.close()
  ctx = Context({'temas': ['t1', 't2', 't3']})
  doc = plt.render(ctx)
  return HttpResponse(doc)

def corto(request):
  return render(request, 'django_02_template/temas.html', {'temas': ['t1', 't2', 't3']})