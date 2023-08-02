from . import main
from flask import render_template,request

from ..models import  Notice,Fixture,Blog,Positions

@main.route('/',methods=['GET','POST'])
@main.route('/index',methods=['GET','POST'])
def index():
    notices = Notice.query.order_by(Notice.timestamp.desc()).limit(5).all()
    proxPartido = Fixture.query.order_by((Fixture.fecha_hora).desc()).first()
    partidos = Fixture.query.order_by((Fixture.fecha_hora).asc()).limit(3).all()
    blogs = Blog.query.order_by(Blog.timestamp.desc()).limit(2).all()
    min=len(notices)
    print("///////////******************--------------------------")
    return render_template("index.html",notices=notices,min=min,partidos=partidos,proxPartido=proxPartido,blogs=blogs)

@main.route('/noticias')
def noticias():
    cantidad=5
    page = request.args.get('page',type=int)
    pagination = Notice.query.order_by(Notice.timestamp.desc()).paginate(page=page, per_page=cantidad,error_out=False)
    notices = pagination.items
    return render_template('notices.html', notices=notices,pagination=pagination)

@main.route('/noticia/<int:id>',methods=['GET','POST'])
def noticia(id):
    notice = Notice.query.get_or_404(id)
    return render_template('notice.html',notice=notice)

@main.route('/nosotros')
def nosotros():
    return render_template("us.html")

@main.route('/fixture')
def fixture():
    partidos = Fixture.query.order_by((Fixture.fecha_hora).asc()).all()
    tabla = Positions.query.order_by((Positions.puntos).desc(),(Positions.df).desc()).all()
    return render_template("fixture.html",partidos=partidos,tabla=tabla)

@main.route('/academia')
def academia():
    return render_template("academy.html")

@main.route('/contacto')
def contacto():
    return render_template("contact.html")

@main.route('/blog')
def blog():
    cantidad=5
    page = request.args.get('page',type=int)
    pagination = Blog.query.order_by(Blog.timestamp.desc()).paginate(page=page, per_page=cantidad,error_out=False)
    blogs = pagination.items
    return render_template('blog.html', blogs=blogs,pagination=pagination)


@main.route('/blogonly/<int:id>',methods=['GET','POST'])
def blogonly(id):
    blog = Blog.query.get_or_404(id)
    return render_template('blogonly.html',blog=blog)