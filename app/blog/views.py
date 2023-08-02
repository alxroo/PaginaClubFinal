from . import blog
from flask import render_template,request,redirect,url_for,send_from_directory,flash
from flask_login import current_user,login_required
from werkzeug.utils import secure_filename
import os

from .forms import BlogForm
from .. import db
from ..functions import allowed_file,getFolder
from ..models import Blog


@blog.route('/dashBlog/addBlog',methods=['GET','POST'])
@login_required
def addBlog():
    formBlog = BlogForm()
    # Crear Blog
    if request.method == 'POST' and formBlog.validate_on_submit():
        titulo = formBlog.title.data
        contenido = formBlog.body.data
        autor = current_user._get_current_object()

        if "img_blog" not in request.files:
            # return "El formulario no tiene parte del archivo"
            flash("El formulario no tiene parte del archivo",'error')
            return redirect(url_for('blog.addBlog'))
        f = request.files["img_blog"]
        if f.filename == f.filename == "":
            # return "Ningun archivo seleccionado"
            flash("Ningun archivo seleccionado",'warning')
            image_name = None
        if f and allowed_file(f.filename):
            image_name = secure_filename(f.filename)
            f.save(os.path.join(getFolder(),image_name))

        post = Blog(title=titulo, body= contenido, author=autor,img_blog=image_name)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.addBlog'))
    
    return render_template('AddBlogDash.html',form=formBlog)

@blog.route("/dashBlog/get_imgBlog/<filename>")
def get_imgBlog(filename):
    return send_from_directory(getFolder(),filename)

@blog.route('/dashBlog/seeBlog',methods=['GET','POST'])
@login_required
def seeBlog():
    cantidad=5
    page = request.args.get('page',type=int)
    pagination = Blog.query.order_by(Blog.timestamp.desc()).paginate(page=page, per_page=cantidad,error_out=False)
    items = pagination.items

    return render_template('SeeBlogsDash.html',items=items,pagination=pagination)

@blog.route('/dashBlog/editBlog/<int:id>',methods=['GET','POST'])
@login_required
def editBlog(id):
    blogitem = Blog.query.get_or_404(id)
    form = BlogForm()
    if form.validate_on_submit():
        blogitem.title = form.title.data
        blogitem.body = form.body.data
        if "img_blog" not in request.files:
            return "El formulario no tiene parte del archivo"
        f = request.files["img_blog"]
        if f and allowed_file(f.filename):
            image_name = secure_filename(f.filename)
            f.save(os.path.join(getFolder(),image_name))
            blogitem.img_blog = image_name
        db.session.add(blogitem)
        db.session.commit()
        print('El blog se ha actualizado')
        return redirect(url_for('blog.seeBlog',id=blogitem.id))
    form.title.data = blogitem.title
    form.body.data = blogitem.body
    return render_template('AddBlogDash.html',form=form)

@blog.route('/dashBlog/deleteBlog/<id>')
@login_required
def deleteBlog(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('blog.seeBlog'))