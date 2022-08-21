from django.shortcuts import render
from django.http import HttpResponse


from app_name.models import Check


# Create your views here.
def main(request):
    # check1 = Check.objects.create(abc="888", xyz="789")
    # print("check 1:", check1)
    
    check2 = Check.objects.get(abc="123")
    print("check 2:", check2)
    
    col_name = "abc"
    col_name = col_name + "123"
    setattr(check2, col_name, "afadsfasd")
    check2.save()
    
    return HttpResponse("성공!")
    