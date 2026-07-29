# Mini Görev Yöneticisi (REST API)

Bu proje, temel RESTful mimari standartlarına uygun olarak geliştirilmiş bir arka uç (backend) servisidir. Kullanıcıların projeler oluşturabildiği ve bu projelere bağlı görevlerin (task) durumlarını takip edebildiği bir sistem sunar.

## Teknik Detaylar
- **Dil/Framework:** Python, Django, Django Rest Framework
- **Veritabanı:** SQLite
- **Kimlik Doğrulama:** JWT (JSON Web Token)
- **Dokümantasyon:** Swagger (OpenAPI)

## QUICK START

Projeyi yerel bilgisayarınızda ayağa kaldırmak için aşağıdaki adımları sırasıyla izleyin:

1. **Repoyu Klonlayın:**
   ```bash
   git clone [https://github.com/ibrahimaral/Gorev_Yoneticisi_Api.git](https://github.com/ibrahimaral/Gorev_Yoneticisi_Api.git)
   cd Gorev_Yoneticisi_Api
   ```

2. **Sanal Ortamı Oluşturun ve Aktif Edin:**
   
   ```bash
    python -m venv venv
    .\venv\Scripts\activate
   ```

3. **Gerekli Paketleri Yükleyin:**
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Veritabanını Hazırlayın:**
   
   ```bash
   python manage.py migrate
   ```

5. **Sunucuyu Başlatın:**
   
   ```bash
   python manage.py runserver
   ```

*Not: API uç noktalarını incelemek ve test etmek için sunucuyu başlattıktan sonra tarayıcınızda http://127.0.0.1:8000/swagger/ adresine gidebilirsiniz.



