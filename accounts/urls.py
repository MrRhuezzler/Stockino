#from django.conf.urls import url
from django.urls import path

from .views import AccountEmailActivateView, LoanView, cancel_loan, deduct_interest


app_name = 'Account'


urlpatterns = [
    path('email/confirm/<key>/', AccountEmailActivateView.as_view(), name='email-activate'),
    path('email/resend-activation/', AccountEmailActivateView.as_view(), name='resend-activation'),
    path('bank/loan', LoanView.as_view(), name='loan'),
    # cancel_loan
    path('bank/loan/deduct', cancel_loan, name='cancel_loan'),
    path('bank/interest/deduct', deduct_interest, name='deduct_interest'),
]
