from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is not None:
        return jsonify(urlmap.to_dict()), 200
    raise InvalidAPIUsage('Такой ссылки не существует', 404)


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    data = request.get_json()
    if 'original_link' not in data or 'short_link' not in data:
        raise InvalidAPIUsage('В запросе отсутствуют обязательные поля')

    if URLMap.query.filter_by(
        short_link=data['short_link']
    ).first() is not None:
        raise InvalidAPIUsage('Такая короткая ссылка уже существует')

    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(urlmap.to_dict()), 201
