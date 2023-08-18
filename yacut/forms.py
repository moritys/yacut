# original_link — поле для оригинальной длинной ссылки,
# custom_id — поле для пользовательского варианта короткого идентификатора.

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional


class LinkForm(FlaskForm):
    original_link = StringField(
        'Вставьте оригинальную ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(1, 300)
        ]
    )
    custom_id = StringField(
        'Укажите короткую ссылку (необязательно)',
        validators=[
            Length(6, 6),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
