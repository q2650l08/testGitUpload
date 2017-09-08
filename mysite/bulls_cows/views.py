from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from random import randint
import json


class Entity(object):
    def __init__(self): 
        self.number = 0
        self.result = False

def bulls_cows(request):
  
    if request.method == "POST":

       
        myList = []
        
        if request.session.get('myList') :
            myList = request.session['myList']


        entity = Entity()
        entity.number = request.POST['input_number']


        if int(request.session['target_number']) == int(entity.number) :
            entity.result = True
        else :
            entity.result = False

        myList.append(entity.__dict__ )

        request.session['myList'] = myList
        
      

        return render(request, "bulls_cows.html", {'myList':myList})
   

       # return render(request, "bulls_cows.html", {'myList':json.dumps(myList), })
    else:
        request.session['target_number'] =  randint(1, 99)

        print("The Fuckin Ans : " , request.session['target_number'])

        if request.session.get('myList') :
            del request.session['myList']
    
        return render(request, "bulls_cows.html")


    
