from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileField
from wtforms.fields import SubmitField,StringField,EmailField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    userName = StringField('Usuario',validators=[InputRequired()])
    name = StringField('Nombre',validators=[InputRequired()])
    email = EmailField('Email:',validators=[InputRequired()])
    img = FileField('Imagen de Perfil',validators=[FileAllowed(['jpg','png'],'Solo se permiten imagenes')]) 
    submit = SubmitField('Guardar')