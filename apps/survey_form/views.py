from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'survey_form/index.html')

def process(request):
    print 'hi'
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['favlang'] = request.POST['favlang']

    return redirect('/results')

def results(request):


    return render(request, 'survey_form/success.html')
