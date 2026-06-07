# Foziljon Portfolio — Django Backend

## Loyiha tuzilmasi
```
django_portfolio/
├── manage.py
├── requirements.txt
├── db.sqlite3          (avtomatik yaratiladi)
├── portfolio/          (asosiy sozlamalar)
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/               (asosiy app)
│   ├── models.py       (Certificate, Message)
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   └── index.html      (frontend)
└── static/
    └── style.css
```

## O'rnatish va ishga tushirish

### 1. Virtual muhit yaratish
```bash
python -m venv venv
venv\Scripts\activate        # Windows
# yoki
source venv/bin/activate     # Mac/Linux
```

### 2. Kutubxonalarni o'rnatish
```bash
pip install -r requirements.txt
```

### 3. Ma'lumotlar bazasini tayyorlash
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Admin foydalanuvchi yaratish
```bash
python manage.py createsuperuser
# Ism, email, parol kiriting
```

### 5. Serverni ishga tushirish
```bash
python manage.py runserver
```

## Sahifalar

| URL | Tavsif |
|-----|--------|
| http://127.0.0.1:8000/ | Portfolio bosh sahifasi |
| http://127.0.0.1:8000/admin/ | Admin panel |
| http://127.0.0.1:8000/send-message/ | Contact API (POST) |
| http://127.0.0.1:8000/api/certificates/ | Sertifikatlar API (GET) |

## Admin panelda nima qilish mumkin?
- ✅ **Certificates** — yangi sertifikat qo'shish, rasm yuklash, o'chirish
- ✅ **Messages** — contact formadan kelgan xabarlarni ko'rish
