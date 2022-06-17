from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),

    path('wallpaper-list/', WallpaperList.as_view(), name='wallpaper_list'),
    path('category/<int:pk>/', WallpaperListByCategory.as_view(), name='category_list'),
    path('category/<int:pk>', wallpaper_detail, name='wallpaper_detail'),

    path('animes/', AnimeList.as_view(), name='anime_list'),
    path('anime/<int:pk>', anime_detail, name='anime_detail'),

    path('nfts/', NFTList.as_view(), name='nft_list'),
    path('nft/<int:pk>', nft_detail, name='nft_detail'),

    path('search/', SearchResults.as_view(), name='search'),

    path('creator/', creator, name='creator'),

    path('about-site/', about_site, name='about_site'),

    path('profile/', profile, name='profile'),

    path('send-comment/', send_comment, name='send_comment'),

    path('login-register/', user_form, name='user_form'),
    path('register/', register, name='register'),
    path('login', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

]
