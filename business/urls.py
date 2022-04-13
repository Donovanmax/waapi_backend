from django.urls import path, include

from . import views
urlpatterns = [
    path("business/", views.BusinessList.as_view()),
    path("userprofile/", views.AccountViews.as_view(), name='registration'),
    path("gmail/", views.AccountGmailViews.as_view(), name='registrationGmail'),

    path("user/<str:query>/", views.AccountLoginViews.as_view(), name='login'),
    
    path("types/", views.TypesView.as_view()),
    
    
    path("businessDetails/<str:id>/", views.BusinessDetails.as_view()),
    path("business/details/<str:id>/", views.DetailsList.as_view()),
    path("business/category/<str:query>/", views.CategoryList.as_view()),
    

]