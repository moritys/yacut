from flask import jsonify, request
from string import ascii_lowercase, digits

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id


ALLOWED_SYMBOLS = ascii_lowercase + digits

def check_correct_link(link):
    if len(link) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    for letter in link:
        if letter not in ALLOWED_SYMBOLS:
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    return link


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is not None:
        return jsonify(urlmap.to_dict_only_url()), 200
    raise InvalidAPIUsage('Указанный id не найден', 404)


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    if (
        'custom_id' not in data or
        data['custom_id'] == ''  or
        data['custom_id'] is None
    ):
        data['custom_id'] = get_unique_short_id()
    check_correct_link(data['custom_id'])

    if URLMap.query.filter_by(
        short=data['custom_id']
    ).first() is not None:
        name = data['custom_id']
        raise InvalidAPIUsage(f'Имя "{name}" уже занято.')

    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(urlmap.to_dict()), 201
