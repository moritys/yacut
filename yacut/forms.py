# original_link — поле для оригинальной длинной ссылки,
# custom_id — поле для пользовательского варианта короткого идентификатора.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional
from wtforms_validators import AlphaNumeric


class LinkForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 300)
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки (необязательно)',
        validators=[
            Length(5, 16),
            AlphaNumeric(
                message='Ссылка может содержать только буквы и цифры'
            ),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
