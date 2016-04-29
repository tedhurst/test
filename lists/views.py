from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item


# Create your views here.
#def home_page(request):
#    return HttpResponse('<html><title>To-Do lists</title></html>')
def home_page(request):
##    item = Item()
##    item.text = request.POST.get('item_text', '')
##    item.save()
    if request.method == 'POST':
##        new_item_text = request.POST['item_text']
##        Item.objects.create(text=new_item_text)
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    #items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
##    else:
##        new_item_text = ''
##    
##    return render(request, 'home.html', {
##        'new_item_text': new_item_text
##    })
##    return render(request, 'home.html')

##    if request.method == 'POST':
##        return HttpResponse(request.POST['item_text'])
##    return render(request, 'home.html')

#home_page = None

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items}) 
