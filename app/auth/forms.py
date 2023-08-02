from flask_wtf import FlaskForm
from wtforms.fields import EmailField,SubmitField,PasswordField
from wtforms.validators import InputRequired,Length,Email


class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[
                                           InputRequired("Es necesario el email"),
                                           Length(1,64),
                                           Email("Formato email incorrecto")

    ])
    password = PasswordField('Password',validators=[InputRequired("Es necesario el password")])
    # remember_me = BooleanField('Mantenerme conectado')

    submit = SubmitField('Login')