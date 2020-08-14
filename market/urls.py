from django.conf.urls import url

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
    url(r'^select/$', CompanySelectionView.as_view(), name='company_select'),
    url(r'^transact/(?P<code>\w+)$', CompanyTransactionView.as_view(), name='transaction'),
    url(r'^admin/(?P<code>\w+)$', CompanyAdminCompanyUpdateView.as_view(), name='admin'),
    url(r'^create/$', CompanyCMPCreateView.as_view(), name='create_cmp'),
    url(r'^company/api/(?P<code>\w+)$', CompanyCMPChartData.as_view(), name='cmp_api_data'),
    url(r'^tax/$', deduct_tax, name='tax'),
    url(r'^update/$', update_market, name='update')
]
