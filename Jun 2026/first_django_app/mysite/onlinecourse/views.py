from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Course
from datetime import date

def course_list(request):
    course = Course.objects.get(pk=1)
    template = "<html>" \
                "<body>The first course we created is `%s.`" \
                "</body>" \
                "</html>" %course.name
    return HttpResponse(content=template)

def get_date(request):
    today = date.today()
    template = "<html>" \
                f"Today's date is {today}" \
               "</html>"
    return HttpResponse(content=template)