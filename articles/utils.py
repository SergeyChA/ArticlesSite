from django.shortcuts import render, redirect
from .models import *


class ObjectUpdateMixin:
    model = None
    form_model = None
    temlate = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bount_form = self.form_model(instance=obj)
        return render(request, self.template, context={'form': bount_form, self.model.__name__.lower(): obj})
    
    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bount_form = self.form_model(request.POST, request.FILES, instance=obj)
        

        if bount_form.is_valid():
            update_obj = bount_form.save()
            return redirect(update_obj)
        return render(request, self.template, context={'form': bount_form, self.model.__name__.lower(): obj})

class ObjectDeleteMixin:
    model = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))

