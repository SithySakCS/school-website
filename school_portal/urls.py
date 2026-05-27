from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('apply/', views.apply_form, name='apply_form'),
    path('contact-submit/', views.contact_submit, name='contact_submit'),

    # Admin panel
    path('admin-panel/login/', views.admin_login, name='admin_login'),
    path('admin-panel/logout/', views.admin_logout, name='admin_logout'),
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/site-settings/', views.admin_site_settings, name='admin_site_settings'),
    path('admin-panel/hero/', views.admin_hero, name='admin_hero'),
    path('admin-panel/about/', views.admin_about, name='admin_about'),
    path('admin-panel/facilities/', views.admin_facilities, name='admin_facilities'),
    path('admin-panel/facilities/save/', views.admin_facility_save, name='admin_facility_add'),
    path('admin-panel/facilities/save/<int:pk>/', views.admin_facility_save, name='admin_facility_save'),
    path('admin-panel/facilities/delete/<int:pk>/', views.admin_facility_delete, name='admin_facility_delete'),
    path('admin-panel/offers/', views.admin_offers, name='admin_offers'),
    path('admin-panel/offers/save/', views.admin_offer_save, name='admin_offer_add'),
    path('admin-panel/offers/save/<int:pk>/', views.admin_offer_save, name='admin_offer_save'),
    path('admin-panel/offers/delete/<int:pk>/', views.admin_offer_delete, name='admin_offer_delete'),
    path('admin-panel/gallery/', views.admin_gallery, name='admin_gallery'),
    path('admin-panel/gallery/save/', views.admin_gallery_save, name='admin_gallery_add'),
    path('admin-panel/gallery/save/<int:pk>/', views.admin_gallery_save, name='admin_gallery_save'),
    path('admin-panel/gallery/delete/<int:pk>/', views.admin_gallery_delete, name='admin_gallery_delete'),
    path('admin-panel/applications/', views.admin_applications, name='admin_applications'),
    path('admin-panel/applications/<int:pk>/', views.admin_application_detail, name='admin_application_detail'),
    path('admin-panel/location/', views.admin_location, name='admin_location'),
    path('admin-panel/contact/', views.admin_contact, name='admin_contact'),
    path('admin-panel/messages/read/<int:pk>/', views.admin_message_read, name='admin_message_read'),
    path('admin-panel/messages/delete/<int:pk>/', views.admin_message_delete, name='admin_message_delete'),

    path('django-admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
