from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    id           = db.Column(db.Integer, primary_key=True)
    username     = db.Column(db.String(50), unique=True, nullable=False)
    password     = db.Column(db.String(255), nullable=False)
    
    # ─── KOLOM BARU UNTUK FITUR LUPA PASSWORD VIA EMAIL ───
    email        = db.Column(db.String(100), unique=True, nullable=True)
    reset_token  = db.Column(db.String(100), nullable=True)
    token_expiry = db.Column(db.DateTime, nullable=True)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


class Kategori(db.Model):
    __tablename__ = 'kategori'
    id             = db.Column(db.Integer, primary_key=True)
    nama_kategori  = db.Column(db.String(100), nullable=False)
    icon           = db.Column(db.String(50))
    warna          = db.Column(db.String(20))
    
    lokasi         = db.relationship('Lokasi', backref='kategori', lazy=True)
    
    created_at     = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at     = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Lokasi(db.Model):
    __tablename__ = 'lokasi'
    id           = db.Column(db.Integer, primary_key=True)
    nama         = db.Column(db.String(150), nullable=False)
    kategori_id  = db.Column(db.Integer, db.ForeignKey('kategori.id'), nullable=False)
    deskripsi    = db.Column(db.Text)
    alamat       = db.Column(db.Text)
    latitude     = db.Column(db.Float, nullable=False)
    longitude    = db.Column(db.Float, nullable=False)
    foto         = db.Column(db.Text)
    kontak       = db.Column(db.String(20))
    
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at   = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# ─── MODEL BERDASARKAN DATABASE SQL ASLI ANDA ──────────────────────
class ActivityLog(db.Model):
    __tablename__ = 'activity_logs'  # Sesuai dengan nama tabel MySQL Anda
    
    id          = db.Column(db.Integer, primary_key=True)
    user_id     = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=True)  # FK ke tabel admin
    aksi        = db.Column(db.String(50), nullable=False)
    deskripsi   = db.Column(db.Text, nullable=False)
    created_at  = db.Column(db.DateTime, default=datetime.utcnow)

    # Menghubungkan log secara dinamis dengan objek Admin penggunanya
    admin_rel   = db.relationship('Admin', backref=db.backref('logs', lazy=True))

    def __repr__(self):
        return f'<ActivityLog {self.aksi}>'