from django.shortcuts import render
from django.utils import timezone
from .models import TourInfo
from .models import SpotInfo

# Create your views here.
def post_list(request):
    logged_in_user = request.user
    posts = TourInfo.objects.filter(user = user, published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'create/post_list.html', {'posts':posts})

def account(request):

    return render(request, 'create/account.html', {})

def accountedit(request):

    return render(request, 'create/accountedit.html', {})
