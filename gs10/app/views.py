from django.shortcuts import render
from . models import Chat,Group
# Create your views here.
def index(request,group_name):
    print("Group name...",group_name)
    # group = Group.objects.filter(name = group_name).first()

    # if group:
    #     pass
    # else:
    #     group = Group(name = group_name)
    #     group.save()
    return render(request,'app/index.html',{'groupname':group_name})
