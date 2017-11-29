from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import generic
from .models import Product, Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm
from django.views.generic import View

from django.core.mail import send_mail
from django.conf import settings
from .async_email import send_email
import asyncio
# import aiosmtplib


# Class based views


class IndexView(generic.ListView):
    template_name = 'core/index.html'

    def get_queryset(self):
        return Product.objects.all()


class DetailView(generic.DetailView):
    model = Product
    template_name = 'core/product.html'


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'price', 'quantity', 'category']
    # template_name = 'core/product_form.html'


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'price', 'quantity', 'category']


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('core:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'core/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            email_subject = "Welcome " + str(username)

            # async email logic
            # REDIRECT TO HOME PAGE BEFORE EMAIL IS SENT
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_in_executor(None, send_mail, email_subject,
                                 "TEST MESSAGE",
                                 settings.EMAIL_HOST_USER,
                                 [email])
            loop.close()

            # return user object if credentials are correct.
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('core:index')

        return render(request, self.template_name, {'form': form})
