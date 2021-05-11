from django.urls import path
from . import views
from .views import FilteredPizzaList

urlpatterns = [
  path('all_pizza_list/', views.pizza_list),
  path('create', views.create_item),
  path('pizza_list/filtered', FilteredPizzaList.as_view()),
  path('update/<int:pk>', views.update_item),
  path('delete/<int:pk>', views.delete_item)
]