from django.db import models
from django.utils.text import slugify
from django.db.models import UniqueConstraint

# Image Upload Path Function
def vehicle_image_upload_path(instance, filename):
    category = instance.vehicle.category.name.lower().replace(" ", "_")
    vehicle_name = instance.vehicle.title.lower().replace(" ", "_")
    color = instance.color.lower().replace(" ", "_")
    image_category = instance.get_image_category_display().lower().replace(" ", "_")
    return f'vehicle_images/{category}/{vehicle_name}/{color}/{image_category}/{filename}'

# Category Model
class Category(models.Model):
    """Vehicle categories (e.g., motorcycles, scooters)"""
    name = models.CharField("Category Name", max_length=100, unique=True)

    class Meta:
        db_table = "vehicle_category"
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# Vehicle Model
class Vehicle(models.Model):
    """Vehicles belonging to different categories"""
    title = models.CharField("Vehicle Title", max_length=300)
    slug = models.SlugField("Slug", unique=True, blank=True)
    description = models.TextField("Description", blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="vehicles"
    )
    uploaded_at = models.DateTimeField("Uploaded At", auto_now=True)  

    class Meta:
        db_table = "vehicle"
        ordering = ["-uploaded_at"]
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.category.name})"

# Variant Model
class Variant(models.Model):
    """Different variants of a vehicle categorized by color and image type"""
    IMAGE_CATEGORY_CHOICES = [
        ('practical', 'Practical'),
        ('executive', 'Executive'),
        ('performance', 'Performance'),
    ]

    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="variants"
    )
    title = models.CharField("Variant Title", max_length=300)
    description = models.TextField("Description", blank=True, null=True)
    color = models.CharField("Color", max_length=50)
    image_category = models.CharField("Image Category", max_length=20, choices=IMAGE_CATEGORY_CHOICES)
    image_file = models.ImageField("Variant Image", upload_to=vehicle_image_upload_path, blank=True, null=True)

    class Meta:
        db_table = "vehicle_variant"
        ordering = ["title"]
        verbose_name = "Variant"
        verbose_name_plural = "Variants"
        constraints = [
            UniqueConstraint(fields=['vehicle', 'color', 'image_category'], name='unique_vehicle_variant')
        ]

    def __str__(self):
        return f"{self.vehicle.title} - {self.title} - {self.color} - {self.get_image_category_display()}"

# Vehicle Price Model
class VehiclePrice(models.Model):
    """Unified Price Model for Vehicles (Bikes & Scooters)"""
    SPEC_TYPE_CHOICES = [
        ("base", "Base Model"),
        ("top", "Top Model"),
        ("standard", "Standard"), 
    ]

    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="prices"
    )
    spec_type = models.CharField(
        "Specification Type", max_length=10, choices=SPEC_TYPE_CHOICES, default="standard"
    )
    color = models.CharField("Color", max_length=50, blank=True, null=True)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)

    class Meta:
        db_table = "vehicle_price"
        constraints = [
            UniqueConstraint(fields=['vehicle', 'spec_type', 'color'], name='unique_vehicle_price')
        ]

    def __str__(self):
        details = [self.get_spec_type_display()]
        if self.color:
            details.append(self.color)
        return f"{self.vehicle.title} - {' / '.join(details)} - ₹{self.price}"
