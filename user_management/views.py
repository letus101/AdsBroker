from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from Articles.models import Article 
from .form import CustomUserCreationForm, UserProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.forms import UserChangeForm
from .form import CustomUserCreationForm, UserProfileForm, CustomUserChangeForm  # Assurez-vous que c'est correctement importé.


def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = request.POST.get('phone_number')
            city = request.POST.get('city')
            photo = request.FILES.get('photo')
            UserProfile.objects.create(user=user, phone_number=phone_number, city=city, photo=photo)
            return redirect('article_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('article_list')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')

@login_required
def acceuil(request):
    return render(request, 'acceuil.html', {'user': request.user})

@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    articles = Article.objects.filter(author=request.user)

    user_form = CustomUserChangeForm(instance=request.user)
    profile_form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profil mis à jour avec succès.')
            return redirect('profile')  # Vérifiez le nom de l'URL du profil

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'articles': articles
    })
