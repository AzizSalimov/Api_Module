from django.urls import path

from products.views import get_products_list, get_product, category, category_detail

urlpatterns = [
    # api_view
    path("", get_products_list, name="products_list"),
    path('categories/', category, name='categories'),
    path('categories/<int:pk>/', category_detail, name = 'categoriy-detail'),

    path("<int:pk>/", get_product, name="products_detail"),
    # path("<slug:slug>/", get_product, name="products_detail"),
]