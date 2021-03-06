from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # path('content_creators/', views.CreatorList.as_view()),
    # path('content_creator/<int:pk>/', views.CreatorDetail.as_view()),
    path('blog_content_creator/', views.BlogList.as_view()),
    path('blog_content/all', views.BlogList2.as_view()),
    path('blog_content_creator/<int:pk>/', views.BlogDetail.as_view()),
    path('digital_products_creator/', views.Digital_ProductList.as_view()),
    path('digital_products/all/', views.Digital_ProductList2.as_view()),
    path('digital_product/<int:pk>/', views.Digital_ProductDetail.as_view()),
    path('reviews/', views.ReviewList.as_view()),
    path('review/<int:pk>/', views.ReviewDetail.as_view()),
    path('code_snippets_creator/', views.Code_SnippetList.as_view()),
    path('code_snippets/all', views.Code_SnippetList2.as_view()),
    path('code_snippet/<int:pk>/', views.Code_SnippetDetail.as_view()),
    path('videos_creator/', views.VideoList.as_view()),
    path('videos/all/', views.VideoList2.as_view()),
    path('video/<int:pk>/', views.VideoDetail.as_view()),
    path('image_creator/', views.ImageList.as_view()),
    # path('authenticate/', views.LoginList.as_view()),
    path('token-auth/', obtain_jwt_token),
    path('current_user/', views.current_user),
    path('users/', views.UserList.as_view()),
    path('test_payment/', views.PaymentList.as_view()),
    path('save_stripe_info/', views.Save_Stripe_Info.as_view())
]
