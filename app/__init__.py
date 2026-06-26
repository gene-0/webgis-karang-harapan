from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_mail import Mail  # Tambahkan import ini

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()  # Tambahkan objek global mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)  # Daftarkan mail ke context aplikasi Flask
    
    login_manager.login_view = 'admin.login'

    from app.routes.public import public_bp
    from app.routes.admin import admin_bp
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app