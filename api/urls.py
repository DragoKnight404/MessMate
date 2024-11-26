from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.viewsets_crud import (
    UserProfileViewSet,
    IngredientViewSet,
    MenuViewSet,
    MenuIngredientViewSet,
    OrderViewSet,
    OrderItemViewSet,
    NotificationViewSet,
    ReviewViewSet,
    ExcelUploadLogViewSet,
    OrderModificationViewSet,
    InventoryViewSet,
    IngredientRequirementViewSet,
    InventoryPurchaseViewSet,
    RawMaterialToIngredientViewSet,
    BillViewSet,
    UserRegistrationViewSet
)
from .views.analytics_views import *


# Initialize the DRF router
router = DefaultRouter()

# Register each ViewSet with the router
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'menuingredients', MenuIngredientViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'exceluploadlogs', ExcelUploadLogViewSet)
router.register(r'ordermodifications', OrderModificationViewSet)
router.register(r'inventories', InventoryViewSet)
router.register(r'ingredientrequirements', IngredientRequirementViewSet)
router.register(r'inventorypurchases', InventoryPurchaseViewSet)
router.register(r'rawmaterialtoingredients', RawMaterialToIngredientViewSet)
router.register(r'bills', BillViewSet)
router.register(r'userregistration', UserRegistrationViewSet)

# Include router.urls in the main URL configuration
urlpatterns = [
    path('', include(router.urls)),
    path('reviews/average-rating/<int:menu_item_id>/', average_rating_view, name='average_rating'),
    path('reviews/top-rated/', top_n_rated_items_view, name='top_rated_items'),
    path('orders/stats/<str:timeframe>/', aggregate_order_stats, name='aggregate_order_stats'),
    path('orders/custom-stats/', custom_aggregate_order_stats, name='custom_aggregate_order_stats'),
    # path('orders/graph/<str:timeframe>/', order_graph_data, name='order_graph_data'),
    path('orders/custom-graph/', custom_order_graph_data, name='custom_order_graph_data'),
    # path('orders/menu-item/<str:timeframe>/', aggregate_order_by_menu_item, name='aggregate_order_by_menu_item'),
    path('orders/custom-menu-item-stats/', custom_aggregate_order_by_menu_item, name='custom_aggregate_order_by_menu_item'),
    # path('orders/menu-item/graph/<str:timeframe>/', order_graph_by_menu_item, name='order_graph_by_menu_item'),
    path('orders/custom-menu-item-graph/', custom_order_graph_by_menu_item, name='custom_order_graph_by_menu_item'),
    path('orders/time-of-day/<str:timeframe>/', custom_aggregate_order_by_time_of_day, name='aggregate_order_by_time_of_day'),
    #path('orders/time-of-day/graph/<str:timeframe>/', graph_order_by_time_of_day, name='graph_order_by_time_of_day'),
    path('orders/custom-time-of-day-graph/', custom_graph_order_by_time_of_day, name='custom_graph_order_by_time_of_day'),  # New function

]

# aj, aj1
