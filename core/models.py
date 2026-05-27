from django.db import models

class SiteSettings(models.Model):
    school_name_en = models.CharField(max_length=200, default="Apex Nursing College")
    school_name_km = models.CharField(max_length=200, default="មហាវិទ្យាល័យ Apex")
    tagline_en = models.CharField(max_length=300, default="Accredited · Est. 2001")
    tagline_km = models.CharField(max_length=300, default="ទទួលស្គាល់ · ២០០១")
    logo = models.ImageField(upload_to='site/', blank=True, null=True)
    phone = models.CharField(max_length=50, default="(325) 942-0000")
    email = models.EmailField(default="admissions@school.edu")
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Site Settings"
    def __str__(self):
        return "Site Settings"

class HeroSection(models.Model):
    title_en = models.CharField(max_length=300, default="Train to Heal. Lead to Care.")
    title_km = models.CharField(max_length=300, default="រៀនព្យាបាល។ នាំការថែទាំ។")
    subtitle_en = models.TextField(default="We prepare compassionate, skilled nurses.")
    subtitle_km = models.TextField(default="យើងបណ្តុះបណ្តាលគិលានុបដ្ឋាក។")
    badge_en = models.CharField(max_length=200, default="ACEN Accredited · Est. 2001")
    badge_km = models.CharField(max_length=200, default="ទទួលស្គាល់ ACEN · ២០០១")
    btn1_en = models.CharField(max_length=100, default="Apply Now")
    btn1_km = models.CharField(max_length=100, default="ដាក់ពាក្យឥឡូវ")
    btn2_en = models.CharField(max_length=100, default="Contact Admissions")
    btn2_km = models.CharField(max_length=100, default="ទំនាក់ទំនង")
    background_image = models.ImageField(upload_to='hero/', blank=True, null=True)
    stat1_num = models.CharField(max_length=20, default="98%")
    stat1_label_en = models.CharField(max_length=100, default="NCLEX Pass Rate")
    stat1_label_km = models.CharField(max_length=100, default="អត្រាប្រឡងជាប់")
    stat2_num = models.CharField(max_length=20, default="2,400+")
    stat2_label_en = models.CharField(max_length=100, default="Graduates")
    stat2_label_km = models.CharField(max_length=100, default="អ្នកបញ្ចប់")
    stat3_num = models.CharField(max_length=20, default="45+")
    stat3_label_en = models.CharField(max_length=100, default="Clinical Partners")
    stat3_label_km = models.CharField(max_length=100, default="ដៃគូ")
    stat4_num = models.CharField(max_length=20, default="94%")
    stat4_label_en = models.CharField(max_length=100, default="Employment Rate")
    stat4_label_km = models.CharField(max_length=100, default="អត្រាការងារ")
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Hero Section"

class AboutSection(models.Model):
    title_en = models.CharField(max_length=300, default="Built on Compassion & Excellence")
    title_km = models.CharField(max_length=300, default="បង្កើតឡើងលើចិត្តអាណិត")
    body_en = models.TextField(default="Since 2001, we have been the region's most trusted nursing school.")
    body_km = models.TextField(default="តាំងពីឆ្នាំ ២០០១ យើងជាសាលាដែលទុកចិត្តបានបំផុត។")
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    years_label_en = models.CharField(max_length=100, default="Years of Excellence")
    years_label_km = models.CharField(max_length=100, default="ឆ្នាំនៃភាពល្អឥតខ្ចោះ")
    years_number = models.CharField(max_length=10, default="23rd")
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "About Section"

class Facility(models.Model):
    title_en = models.CharField(max_length=200)
    title_km = models.CharField(max_length=200)
    description_en = models.TextField()
    description_km = models.TextField()
    image = models.ImageField(upload_to='facilities/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.title_en

class Offer(models.Model):
    title_en = models.CharField(max_length=200)
    title_km = models.CharField(max_length=200)
    description_en = models.TextField()
    description_km = models.TextField()
    image = models.ImageField(upload_to='offers/', blank=True, null=True)
    icon = models.CharField(max_length=10, default="🎓")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    class Meta:
        ordering = ['order']
    def __str__(self):
        return self.title_en

class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('events','Events'),('students','Students'),('facilities','Facilities'),
        ('sports','Sports'),('ceremonies','Ceremonies'),('classroom','Classroom'),
    ]
    title_en = models.CharField(max_length=200)
    title_km = models.CharField(max_length=200, blank=True)
    description_en = models.CharField(max_length=300, blank=True)
    description_km = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='events')
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['order', '-created_at']
    def __str__(self):
        return self.title_en

class Application(models.Model):
    STATUS_CHOICES = [('new','New'),('reviewed','Reviewed'),('accepted','Accepted'),('rejected','Rejected')]
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=20)
    grade_applying = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    address = models.TextField()
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    submitted_at = models.DateTimeField(auto_now_add=True)
    admin_notes = models.TextField(blank=True)
    class Meta:
        ordering = ['-submitted_at']
    def __str__(self):
        return f"{self.full_name} — {self.submitted_at.strftime('%Y-%m-%d')}"

class LocationSection(models.Model):
    title_en = models.CharField(max_length=200, default="Visit Our Campus")
    title_km = models.CharField(max_length=200, default="ចូលទស្សនាសាលា")
    address_en = models.TextField(default="2400 W. Avenue N, San Angelo, TX 76904")
    address_km = models.TextField(default="San Angelo, TX")
    google_map_embed = models.TextField(blank=True)
    open_map_url = models.URLField(blank=True, default="https://maps.google.com")
    hours_en = models.CharField(max_length=200, default="Mon–Fri 8AM–6PM · Sat 9AM–1PM")
    hours_km = models.CharField(max_length=200, default="ចន្ទ–សុក្រ ៨ព្រឹក–៦ល្ងាច")
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Location Section"

class ContactSection(models.Model):
    title_en = models.CharField(max_length=200, default="Get In Touch")
    title_km = models.CharField(max_length=200, default="ទំនាក់ទំនងយើង")
    phone = models.CharField(max_length=50, default="(325) 942-0000")
    email = models.EmailField(default="admissions@school.edu")
    address_en = models.TextField(default="2400 W. Avenue N, San Angelo, TX 76904")
    address_km = models.TextField(default="San Angelo, TX")
    hours_en = models.CharField(max_length=200, default="Mon–Fri 8AM–6PM")
    hours_km = models.CharField(max_length=200, default="ចន្ទ–សុក្រ ៨ព្រឹក–៦ល្ងាច")
    admission_info_en = models.TextField(default="Applications are reviewed on a rolling basis.")
    admission_info_km = models.TextField(default="ពាក្យស្នើសុំត្រូវបានពិនិត្យជានិច្ច។")
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Contact Section"

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-submitted_at']
    def __str__(self):
        return f"{self.name} — {self.subject}"
