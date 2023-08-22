from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is not None:
        return jsonify(urlmap.to_dict_only_url()), 200
    raise InvalidAPIUsage('Указанный id не найден', 404)


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    data = request.get_json()
    if len(data) == 0:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    if 'custom_id' not in data:
        data['custom_id'] = get_unique_short_id()
    if (
        6 > len(data['custom_id']) > 16 or
        data['custom_id'].isalnum() is False
    ):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

    if URLMap.query.filter_by(
        short=data['custom_id']
    ).first() is not None:
        raise InvalidAPIUsage('Такая короткая ссылка уже существует')

    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(urlmap.to_dict()), 201
