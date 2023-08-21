from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, url
from wtforms_validators import AlphaNumeric


class LinkForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='* Обязательное поле'),
            Length(
                1, 400,
                message='* Превышена максимальная длина ссылки (400)'
            ),
            url(message='* Некорректная ссылка')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки (необязательно)',
        validators=[
            Length(
                5, 16,
                message='* Длина короткой ссылки должна быть от 5 до 16 символов'
            ),
            AlphaNumeric(
                message='* Ссылка может содержать только буквы и цифры'
            ),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
