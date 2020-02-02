from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from attendance.models import timetable, course

import json
from datetime import date
import calendar

# Create your views here.

def home(req):
    my_date = date.today()
    day_of_week = calendar.day_name[my_date.weekday()]
    print(my_date)
    context = dict()
    context['name'] = timetable['user'][0]['name']
    context['day'] = day_of_week
    context['subject'] = timetable['user'][0]['table']['Monday']
    return render(req, template_name='attendance/home.html', context=context)

def course_detail(req, id):
    context = dict()
    context['detail'] = course[id]
    return render(req, template_name='attendance/course_detail.html', context=context)

def check_in(req, id):
    context = dict()
    context['subject'] = course[id]['name']
    context['id'] = id
    return render(req, template_name='attendance/check-in.html', context=context)