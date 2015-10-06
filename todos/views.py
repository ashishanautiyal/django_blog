from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Todos
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todos
from .serializers import PostSerializer
#from talk.forms import PostForm

import time
import datetime

def datetime_to_milliseconds(some_datetime_object):
    timetuple = some_datetime_object.timetuple()
    timestamp = time.mktime(timetuple)
    return timestamp * 1000.0



def index(request):
    latest_question_list = Todos.objects.all()[:5]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))



@api_view(['GET', 'POST'])
def post_collection(request):

    if request.method == 'GET':
        posts = Todos.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = { "name": request.DATA.get('name'), "description": request.DATA.get('description'),"created": timezone.now() }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
def delete_todo (request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pk = request.DATA.get('pk')
        Todos.objects.filter(pk=pk).delete()
        return  Response('ok', status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def update_todo(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
       pk = request.DATA.get('pk')
       try:
           obj = Todos.objects.get(pk=pk)
           obj.name = request.DATA.get('name')
           obj.description = request.DATA.get('description')
           obj.created = timezone.now()
           obj.save()
       except Todos.DoesNotExist:
           obj = Todos.objects.create(name=request.DATA.get('name'),description = request.DATA.get('description'),created = timezone.now() )
       return  Response('ok', status=status.HTTP_201_CREATED)







