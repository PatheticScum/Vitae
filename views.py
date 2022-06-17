from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView
from django.contrib import messages
from .models import Category, Wallpaper, Anime, NFT
from .forms import LoginForm, RegistrationForm, SendCommentForm

from project import settings


# Main Page


def index(request):
    return render(request, 'blog/index.html')


# All Wallpapers

class WallpaperList(ListView):
    template_name = 'blog/all_wallpapers.html'
    model = Wallpaper
    context_object_name = 'wallpapers'
    extra_context = {
        'title': 'All wallpapers from classes'
    }
    paginate_by = 10

    def get_queryset(self):
        return Wallpaper.objects.all()


# Wallpapers Category

class WallpaperListByCategory(WallpaperList):
    template_name = 'blog/all_wallpapers.html'

    def get_queryset(self):
        return Wallpaper.objects.filter(
            category_id=self.kwargs['pk']
        ).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context


# Wallpaper Detail

def wallpaper_detail(request, pk):
    wallpaper = Wallpaper.objects.get(pk=pk)
    context = {
        'title': wallpaper.title,
        'wallpaper': wallpaper
    }

    return render(request, 'blog/details.html', context)


# Anime


class AnimeList(ListView):
    template_name = 'blog/animes.html'
    model = Anime
    context_object_name = 'animes'
    paginate_by = 10

    def get_queryset(self):
        return Anime.objects.all()


def anime_detail(request, pk):
    anime = Anime.objects.get(pk=pk)
    context = {
        'title': anime.title,
        'anime': anime
    }

    return render(request, 'blog/anime_details.html', context)


#   NFT


class NFTList(ListView):
    template_name = 'blog/nfts.html'
    model = NFT
    context_object_name = 'nfts'
    paginate_by = 10

    def get_queryset(self):
        return NFT.objects.all()


def nft_detail(request, pk):
    nft = NFT.objects.get(pk=pk)
    context = {
        'title': nft.title,
        'nft': nft
    }

    return render(request, 'blog/nft_details.html', context)


# Search

class SearchResults(WallpaperList, AnimeList, NFTList):
    def get_queryset(self):
        word = self.request.GET.get('q')
        wallpaper = Wallpaper.objects.filter(title__contains=word)
        return wallpaper


# Creator

def creator(request):
    return render(request, 'blog/creator.html')


# Profile

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'blog/profile.html')
    else:
        context = 'Log in or Registrate in order to view the profile page.'
        return HttpResponse(context)


# About Size Page

def about_site(request):
    return render(request, 'blog/about_site.html')


# User Form

def user_form(request):
    login_form = LoginForm()
    registration_form = RegistrationForm()

    context = {
        'login_form': login_form,
        'registration_form': registration_form,
    }

    return render(request, 'blog/user_form.html', context)


# Login

def user_login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('index')
    else:
        messages.error(request, 'Incorrect username or password')
        return redirect('user_form')


# Register

def register(request):
    form = RegistrationForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        errors = form.errors
        messages.error(request, errors)
    return redirect('user_form')


# Logout

def user_logout(request):
    logout(request)
    return redirect('index')


def send_comment(request):
    if request.method == 'POST':
        data = request.POST
        email = data['email']
        subject = data['subject']
        comment = data['comment']

        send_mail(
            f'{subject}',
            comment + f'\n\n\n{email}',
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER]
        )

        return redirect('index')
    return render(request, 'blog/_send_email.html')

# style='background-image: url({% static "store/images/email_form-bg.png" %});'
# darkinnspire2022@gmail.com