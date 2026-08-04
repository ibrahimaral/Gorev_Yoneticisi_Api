#  Mini Task Manager API

Django REST Framework (DRF) kullanılarak geliştirilmiş, tam kapsamlı (CRUD) bir Görev Yönetim Sistemi API'si. Bu proje, projeler oluşturmaya ve bu projelerin altına belirli durumlara (TODO, IN_PROGRESS, DONE) sahip görevler atamaya olanak tanır.

Güvenlik için **JWT (JSON Web Tokens)** kullanılmış olup, büyük verileri yönetebilmek adına **Sayfalama (Pagination)** ve **Filtreleme** mantığı entegre edilmiştir.

##  Özellikler

*   **Güvenli Kimlik Doğrulama:** JWT (SimpleJWT) tabanlı yetkilendirme altyapısı.
*   **Tam CRUD Operasyonları:** Projeler ve Görevler için eksiksiz Create, Read, Update, Delete uç noktaları.
*   **İş Mantığı (Business Logic):**
    *   Görev durumuna göre filtreleme yeteneği (`?status=TODO`).
    *   Performans optimizasyonu için veri sayfalama (Her sayfada 5 görev).
*   **İlişkisel Veritabanı:** Projeler ve Görevler arasında `ForeignKey` ilişkisi (One-to-Many).
*   **Unit Tests:** Uç noktaların (endpoints) ve veritabanı işlemlerinin doğruluğunu kanıtlayan %100 başarılı birim testleri (Unit Tests).

---

##  Kullanılan Teknolojiler

*   **Backend:** Python 3, Django, Django REST Framework (DRF)
*   **Güvenlik:** djangorestframework-simplejwt
*   **Veritabanı:** SQLite (Geliştirme ortamı için)

---

##  Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

**1. Repoyu Klonlayın:**
```bash
git clone https://github.com/ibrahimaral/Mini_Gorev_Yoneticisi.git
cd mini_task_manager
```
**2. Sanal Ortam (Virtual Environment) Oluşturun ve Aktif Edin:**

python -m venv venv
# Windows için:
```bash
venv\Scripts\activate
```
# macOS/Linux için:
```bash
source venv/bin/activate
```

**3. Gerekli Paketleri Yükleyin:**
```bash
pip install django djangorestframework djangorestframework-simplejwt
```

**4. Veritabanı Geçişlerini (Migrations) Uygulayın:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Yönetici (Superuser) Hesabı Oluşturun:**
```bash
python manage.py createsuperuser
```

**6. Geliştirme Sunucusunu Başlatın:**
```bash
python manage.py runserver
```

# 📡 API Uç Noktaları (Endpoints)

Not: Tüm API istekleri, Authorization: Bearer <token> başlığı (header) gerektirir.


* **Kimlik Doğrulama**

POST /api/token/ - Yeni bir JWT Access ve Refresh token alır.

POST /api/token/refresh/ - Süresi dolan token'ı yeniler.


* **Projeler (Projects)**

GET /api/projects/ - Tüm projeleri listeler.

POST /api/projects/ - Yeni proje oluşturur.


* **Görevler (Tasks)**

GET /api/projects/{id}/tasks/ - Belirli bir projenin görevlerini listeler.

*Filtreleme:* /api/projects/{id}/tasks/?status=TODO

*Sayfalama:* /api/projects/{id}/tasks/?page=2


POST /api/projects/{id}/tasks/ - Belirli bir projeye yeni görev ekler.

PATCH /api/tasks/{id}/ - Görevin belirli alanlarını günceller (Örn: Sadece status).

DELETE /api/tasks/{id}/ - Görevi siler.

# **Testleri Çalıştırma**
```bash
python manage.py test
```

