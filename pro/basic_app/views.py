from django.shortcuts import render

# Create your views here.
def index(request):
    dict={'text':'hello world', 'number':100}
    return render(request,'htmlfiles/index.html',context=dict)

def other_fun(request):
    return render(request,'htmlfiles/other.html')

def relative_fun(request):
    return render(request,'htmlfiles/relative_url_templates.html')
