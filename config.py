import os

class Config:
    SECRET_KEY = 'ganti-dengan-random-string-panjang'
    
    # Database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/webgis_karang_harapan'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload foto (Setelan Asli Anda Tetap Dipertahankan)
    UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024  # Maks 2MB per foto
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

    # ─── KONFIGURASI SMTP GMAIL GRATIS ───
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'wibowoprawiro4@gmail.com' 
    
    # Tempel 16 digit kode dari Google di bawah ini (TANPA SPASI)
    MAIL_PASSWORD = 'xopwtlevfbekyhtj'  
    
    MAIL_DEFAULT_SENDER = ('WebGIS Kelurahan (Demo)', 'wibowoprawiro4@gmail.com')