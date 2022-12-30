from django.urls import path
from . import views
app_name='shopping_app'
urlpatterns = [
    path('',views.allproduct_cat,name='all_products'),
    path('<slug:cat_slug>/',views.allproduct_cat,name='product_by_category'),
    path('<slug:cat_slug>/<slug:prod_slug>/',views.prod_detail,name='product_details'),

]
