from django.shortcuts import render, get_object_or_404, redirect

from .models import *


class ObjectDetailMixin:

    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'object': obj, 'detail': True})


class ObjectCreateMixin:

    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form': form})

    def post(self, request):

        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)

        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:

    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, slug):

        obj = self.model.objects.get(slug=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)

        return render(request, self.template, context={'form': bound_form})


class ObjectDeletelMixin:

    model = None
    # model_form = None
    template = None
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, slug):
        obj = self.model.objects.get(slug=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
