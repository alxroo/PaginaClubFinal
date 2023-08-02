from flask_wtf import FlaskForm
from wtforms.fields import SubmitField,TextAreaField,StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileAllowed,FileField


class NoticeForm(FlaskForm):
    title = StringField('Titulo',validators=[InputRequired("falta el titulo")])
    body = TextAreaField('Contenido',validators=[InputRequired("falta el contenido")])
    img = FileField('Logo',validators=[FileAllowed(['jpg','png'],'Solo se permiten imagenes')]) 
    submit = SubmitField('Publicar')