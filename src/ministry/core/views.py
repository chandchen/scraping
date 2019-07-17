from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = ''
    template_name = "core/ministry/dashboard.html"

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return render(
                request, self.template_name,
                {'username': request.user.username,
                 'dashboard_active': 'active'})
        return super(UserLoginView, self).get(self, request, *args, **kwargs)


class UserLoginView(TemplateView):
    template_name = "core/ministry/login.html"

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('login')

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return super(UserLoginView, self).get(self, request, *args, **kwargs)


@csrf_exempt
@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect(reverse('login'))


class SettingsView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = ''
    template_name = "core/ministry/settings.html"

    # @csrf_exempt
    # def post(self, request, *args, **kwargs):
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return HttpResponseRedirect('/')
    #     return HttpResponseRedirect('login')

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return render(
                request, self.template_name,
                {'username': request.user.username})
        return super(SettingsView, self).get(self, request, *args, **kwargs)


class GmailListView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = ''
    template_name = "core/ministry/gmail_list.html"

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return render(
                request, self.template_name,
                {'username': request.user.username,
                 'gmail_active': 'active'})
        return super(SettingsView, self).get(self, request, *args, **kwargs)


class EbayListView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = ''
    template_name = "core/ministry/settings.html"

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return render(
                request, self.template_name,
                {'username': request.user.username,
                 'ebay_active': 'active'})
        return super(SettingsView, self).get(self, request, *args, **kwargs)


class PaypalListView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = ''
    template_name = "core/ministry/settings.html"

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        if request.user and request.user.is_authenticated:
            return render(
                request, self.template_name,
                {'username': request.user.username,
                 'paypal_active': 'active'})
        return super(SettingsView, self).get(self, request, *args, **kwargs)
