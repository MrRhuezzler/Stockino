#from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('password/change/',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'
        ),
    path('password/change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
        ),
    path('password/reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'
        ),
    path('password/reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
        ),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'
        ),
    path('password/reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
        ),
]
