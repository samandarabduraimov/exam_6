from django.contrib import messages
from django.views.generic import  CreateView, DeleteView
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from .forms import AddReviewForm, ReviewUpdateForm, DetailInfo, DetailInfoForm
from .models import  Review, CategoryFootwears, Footwears
from django.urls import reverse_lazy
# Create your views here.


class FootwearListView(View):
    def get(self, request):
        footwear = Footwears.objects.all().order_by('-id')
        return render(request, 'footwear/footwear_list.html', {'footwear': footwear})


class FootwearDetailView(View):
    def get(self, request, pk):
        footwear = Footwears.objects.get(pk=pk)
        reviews = Review.objects.filter(footwear=pk)
        category_footwears = Footwears.objects.filter(category=footwear.category.pk)
        context = {
            'footwear': footwear,
            'reviews': reviews,
            'category_footwears': category_footwears
        }
        return render(request, 'footwear/footwear_detail.html', context=context)



class FootwearCreateView(CreateView):
    model = Footwears
    template_name = 'footwear/footwear_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:footwear-list')


class FootwearDeleteView(DeleteView):
    model = Footwears
    template_name = 'footwear/footwear_delete.html'
    success_url = reverse_lazy('products:footwear-delete')


class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        footwears = Footwears.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'footwears': footwears,
            'add_review_form': add_review_form
        }
        return render(request, 'footwear/add_review.html', context=context)

    def post(self, request, pk):
        footwears = Footwears.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                footwear=footwears,
                user=request.user,
                star_given=add_review_form.cleaned_data['star_given']
            )

            review.save()
            messages.success(request, "Review added successfully.")
            return redirect('products:footwear-detail', pk=pk)
        else:
            messages.error(request, "Failed to add review. Please check the form.")
            return render(request, 'footwear/add_review.html', {'footwears': footwears, 'add_review_form': add_review_form})
class DetailReview(View):
    def get(self, request, pk):
        footwear = Footwears.objects.get(id=pk)
        review = Review.objects.filter(gul=pk)
        view_comment = Review.objects.filter(gul=pk)
        context = {
            'footwear': footwear,
            'review': review,
            'view_comment': view_comment
        }
        return render(request, 'footwear/detail_review.html', context=context)

class ReviewUpdateView(View):
    def get(self, request, pk):
        review = Review.objects.get(pk=pk)
        update_review_form = ReviewUpdateForm(instance=review)
        context = {
            'update_review_form': update_review_form
        }
        return render(request, 'footwear/review_update.html', context=context)

    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        update_review_form = ReviewUpdateForm(request.POST, instance=review)
        if update_review_form.is_valid():
            update_review = update_review_form.save(commit=False)
            update_review.footwear_id = review.footwear_id
            update_review.save()
            return redirect('products:footwear-detail', pk=review.footwear_id)
        else:
            return render(request, 'footwear/review_update.html', {'update_review_form': update_review_form})


class CategoriesListView(View):
    def get(self, request):
        category = CategoryFootwears.objects.all()

        return render(request, 'footwear/products.html', {'categorys': category})
    
class DetailInfoView(View):
    def get(self, request, pk):
        footwear = Footwears.objects.get(id=pk)
        detail_form = DetailInfoForm()
        context = {
            'footwear': footwear,
            'detail_form': detail_form
        }
        return render(request, 'footwear/detail_info.html', context=context)

    def post(self, request, pk):
        detail_form = DetailInfoForm(request.POST)
        if detail_form.is_valid():
            # Assuming you have a way to get the product object
            product = Footwears.objects.get(pk=pk)
            detail = detail_form.save(commit=False)
            detail.product = product
            detail.save()
            return redirect('products:footwear-detail', pk=pk)
        else:
            return render(request, 'footwear/detail_info.html', {'detail_form': detail_form})


class DetailView(View):
    def get(self, request):
        details = DetailInfo.objects.all()
        context = {
            'details': details,
        }
        return render(request, 'footwear/detail_info_list.html', context=context)


class ExpensiveProduct(View):
    def get(self, request):
        products = Footwears.objects.all()
        sorted_expensive = products.order_by('-price')[:10]

        return render(request, 'footwear/expensive.html', {'products': sorted_expensive})


class CheapProduct(View):
    def get(self, request):
        products = Footwears.objects.all()
        sorted_cheap = products.order_by('price')[:3]

        return render(request, 'footwear/cheap.html', {'products': sorted_cheap})
