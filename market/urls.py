from django.conf.urls import url
from django.urls import path
from .views import (
    CompanySelectionView,
    CompanyTransactionView,
    CompanyCMPChartData,
    CompanyCMPCreateView,
    CompanyAdminCompanyUpdateView,
    deduct_tax,
    update_market
)


app_name = 'Market'


urlpatterns = [
    path('select/', CompanySelectionView.as_view(), name='company_select'),
    path('transact/<code>', CompanyTransactionView.as_view(), name='transaction'),
    path('admin/<code>', CompanyAdminCompanyUpdateView.as_view(), name='admin'),
    path('create/', CompanyCMPCreateView.as_view(), name='create_cmp'),
    path('company/api/<code>', CompanyCMPChartData.as_view(), name='cmp_api_data'),
    path('tax/', deduct_tax, name='tax'),
    path('update/', update_market, name='update')
]
