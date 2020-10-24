from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class IndexView(ListView):
    template_name = 'photo/index.html'
    context_object_name = 'photos'
    model = Photo


class PhotoView(DetailView):
    template_name = 'photo/photo_view.html'
    model = Photo


class PhotoCreateView(CreateView):
    template_name = 'photo/photo_create.html'
    form_class = PhotoForm
    model = Photo

    # permission_required = 'webapp.add_product'

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})

    # def has_permission(self):
    #     photo = self.get_object()
    #     return super().has_permission() or comment.author == self.request.user


class PhotoUpdateView(UserPassesTestMixin,UpdateView):
    template_name = 'photo/photo_update.html'
    form_class = PhotoForm
    model = Photo

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.has_perm('webapp.change_photo') or \
               self.get_object().author == self.request.user


class PhotoDeleteView(UserPassesTestMixin,DeleteView):
    template_name = 'photo/photo_delete.html'
    model = Photo
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        return self.request.user.has_perm('webapp.change_photo') or \
               self.get_object().author == self.request.user
#     permission_required = 'webapp.delete_product'
# permission_required = 'webapp.change_article'
#
# class ProductView(DetailView):
#     template_name = 'product/product_view.html'
#     model = Product
#
#
# class ProductCreateView(CreateView):
#     template_name = 'product/product_create.html'
#     form_class = ProductForm
#     model = Product
#     permission_required = 'webapp.add_product'
#
#     def post(self, request, *args, **kwargs):
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def get_success_url(self):
#         return reverse('webapp:product_view', kwargs={'pk': self.object.pk})
#
#
# class ProductUpdateVIew(UpdateView):
#     template_name = 'product/product_update.html'
#     model = Product
#     form_class = ProductForm
#     permission_required = 'webapp.change_product'
#
#     # def post(self, request, *args, **kwargs):
#     #     self.object = self.get_object()
#     #     form = self.form_class(request.POST, request.FILES)
#     #     if form.is_valid():
#     #         form.save()
#     #         return self.form_valid(form)
#     #     else:
#     #         return self.form_invalid(form)
#
#     def get_success_url(self):
#         return reverse('webapp:product_view', kwargs={'pk': self.object.pk})
#
#
# class ProductDeleteView(DeleteView):
#     template_name = 'product/product_delete.html'
#     model = Product
#     success_url = reverse_lazy('webapp:index')
#     permission_required = 'webapp.delete_product'
