from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TourInfo
from .models import SpotInfo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.
@login_required
def post(request):
    logged_in_user = request.user
    return render(request, 'create/post.html', {})

@login_required
def account(request):
    logged_in_user = request.user
    posts = TourInfo.objects.filter(user = logged_in_user, published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'create/account.html', {'posts':posts})

@login_required
def accountedit(request):

    return render(request, 'create/accountedit.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
