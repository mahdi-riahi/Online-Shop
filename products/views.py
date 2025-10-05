from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic

from .forms import AuthenticatedCommentForm, AnonymousCommentForm
from .models import Product, Comment


class ProductListView(generic.ListView):
    queryset = Product.objects.filter(active=True).order_by('-datetime_modified')
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 4

    # def get_queryset(self):
    #     return Product.objects.filter(active=True).order_by('-datetime_modified')


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AuthenticatedCommentForm() if self.request.user.is_authenticated else AnonymousCommentForm()
        return context

# def product_detail_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     form = AuthenticatedCommentForm(request.POST or None) if request.user.is_authenticated else AnonymousCommentForm(
#         request.POST or None)
#     if form.is_valid():
#         new_comment = form.save(commit=False)
#         new_comment.product = product
#         if request.user.is_authenticated:
#             new_comment.author = request.user.username
#             new_comment.author_email = request.user.email
#         new_comment.save()
#         return redirect('product_detail', pk)
#     return render(request, 'products/product_detail.html', context={
#         'product': product,
#         'form': form,
#     })


class CommentCreateView(generic.CreateView):
    model = Comment

    def get_form_class(self):
        return AuthenticatedCommentForm if self.request.user.is_authenticated else AnonymousCommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        product = get_object_or_404(Product, pk=int(self.kwargs['pk']))
        obj.product = product
        if self.request.user.is_authenticated:
            obj.author = self.request.user.username
            obj.author_email = self.request.user.email
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.kwargs['pk']})
