from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash,check_password_hash
from flask import current_app
from datetime import datetime

from sqlalchemy.orm import relationship

from . import db,login_manager

ALLOWED_EXTENSIONS = set(['png','jpg','jpge','gif'])

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean,default=False)

    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    img= db.Column(db.String(100))

    notices = db.relationship('Notice',backref='author', lazy='dynamic')
    blogs = db.relationship('Blog',backref='author', lazy='dynamic')

    # Password verification --------------------------------------------
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash= generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    #Capturar tiempo-----------------------------------------------------
    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Notice(db.Model):
    __tablename__ = 'notice'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    body_html = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    img= db.Column(db.String(100))

    @staticmethod
    def generate_fake_one(count):
        from random import seed, randint
        import forgery_py

        autor = current_user._get_current_object()
        seed()
        for i in range(count):
            p = Notice(title=forgery_py.lorem_ipsum.sentence(),body=forgery_py.lorem_ipsum.sentences(randint(10,20)),timestamp=forgery_py.date.date(True))
            db.session.add(p)
            db.session.commit()

# --------------------------------------------------------------------

class Team(db.Model):
    __tablename__ = 'team'
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(100))
    logo = db.Column(db.String(100))

    def allowed_file(filename):
        return "." in filename and filename.rsplit(".",1)[1] in ALLOWED_EXTENSIONS

class Fixture(db.Model):
    __tablename__ = 'fixture'
    id = db.Column(db.Integer, primary_key=True)
    Local_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    Visita_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    Local = relationship("Team",foreign_keys=[Local_id])
    Visita = relationship("Team",foreign_keys=[Visita_id])

    fecha_hora = db.Column(db.DateTime(timezone=True))
    lugar = db.Column(db.Text())
    resLocal = db.Column(db.String(50))
    resVisita = db.Column(db.String(50))
    golLocal = db.Column(db.Integer)
    golVisita = db.Column(db.Integer)

    estado = db.Column(db.String(50))

class Positions(db.Model):
    __tablename__ = 'positions'
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(100))
    p_ganado = db.Column(db.Integer)
    p_empatado = db.Column(db.Integer)
    p_perdido = db.Column(db.Integer)
    p_jugados = db.Column(db.Integer)
    puntos = db.Column(db.Integer)
    gf = db.Column(db.Integer)
    ge = db.Column(db.Integer)
    df = db.Column(db.Integer)

    id_team = db.Column(db.Integer, db.ForeignKey('team.id'))
    tablaPosicion = relationship("Team",foreign_keys=[id_team])

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    img_blog= db.Column(db.String(100))

    @staticmethod
    def generate_fake_one(count):
        from random import seed, randint
        import forgery_py

        autor = current_user._get_current_object()
        seed()
        for i in range(count):
            p = Blog(title=forgery_py.lorem_ipsum.sentence(),body=forgery_py.lorem_ipsum.sentences(randint(10,20)))
            db.session.add(p)
            db.session.commit()

