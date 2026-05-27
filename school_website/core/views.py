from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import *

# ── HELPERS ──────────────────────────────────────────────────
def get_site_context():
    settings_obj, _ = SiteSettings.objects.get_or_create(pk=1)
    return {'site': settings_obj}

# ── FRONTEND ─────────────────────────────────────────────────
def home(request):
    ctx = get_site_context()
    ctx['hero'], _ = HeroSection.objects.get_or_create(pk=1)
    ctx['about'], _ = AboutSection.objects.get_or_create(pk=1)
    ctx['facilities'] = Facility.objects.filter(is_active=True)
    ctx['offers'] = Offer.objects.filter(is_active=True)
    ctx['gallery'] = GalleryItem.objects.all()[:12]
    ctx['location'], _ = LocationSection.objects.get_or_create(pk=1)
    ctx['contact'], _ = ContactSection.objects.get_or_create(pk=1)
    return render(request, 'core/home.html', ctx)

def apply_form(request):
    ctx = get_site_context()
    if request.method == 'POST':
        try:
            Application.objects.create(
                full_name=request.POST.get('full_name',''),
                date_of_birth=request.POST.get('date_of_birth'),
                gender=request.POST.get('gender',''),
                grade_applying=request.POST.get('grade_applying',''),
                parent_name=request.POST.get('parent_name',''),
                phone=request.POST.get('phone',''),
                email=request.POST.get('email',''),
                address=request.POST.get('address',''),
                message=request.POST.get('message',''),
            )
            return JsonResponse({'success': True, 'message': 'Application submitted successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return redirect('home')

def contact_submit(request):
    if request.method == 'POST':
        try:
            ContactMessage.objects.create(
                name=request.POST.get('name',''),
                email=request.POST.get('email',''),
                phone=request.POST.get('phone',''),
                subject=request.POST.get('subject',''),
                message=request.POST.get('message',''),
            )
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return redirect('home')

# ── ADMIN LOGIN/LOGOUT ────────────────────────────────────────
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        messages.error(request, 'Invalid credentials or not staff.')
    return render(request, 'admin_panel/login.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')

# ── ADMIN DASHBOARD ──────────────────────────────────────────
@login_required
def admin_dashboard(request):
    ctx = {
        'total_applications': Application.objects.count(),
        'new_applications': Application.objects.filter(status='new').count(),
        'total_gallery': GalleryItem.objects.count(),
        'total_facilities': Facility.objects.count(),
        'total_offers': Offer.objects.count(),
        'unread_messages': ContactMessage.objects.filter(is_read=False).count(),
        'recent_applications': Application.objects.all()[:5],
        'recent_messages': ContactMessage.objects.filter(is_read=False)[:5],
    }
    return render(request, 'admin_panel/dashboard.html', ctx)

# ── SITE SETTINGS ─────────────────────────────────────────────
@login_required
def admin_site_settings(request):
    obj, _ = SiteSettings.objects.get_or_create(pk=1)
    if request.method == 'POST':
        obj.school_name_en = request.POST.get('school_name_en', obj.school_name_en)
        obj.school_name_km = request.POST.get('school_name_km', obj.school_name_km)
        obj.tagline_en = request.POST.get('tagline_en', obj.tagline_en)
        obj.tagline_km = request.POST.get('tagline_km', obj.tagline_km)
        obj.phone = request.POST.get('phone', obj.phone)
        obj.email = request.POST.get('email', obj.email)
        obj.facebook = request.POST.get('facebook', obj.facebook)
        obj.instagram = request.POST.get('instagram', obj.instagram)
        if 'logo' in request.FILES:
            obj.logo = request.FILES['logo']
        obj.save()
        messages.success(request, 'Site settings saved!')
        return redirect('admin_site_settings')
    return render(request, 'admin_panel/site_settings.html', {'obj': obj})

# ── HERO EDITOR ───────────────────────────────────────────────
@login_required
def admin_hero(request):
    obj, _ = HeroSection.objects.get_or_create(pk=1)
    if request.method == 'POST':
        for f in ['title_en','title_km','subtitle_en','subtitle_km','badge_en','badge_km',
                  'btn1_en','btn1_km','btn2_en','btn2_km',
                  'stat1_num','stat1_label_en','stat1_label_km',
                  'stat2_num','stat2_label_en','stat2_label_km',
                  'stat3_num','stat3_label_en','stat3_label_km',
                  'stat4_num','stat4_label_en','stat4_label_km']:
            setattr(obj, f, request.POST.get(f, getattr(obj, f)))
        if 'background_image' in request.FILES:
            obj.background_image = request.FILES['background_image']
        obj.save()
        messages.success(request, 'Hero section saved!')
        return redirect('admin_hero')
    return render(request, 'admin_panel/hero.html', {'obj': obj})

# ── ABOUT EDITOR ──────────────────────────────────────────────
@login_required
def admin_about(request):
    obj, _ = AboutSection.objects.get_or_create(pk=1)
    if request.method == 'POST':
        for f in ['title_en','title_km','body_en','body_km','years_label_en','years_label_km','years_number']:
            setattr(obj, f, request.POST.get(f, getattr(obj, f)))
        if 'image' in request.FILES:
            obj.image = request.FILES['image']
        obj.save()
        messages.success(request, 'About section saved!')
        return redirect('admin_about')
    return render(request, 'admin_panel/about.html', {'obj': obj})

# ── FACILITIES ────────────────────────────────────────────────
@login_required
def admin_facilities(request):
    items = Facility.objects.all()
    return render(request, 'admin_panel/facilities.html', {'items': items})

@login_required
def admin_facility_save(request, pk=None):
    obj = get_object_or_404(Facility, pk=pk) if pk else Facility()
    if request.method == 'POST':
        obj.title_en = request.POST.get('title_en','')
        obj.title_km = request.POST.get('title_km','')
        obj.description_en = request.POST.get('description_en','')
        obj.description_km = request.POST.get('description_km','')
        obj.order = request.POST.get('order', 0)
        obj.is_active = 'is_active' in request.POST
        if 'image' in request.FILES:
            obj.image = request.FILES['image']
        obj.save()
        messages.success(request, 'Facility saved!')
    return redirect('admin_facilities')

@login_required
def admin_facility_delete(request, pk):
    get_object_or_404(Facility, pk=pk).delete()
    messages.success(request, 'Facility deleted!')
    return redirect('admin_facilities')

# ── OFFERS ────────────────────────────────────────────────────
@login_required
def admin_offers(request):
    items = Offer.objects.all()
    return render(request, 'admin_panel/offers.html', {'items': items})

@login_required
def admin_offer_save(request, pk=None):
    obj = get_object_or_404(Offer, pk=pk) if pk else Offer()
    if request.method == 'POST':
        obj.title_en = request.POST.get('title_en','')
        obj.title_km = request.POST.get('title_km','')
        obj.description_en = request.POST.get('description_en','')
        obj.description_km = request.POST.get('description_km','')
        obj.icon = request.POST.get('icon','🎓')
        obj.order = request.POST.get('order', 0)
        obj.is_active = 'is_active' in request.POST
        if 'image' in request.FILES:
            obj.image = request.FILES['image']
        obj.save()
        messages.success(request, 'Offer saved!')
    return redirect('admin_offers')

@login_required
def admin_offer_delete(request, pk):
    get_object_or_404(Offer, pk=pk).delete()
    messages.success(request, 'Offer deleted!')
    return redirect('admin_offers')

# ── GALLERY ───────────────────────────────────────────────────
@login_required
def admin_gallery(request):
    items = GalleryItem.objects.all()
    return render(request, 'admin_panel/gallery.html', {'items': items})

@login_required
def admin_gallery_save(request, pk=None):
    obj = get_object_or_404(GalleryItem, pk=pk) if pk else GalleryItem()
    if request.method == 'POST':
        obj.title_en = request.POST.get('title_en','')
        obj.title_km = request.POST.get('title_km','')
        obj.description_en = request.POST.get('description_en','')
        obj.description_km = request.POST.get('description_km','')
        obj.category = request.POST.get('category','events')
        obj.order = request.POST.get('order', 0)
        obj.is_featured = 'is_featured' in request.POST
        if 'image' in request.FILES:
            obj.image = request.FILES['image']
        elif not pk:
            messages.error(request, 'Image is required!')
            return redirect('admin_gallery')
        obj.save()
        messages.success(request, 'Gallery item saved!')
    return redirect('admin_gallery')

@login_required
def admin_gallery_delete(request, pk):
    get_object_or_404(GalleryItem, pk=pk).delete()
    messages.success(request, 'Gallery item deleted!')
    return redirect('admin_gallery')

# ── APPLICATIONS ──────────────────────────────────────────────
@login_required
def admin_applications(request):
    status_filter = request.GET.get('status','')
    apps = Application.objects.all()
    if status_filter:
        apps = apps.filter(status=status_filter)
    return render(request, 'admin_panel/applications.html', {'apps': apps, 'status_filter': status_filter})

@login_required
def admin_application_detail(request, pk):
    app = get_object_or_404(Application, pk=pk)
    if request.method == 'POST':
        app.status = request.POST.get('status', app.status)
        app.admin_notes = request.POST.get('admin_notes', app.admin_notes)
        app.save()
        messages.success(request, 'Application updated!')
        return redirect('admin_application_detail', pk=pk)
    return render(request, 'admin_panel/application_detail.html', {'app': app})

# ── LOCATION ──────────────────────────────────────────────────
@login_required
def admin_location(request):
    obj, _ = LocationSection.objects.get_or_create(pk=1)
    if request.method == 'POST':
        for f in ['title_en','title_km','address_en','address_km','google_map_embed','open_map_url','hours_en','hours_km']:
            setattr(obj, f, request.POST.get(f, getattr(obj, f)))
        obj.save()
        messages.success(request, 'Location saved!')
        return redirect('admin_location')
    return render(request, 'admin_panel/location.html', {'obj': obj})

# ── CONTACT ───────────────────────────────────────────────────
@login_required
def admin_contact(request):
    obj, _ = ContactSection.objects.get_or_create(pk=1)
    if request.method == 'POST':
        for f in ['title_en','title_km','phone','email','address_en','address_km',
                  'hours_en','hours_km','admission_info_en','admission_info_km']:
            setattr(obj, f, request.POST.get(f, getattr(obj, f)))
        obj.save()
        messages.success(request, 'Contact section saved!')
        return redirect('admin_contact')
    msgs = ContactMessage.objects.all()
    return render(request, 'admin_panel/contact.html', {'obj': obj, 'messages_list': msgs})

@login_required
def admin_message_read(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    msg.is_read = True
    msg.save()
    return redirect('admin_contact')

@login_required
def admin_message_delete(request, pk):
    get_object_or_404(ContactMessage, pk=pk).delete()
    return redirect('admin_contact')
