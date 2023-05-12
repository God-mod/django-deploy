from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

clicked = 0

# 'request' name is convention. It can be some other name too.
def index(request) :
  global clicked
  clicked += 1
  my_dict = {'count' : clicked}
  return render(request, 'index.html', my_dict)

def help(request) :
  return render(request, 'help.html')

def process_form(request) :

    username = request.POST.get('user')

    password = request.POST.get('pwd')

    print(username, password)

    response = render(request, 'form.html')

    return response