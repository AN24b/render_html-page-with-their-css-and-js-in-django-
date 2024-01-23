from django.http import HttpResponse
from django.shortcuts import render

def aboutus(request):
    return HttpResponse("<b>Welcome</b>")

def coursedetails(request,courseid):
    return HttpResponse(courseid)

def homepage(request):
    #data={
        #'btext':'Welcome to my first django-project',
        #'clist':['PHP','JAVA','C++'],
        #'student_details':[
         #   {'name':'Anjali','phone':9307886567},
          #  {'name':'Disha','phone':9307885805}
        #]
    #S}
    return render(request,"index.html")
