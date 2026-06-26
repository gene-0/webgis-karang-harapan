from flask import Blueprint, render_template, jsonify, request
from app.models import Lokasi, Kategori

public_bp = Blueprint('public', __name__)

# ─── API LOKASI (untuk LeafletJS) ────────────────────
@public_bp.route('/api/lokasi')
def api_lokasi():
    kategori_id = request.args.get('kategori')

    if kategori_id:
        lokasi_list = Lokasi.query.filter_by(kategori_id=kategori_id).all()
    else:
        lokasi_list = Lokasi.query.all()

    data = []
    for l in lokasi_list:
        data.append({
            'id'            : l.id,
            'nama'          : l.nama,
            'kategori'      : l.kategori.nama_kategori,
            'kategori_id'   : l.kategori_id,
            'warna'         : l.kategori.warna,
            'icon'          : l.kategori.icon,
            'deskripsi'     : l.deskripsi,
            'alamat'        : l.alamat,
            'latitude'      : l.latitude,
            'longitude'     : l.longitude,
            'kontak'        : l.kontak,
            'foto'          : l.foto
        })

    return jsonify(data)


# ─── API STATISTIK (untuk dashboard publik) ──────────
@public_bp.route('/api/statistik')
def api_statistik():
    kategori_list = Kategori.query.all()
    data = []
    for k in kategori_list:
        data.append({
            'nama'   : k.nama_kategori,
            'jumlah' : len(k.lokasi),
            'warna'  : k.warna
        })
    return jsonify(data)

# ─── HALAMAN UTAMA / DASHBOARD PUBLIK ────────────────
@public_bp.route('/')
def index():
    kategori = Kategori.query.all()
    total_lokasi = Lokasi.query.count()
    return render_template('public/index.html',
                           kategori=kategori,
                           total_lokasi=total_lokasi)


# ─── HALAMAN PETA ─────────────────────────────────────
@public_bp.route('/peta')
def peta():
    kategori = Kategori.query.all()
    return render_template('public/peta.html', kategori=kategori)


# ─── HALAMAN DETAIL LOKASI ────────────────────────────
@public_bp.route('/lokasi/<int:id>')
def detail(id):
    lokasi = Lokasi.query.get_or_404(id)
    return render_template('public/detail.html', lokasi=lokasi)