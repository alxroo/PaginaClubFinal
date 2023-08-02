from . import notices
from flask import render_template,request,redirect,url_for,send_from_directory,flash
from flask_login import current_user,login_required
from werkzeug.utils import secure_filename
import os

from .forms import NoticeForm
from .. import db
from ..functions import allowed_file,getFolder
from ..models import Notice


@notices.route('/dashNotice/addNotice',methods=['GET','POST'])
@login_required
def addNotice():
    formNotice = NoticeForm()

    if request.method == 'POST' and formNotice.validate_on_submit():
        titulo = formNotice.title.data
        contenido = formNotice.body.data
        autor = current_user._get_current_object()

        if "img" not in request.files:
            flash("El formulario no tiene parte del archivo",'error')
            return redirect(url_for('notices.addNotice'))
        f = request.files["img"]
        if f.filename == f.filename == "":
            flash("Ningun archivo seleccionado",'warning')
            image_name = None
        if f and allowed_file(f.filename):
            image_name = secure_filename(f.filename)
            f.save(os.path.join(getFolder(),image_name))

        notice = Notice(title=titulo, body= contenido, author=autor,img=image_name)
        db.session.add(notice)
        db.session.commit()
        return redirect(url_for('notices.addNotice'))
    
    return render_template('AddNoticeDash.html',form=formNotice)

@notices.route("/dashNotice/get_img/<filename>")
def get_img(filename):
    return send_from_directory(getFolder(),filename)

@notices.route('/dashNotice/seeNotice',methods=['GET','POST'])
@login_required
def seeNotice():
    cantidad=5
    page = request.args.get('page',type=int)
    pagination = Notice.query.order_by(Notice.timestamp.desc()).paginate(page=page, per_page=cantidad,error_out=False)
    items = pagination.items
    return render_template('SeeNoticesDash.html',items=items,pagination=pagination)

@notices.route('/dashNotice/editNotice/<int:id>',methods=['GET','POST'])
@login_required
def editNotice(id):
    noticeitem = Notice.query.get_or_404(id)
    form = NoticeForm()
    if form.validate_on_submit():
        noticeitem.title = form.title.data
        noticeitem.body = form.body.data
        if "img" not in request.files:
            return "El formulario no tiene parte del archivo"
        f = request.files["img"]
        if f and allowed_file(f.filename):
            image_name = secure_filename(f.filename)
            f.save(os.path.join(getFolder(),image_name))
            noticeitem.img = image_name
        db.session.add(noticeitem)
        db.session.commit()
        print('El Notice se ha actualizado')
        return redirect(url_for('notices.seeNotice',id=noticeitem.id))
    form.title.data = noticeitem.title
    form.body.data = noticeitem.body
    return render_template('AddNoticeDash.html',form=form)

@notices.route('/dashNotice/deleteNotice/<id>')
@login_required
def deleteNotice(id):
    notice = Notice.query.get_or_404(id)
    db.session.delete(notice)
    db.session.commit()
    return redirect(url_for('notices.seeNotice'))