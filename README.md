# 🏫 School Website — Full Stack (Django + Admin Panel)

## 🚀 Quick Start

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Run Migrations
```bash
python manage.py migrate
```

### 3. Create Admin User
```bash
python manage.py createsuperuser
```
Or use the default: **username:** `admin` **password:** `admin123`

### 4. Start the Server
```bash
python manage.py runserver
```

### 5. Open in Browser
- 🌐 **Website:** http://127.0.0.1:8000/
- 🔐 **Admin Panel:** http://127.0.0.1:8000/admin-panel/
- Login: `admin` / `admin123`

---

## 📁 Project Structure
```
school_portal/       ← Django settings & URLs
core/
  models.py          ← All database models
  views.py           ← All views (frontend + admin)
  templates/
    core/home.html   ← Main website frontend
    admin_panel/     ← Admin dashboard templates
media/               ← Uploaded images (auto-created)
static/              ← CSS/JS files
db.sqlite3           ← Database (auto-created)
```

## 🌐 Deploying Online

### Option 1: Railway.app (Recommended — Free)
1. Push to GitHub
2. Connect to Railway.app
3. Add environment variable: `SECRET_KEY=your-secret-key`
4. Set `DEBUG=False` in settings.py for production
5. Run: `python manage.py collectstatic`

### Option 2: Render.com (Free)
1. Push to GitHub
2. Create Web Service on Render
3. Build command: `pip install -r requirements.txt && python manage.py migrate`
4. Start command: `gunicorn school_portal.wsgi`

### Option 3: PythonAnywhere (Free)
1. Upload files to PythonAnywhere
2. Set up virtualenv & install requirements
3. Configure WSGI file

## 🔑 Admin Panel Features
- ⚙️ **Header & Logo** — Change school name, logo, tagline
- 🖼️ **Hero Section** — Edit banner, title, stats, buttons
- 📖 **About Section** — Edit about text and image
- 🏫 **Facilities** — Add/edit/delete facility cards with images
- ✨ **Offers** — Add/edit/delete what the school offers
- 📷 **Gallery** — Upload and manage gallery photos
- 📝 **Applications** — View and manage student applications
- 📍 **Location** — Edit address and Google Maps embed
- 📞 **Contact** — Edit contact info and admissions text
- 💬 **Messages** — View contact form submissions

## 🌍 Language Support
- English ↔ Khmer switch button in navigation
- All content editable in both languages from admin panel
- Khmer font (Hanuman) loaded automatically

## ⚠️ Production Checklist
- [ ] Change `SECRET_KEY` in settings.py
- [ ] Set `DEBUG = False`
- [ ] Set `ALLOWED_HOSTS = ['yourdomain.com']`
- [ ] Change admin password from `admin123`
- [ ] Run `python manage.py collectstatic`
- [ ] Use PostgreSQL instead of SQLite for production
