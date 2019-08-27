from django.urls import path
from . import views

app_name = "kypsamhita"
urlpatterns = [
    path("proposal/<slug:proposal_slug>/", views.ProposalPage, name="proposal"),
    path("list/", views.ListingPage, name="listing"),
]
