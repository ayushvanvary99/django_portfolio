from django.shortcuts import render
from .models import UserDetail, ToolStack, TechStack, Projects

# Create your views here.


def home(request):
    user_info = UserDetail.objects.all()
    tech_info = TechStack.objects.all()
    tool_info = ToolStack.objects.all()
    proj_det = Projects.objects.all()

    data = {
        'user_info': user_info,
        'tech_info': tech_info,
        'tool_info': tool_info,
        'proj_det': proj_det,

    }
    return render(request, 'webpage/home.html', data)
