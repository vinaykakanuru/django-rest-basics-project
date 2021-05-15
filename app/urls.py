from django.urls import path

from app.views import (CheckListAPIView, CheckListItemAPIView,
                       CheckListItemCreateAPIView, CheckListsAPIView,
                       TestAPIView, test_api_view)

urlpatterns = [
    path('api/test/', test_api_view, name='test_api'),
    path('api/test/cbv/', TestAPIView.as_view(), name='test_api_cbv'),

    path('api/checklists/', CheckListsAPIView.as_view(), name='check_lists'),
    path('api/checklist/<int:pk>/', CheckListAPIView.as_view(), name='check_list'),

    path('api/checklistitem/create/', CheckListItemCreateAPIView.as_view(), name='check_list_item_create'),
    path('api/checklistitem/<int:pk>/', CheckListItemAPIView.as_view(), name='check_list_item'),
]
