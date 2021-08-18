from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from Blog import settings
from .views import HomeView, PostDetailView, SignUpView, SignInView, FeedBackView, SuccessView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('lib/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout',),
    path('contact/', FeedBackView.as_view(), name='contact'),
    path('contact/success/', SuccessView.as_view(), name='success'),
]
