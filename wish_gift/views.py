# views.py
from django.http import JsonResponse
from .models import List
from django.shortcuts import redirect
from .forms import ListForm


def gift_list(request):
    gifts = List.objects.all().values('id', 'owner', 'listItem')
    gift_list = list(gifts)
    return JsonResponse(gift_list, safe=False)


def gift_detail(request, pk):
    gift = List.objects.get(id=pk)
    data = {'id': gift.id, 'owner': gift.owner, 'listItem': gift.listItem}
    return JsonResponse(data, safe=False)


def gift_create(request, new_owner, new_listItem):
    gift = List.objects.create(owner=new_owner, listItem=new_listItem)
    return redirect('gift_list')


def gift_delete(request, pk):
    List.objects.get(id=pk).delete()
    return redirect('gift_list')

