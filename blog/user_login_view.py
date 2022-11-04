from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render


def user_login(request):
    if request.method == 'POST':
        username_ = request.POST['username']
        print(username_)
        password_ = request.POST['password']
        print(password_)
        user = authenticate(request, username=username_, password=password_)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('blog:main'))
        else:
            context = {'wrong_data': True}
            return render(request, 'blog/blog-login.html', context)
    else:
        return render(request, 'blog/blog-login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:login'))


def authentication(request):
    if not request.user.is_authenticated:
        return redirect('blog:login')
    else:
        return HttpResponse("Hello, You are logged in.")
