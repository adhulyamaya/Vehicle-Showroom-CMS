from django.db import models
from main.models import BaseModel
from django.utils.translation import gettext_lazy as _
from datetime import date


def blog_image_upload_path(instance, filename):
    return f'blog_images/{instance.id}/{filename}'

def showroom_image_upload_path(instance, filename):
    return f'showroom_images/{instance.id}/{filename}'


class Blog(BaseModel):
    title = models.CharField(_("Blog Title"), max_length=255)
    content = models.TextField(_("Content"), blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    is_active = models.BooleanField(_("Is this blog active?"), default=True)
    is_deleted = models.BooleanField(_("Is this blog deleted?"), default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog_blog'
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return self.title


class Showroom(BaseModel):
    name = models.CharField(_("Showroom Name"), max_length=255)
    location = models.CharField(_("Location"), max_length=500, blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    image_file = models.ImageField(_("Showroom Image"), upload_to=showroom_image_upload_path, blank=True, null=True)
    contact_person = models.CharField(_("Contact Person"), max_length=255, blank=True, null=True)
    phone = models.CharField(_("Phone Number"), max_length=20, blank=True, null=True)
    email = models.EmailField(_("Email"), blank=True, null=True)
    website = models.URLField(_("Website"), blank=True, null=True)

    is_active = models.BooleanField(_("Is this showroom active?"), default=True)
    is_deleted = models.BooleanField(_("Is this showroom deleted?"), default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'showroom_showroom'
        verbose_name = _('Showroom')
        verbose_name_plural = _('Showrooms')

    def __str__(self):
        return self.name

