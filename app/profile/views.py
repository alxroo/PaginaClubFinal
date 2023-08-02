from . import profile
from flask import render_template,request,redirect,url_for,send_from_directory
from flask_login import current_user,login_required
from werkzeug.utils import secure_filename
import os

from .forms import UserForm
from ..functions import allowed_file,getFolder
from .. import db
from ..models import User

@profile.route('/dashProfile/profileDash')
@login_required
def profileDash():
    usuario = current_user._get_current_object()
    return render_template("dashProfile.html",usuario=usuario)


@profile.route("/dashProfile/get_img/<filename>")
def get_img(filename):
    return send_from_directory(getFolder(),filename)

@profile.route('/dashProfile/editProfile/<int:id>',methods=['GET','POST'])
@login_required
def editProfile(id):
    userProfile = User.query.get_or_404(id)
    form = UserForm()
    if form.validate_on_submit():
        userProfile.username = form.userName.data
        userProfile.name = form.name.data
        userProfile.email = form.email.data
        if "img" not in request.files:
            return "El formulario no tiene parte del archivo"
        f = request.files["img"]
        if f and allowed_file(f.filename):
            image_name = secure_filename(f.filename)
            f.save(os.path.join(getFolder(),image_name))
            userProfile.img = image_name
        db.session.add(userProfile)
        db.session.commit()
        print('Informacion de usuario actualizado')
        return redirect(url_for('profile.profileDash'))
    form.userName.data = userProfile.username
    form.name.data = userProfile.name
    form.email.data = userProfile.email
    return render_template('EditProfile.html',form=form)