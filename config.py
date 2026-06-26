import os

class Config:
    # ─── SECRET KEY ───
    # Di Railway: set environment variable SECRET_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY', 'ganti-ini-di-env-railway')

    # ─── DATABASE ───
    # Di Railway: otomatis terisi dari plugin MySQL Railway
    # Format: mysql+pymysql://user:password@host:port/dbname
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://root:@localhost/webgis_karang_harapan'  # fallback lokal
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_recycle': 280,       # cegah koneksi timeout di Railway
        'pool_pre_ping': True,
    }

    # ─── UPLOAD FOTO ───
    # Di Railway: file disimpan sementara di /tmp (persistent storage perlu Cloudinary)
    UPLOAD_FOLDER = os.environ.get(
        'UPLOAD_FOLDER',
        os.path.join('app', 'static', 'uploads')
    )
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024   # maks 2MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

    # ─── EMAIL (SMTP Gmail) ───
    MAIL_SERVER   = 'smtp.gmail.com'
    MAIL_PORT     = 587
    MAIL_USE_TLS  = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
    MAIL_DEFAULT_SENDER = (
        'UMKM Karang Harapan',
        os.environ.get('MAIL_USERNAME', '')
    )
