"""stockino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView
from django.urls import path

from .views import HomeView, instruction_view
from accounts.views import RegisterView, LoginView, LeaderBoardView, ProfileView, NewsView
from market.views import UserTransactionHistoryView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<username>/', ProfileView.as_view(), name='profile'),
    path('news/', NewsView.as_view(), name='news'),
    path('account/', include('accounts.urls', namespace='account')),
    path('accounts/', include('accounts.passwords.urls')),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('leaderboard/', LeaderBoardView.as_view(), name='leaderboard'),
    path('instructions/', instruction_view, name='instructions'),
    path('stocks/', include('market.urls', namespace='market')),
    path('history/', UserTransactionHistoryView.as_view(), name='transaction_history'),
    path('admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
