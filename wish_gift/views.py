# views.py
from django.http import JsonResponse
from .models import List
from django.shortcuts import redirect
from .forms import ListForm


def gift_list(request):
    gifts = List.objects.all().values('owner', 'listItem')
    gift_list = list(gifts)
    return JsonResponse(gift_list, safe=False)


def gift_detail(request, pk):
    gift = List.objects.get(id=pk)
    data = {'owner': gift.owner, 'listItem': gift.listItem}
    return JsonResponse(data, safe=False)


# def gift_create(request):
#     if request.method == 'POST':
#         form = ListForm(request.POST)
#         if form.is_valid():
#             list = form.save()
#             return redirect('list_detail', pk=list.pk)
#     else:
#         form = ListForm()
#     # return JsonResponse(request, 'tunr/artist_form.html', {'form': form})
#     # data = {'owner': form.owner, 'listItem': form.listItem}
#     # return JsonResponse(data, safe=False)


def gift_delete(request, pk):
    List.objects.get(id=pk).delete()
    return redirect('gift_list')
