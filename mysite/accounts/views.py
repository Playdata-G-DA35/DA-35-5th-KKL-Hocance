from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():

            
            form.save() # 자동저장
            # 회원가입 후 자동으로 로그인 처리
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})