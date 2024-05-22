from django.urls import path
from .views import *

app_name = 'products'
urlpatterns = [
    path('footwear-list', FootwearListView.as_view(), name='footwear-list'),
    path('detail/<int:pk>', FootwearDetailView.as_view(), name='footwear-detail'),
    path('delete/<int:pk>', FootwearDeleteView.as_view(), name='footwear-delete'),
    path('create', FootwearCreateView.as_view(), name='create-footwear'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add-review'),
    path('edit_review/<int:pk>', ReviewUpdateView.as_view(), name='edit-review'),
    path('category/', CategoriesListView.as_view(), name='category'),
    path('detail_info/<int:pk>', DetailInfoView.as_view(), name='detail-info'),
    path('detailview/', DetailView.as_view(), name='detail'),
    path('expensive/', ExpensiveProduct.as_view(), name='expensive'),
    path('cheap/',CheapProduct.as_view(), name='cheap'), 
]


