from django.http import HttpResponse
from django.shortcuts import render

import random

def hello_world(request):
    return HttpResponse("Hello World")

def root_page(request):
    return render(request,'index.html')

def random_number(request, max_rand=100):
    random_num = random.randrange(0, int(max_rand))

    msg = "Random Number Between 0 and %s : %d" % (max_rand, random_num)

    return HttpResponse(msg)

