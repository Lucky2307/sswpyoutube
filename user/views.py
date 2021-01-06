from django.shortcuts import render, redirect, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model, login as user_login, logout as user_logout, authenticate
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_decode
login_required = login_required(login_url='user:login')

from .email import send_activation_mail, send_reset_mail
from .forms import UserCreateForm, PasswordResetForm, AuthenticationForm, SetPasswordForm
from .tokens import RegisterTokenGenerator

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('landingpage')
    User = get_user_model()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = form.save(commit=False)
            user.is_active = False
            # User is_active attribute is set to False before activation.
            # Will be usable after the user confirm their email.

            user.save()
            current_site = get_current_site(request)
            send_activation_mail(user, email, current_site)
            return render(request, 'signup_confirm.html', {})
    else:
        form = UserCreateForm()

    context = {'form':form}
    return render(request, 'signup.html', context)

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        # Checks if user exist
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist) as e:
        user = None
    finally:
        if user is not None and RegisterTokenGenerator().check_token(user, token):
            # Checks if user token is valid
            user.is_active = True
            user.save()
            return redirect('user:login')
        else:
            return render(request, 'password_reset_confirm.html', {'invalid': True})

@login_required
def logout(request):
    user_logout(request)
    try:
        nextUrl = request.GET.get('next')
        return redirect(nextUrl)
    except:
        pass
    return redirect('videos-index')

def login(request):
    if request.user.is_authenticated:
        return redirect('landingpage')
    form = AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            user_login(request, user)
            try:
                nextUrl = request.POST.get('next')
                return redirect(nextUrl)
            except:
                pass
            return redirect('index')
    context = {'form': form}
    return render(request, 'login.html', context)


def password_reset(request):
    if request.user.is_authenticated:
        return redirect('landingpage')
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        email = form.data['email']
        current_site = get_current_site(request)
        send_reset_mail(email, current_site)
    context = {'form':PasswordResetForm}
    return render(request, 'password_reset.html', context)

def password_reset_confirm(request, uidb64, token):
    User = get_user_model()
    try:
        # Checks if user exist
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist) as e:
        user = None
    finally:
        if user is not None and PasswordResetTokenGenerator().check_token(user=user, token=token):
            if request.method == 'POST':
                form = SetPasswordForm(user=user, data=request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('user:login')
                return render(request, 'password_reset_confirm.html', {'form': form})

            form = SetPasswordForm(user)
            context = {'form':form}
            return render(request, 'password_reset_confirm.html', context)
        else:
            return render(request, 'password_reset_confirm.html', {'invalid': True})