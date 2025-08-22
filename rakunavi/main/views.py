from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Program

def index(request):
    return render(request, 'main/index.html')

def program_list(request):
    programs = Program.objects.all()
    # セッション別に分ける
    morning = programs.filter(session='AM')
    afternoon = programs.filter(session='PM')
    return render(request, 'main/program.html', {
        'morning': morning,
        'afternoon': afternoon,
    })

def program_detail(request, number):
    program = get_object_or_404(Program, number=number)
    return render(request, 'main/program_detail.html', {
        'program': program
    })