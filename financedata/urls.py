from django.urls import path
from . import views

app_name = "financeapp"
urlpatterns = [
    path('icform/<str:prop_id>/', views.IC_view, name='ic-form'),
    path('add-internalcost/', views.AddInterncalCost.as_view(), name='add-ic'),
    path('update-internalcost/', views.UpdateInternalCost.as_view(), name='update-ic')
]
