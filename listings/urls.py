from django.urls import path
from . import views
urlpatterns = [
	path('', views.listings_listview, name="listings"),
	path('<int:list_id>/', views.listings_detailview, name='listing'),
	path('buy/<int:list_id>/', views.listings_buy, name='listing_buy'),
	path('buyc/<int:list_id>/', views.confirm_buy, name='listing_buy_confirm'),
	path('create/', views.listings_createview, name='listing_create'),
	path('update/<int:list_id>/', views.listings_updateview, name='listing_update'),
	path('delete/<int:list_id>/', views.listings_deleteview, name='listing_delete'),
	path('delete/confirm/<int:list_id>/', views.listings_confirmdeleteview, name='listing_confirmdelete'),
]