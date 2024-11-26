from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum




# UserProfile Table
class UserProfile(models.Model):
    USER_ROLE_CHOICES = [
        ('user', 'User'),
        ('mess_staff', 'Mess Staff'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional field for phone number
    residence = models.CharField(max_length=255, blank=True, null=True)  # Optional field for residence
    is_college_student = models.BooleanField(default=False)  # Default is No
    college = models.CharField(max_length=255, blank=True, null=True)  # Optional field for college name
    lunch_timings = models.CharField(max_length=50, blank=True, null=True)  # Optional field for lunch timings

    def __str__(self):
        return self.user.username

# Ingredients Table
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    allergen_info = models.BooleanField(default=False)  # True if allergen
    is_vegan = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    base_unit = models.CharField(max_length=20, null=True, blank=True)  # Base unit for aggregation
    conversion_factor = models.FloatField(default=1, null=True,blank=True)  # E.g., 1 for grams, 1000 for kg
    
    def __str__(self):
        return self.name

# Menu Table
class Menu(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_tag = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='MenuIngredient', related_name="menus")
    available = models.BooleanField(default=True)
    serving_time = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # Path to image file
    # price = models.FloatField(max_digits=10, decimal_places=True)
    def __str__(self):
        return self.item_name

# MenuIngredient Table (for Many-to-Many Relationship)
class MenuIngredient(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()  # e.g., “2.0” for quantity
    unit = models.CharField(max_length=20, default="grams")  # Base unit for aggregation
    conversion_factor = models.FloatField(default=1)  # E.g., 1 for grams, 1000 for kg

    def __str__(self):
        return f"{self.menu.item_name} - {self.ingredient.name}"

# Order Table
class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('placed', 'Placed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready for Pickup'),
        ('completed', 'Completed'),
        ('cancelled','Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='placed')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

# OrderItem Table
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.menu.item_name}"

# Notification Table
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

# Review Table
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    OrderItem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    rating = models.IntegerField()  # Assuming rating is out of 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.menu.item_name}"

# ExcelUploadLog Table
class ExcelUploadLog(models.Model):
    staff = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # UserProfile for mess_staff
    file_path = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Upload by {self.staff.user.username} at {self.uploaded_at}"

# OrderModification Table (Optional)
class OrderModification(models.Model):
    MODIFICATION_TYPE_CHOICES = [
        ('cancel', 'Cancel'),
        ('modify', 'Modify'),
    ]
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    modification_type = models.CharField(max_length=10, choices=MODIFICATION_TYPE_CHOICES)
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Modification for Order {self.order.id} - {self.modification_type}"

class Bill(models.Model):
    
    PAYMENT_CHOICES = [
        ('Card', 'card'),
        ('Cash', 'cash'),
        ('UPI', 'upi')
    ]
    PAYMENT_STATUS_CHOICES = [
        ('paid','Paid'),
        ('pending','Pending'),
        ('cancelled','Cancelled'),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100, choices=PAYMENT_CHOICES, default='Cash')
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Inventory(models.Model):
    # Tracks available stock for each ingredient
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    quantity_in_stock = models.FloatField()  # The current stock level for each ingredient
    unit = models.CharField(max_length=20)   # e.g., "grams", "liters"
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.ingredient.name} - {self.quantity_in_stock} {self.unit}"



class IngredientRequirement(models.Model):
    # Tracks the monthly requirement for each ingredient based on orders
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    month = models.DateField()  # e.g., January 2024
    quantity_required = models.FloatField()  # Total amount required for the month

    def __str__(self):
        return f"{self.ingredient.name} - {self.month.strftime('%B %Y')} - {self.quantity_required} {self.ingredient.unit}"


class InventoryPurchase(models.Model):
    item_name = models.CharField(max_length=255)  # Name of the raw material or ingredient
    quantity = models.FloatField()                # Quantity of the purchased item
    unit = models.CharField(max_length=20)        # Units, e.g., "grams", "kg", "liters"
    purchase_date = models.DateTimeField(default=timezone.now)  # Time of purchase
    supplier = models.CharField(max_length=255, blank=True, null=True)  # Optional supplier info

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.item_name} purchased on {self.purchase_date}"

class RawMaterialToIngredient(models.Model):
    raw_material = models.ForeignKey(InventoryPurchase, on_delete=models.CASCADE)  # Link to InventoryPurchase
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)  # Link to Ingredient model
    conversion_rate = models.FloatField()  # Rate of raw material to ingredient (e.g., 2.5 kg of wheat -> 1 kg of flour)

    def __str__(self):
        return f"{self.raw_material.item_name} to {self.ingredient.name} conversion"


