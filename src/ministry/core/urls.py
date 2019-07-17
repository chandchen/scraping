from django.urls import path
from django.conf import settings
from django.conf.urls import static

from ministry.core import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('gmail/', views.GmailListView.as_view(), name='gmail-list'),
    path('ebay/', views.EbayListView.as_view(), name='ebay-list'),
    path('paypal/', views.PaypalListView.as_view(), name='paypal-list'),
]


if settings.DEBUG:
    urlpatterns += static.static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
