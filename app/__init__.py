from flask import Flask
from .config import config

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from .carpeta import carpeta as carpeta_blueprint
    app.register_blueprint(carpeta_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    from .notices import notices as notices_blueprint
    app.register_blueprint(notices_blueprint)

    from .fixture import fixture as fixture_blueprint
    app.register_blueprint(fixture_blueprint)

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    with app.app_context():
        db.create_all()

    return app