from rest_framework import viewsets
from api.models import UserProfile, Ingredient, Menu, MenuIngredient, Order, OrderItem, Notification, Review, ExcelUploadLog, OrderModification, Inventory, IngredientRequirement, InventoryPurchase, RawMaterialToIngredient,Bill
from api.serializers import (
    UserProfileSerializer,
    IngredientSerializer,
    MenuSerializer,
    MenuIngredientSerializer,
    OrderSerializer,
    OrderItemSerializer,
    NotificationSerializer,
    ReviewSerializer,
    ExcelUploadLogSerializer,
    OrderModificationSerializer,
    InventorySerializer,
    IngredientRequirementSerializer,
    InventoryPurchaseSerializer,
    RawMaterialToIngredientSerializer,
    BillSerializer, 
    UserRegistrationSerializer
)
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import status
from api.permissions import IsMessStaff, IsOwnerOrReadOnly
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    # permission_classes = [AllowAny]  # Allow any user to register

    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [AllowAny]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # General fallback

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # This creates the user and the user profile
        return Response({
            "user": UserProfileSerializer(user.userprofile).data,
            "message": "User created successfully."
        }, status=status.HTTP_201_CREATED)
 

# UserProfile ViewSet
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Associate the profile with the logged-in user

    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# Ingredient ViewSet
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# Menu ViewSet
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# MenuIngredient ViewSet
class MenuIngredientViewSet(viewsets.ModelViewSet):
    queryset = MenuIngredient.objects.all()
    serializer_class = MenuIngredientSerializer

    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# Order ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# OrderItem ViewSet
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# Notification ViewSet
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# Review ViewSet
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsAuthenticated]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# ExcelUploadLog ViewSet
class ExcelUploadLogViewSet(viewsets.ModelViewSet):
    queryset = ExcelUploadLog.objects.all()
    serializer_class = ExcelUploadLogSerializer
    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsAuthenticated,IsMessStaff]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated,IsMessStaff]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# OrderModification ViewSet
class OrderModificationViewSet(viewsets.ModelViewSet):
    queryset = OrderModification.objects.all()
    serializer_class = OrderModificationSerializer
    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsAuthenticated]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# Inventory ViewSet
class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# OrderAnalytics ViewSet

# IngredientRequirement ViewSet
class IngredientRequirementViewSet(viewsets.ModelViewSet):
    queryset = IngredientRequirement.objects.all()
    serializer_class = IngredientRequirementSerializer
    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# InventoryPurchase ViewSet
class InventoryPurchaseViewSet(viewsets.ModelViewSet):
    queryset = InventoryPurchase.objects.all()
    serializer_class = InventoryPurchaseSerializer
    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated,IsMessStaff]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

# RawMaterialToIngredient ViewSet
class RawMaterialToIngredientViewSet(viewsets.ModelViewSet):
    queryset = RawMaterialToIngredient.objects.all()
    serializer_class = RawMaterialToIngredientSerializer
    
    def get_permissions(self):
        # Default to AllowAny (anyone can view)
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only authenticated users can create
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsMessStaff]
        # Only mess staff can perform certain actions
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsMessStaff]
        else:
            permission_classes = [IsAuthenticated]  # General fallback

        return [permission() for permission in permission_classes]

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    
