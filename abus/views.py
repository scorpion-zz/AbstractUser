from django.http import HttpResponse
from django.shortcuts import render

from abus.models import MyAbUser


def get_abstract_user(requets):
    u = MyAbUser.objects.all()
    # u = MyAbUser.objects.filter(id=2)


    for i in u:
        # i.cender = "m"
        # i.username = "Johan"
        print(i.cender,"111")
        print(i.username,"222222")
        # i.save()
    return HttpResponse("Gud luck 1")