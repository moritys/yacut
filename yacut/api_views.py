from flask import jsonify, request
from http import HTTPStatus

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id
from .constants import ALLOWED_SYMBOLS, ERRORS_TEXTS, MAX_LENGHT_SHORT_LINK


def check_correct_link(link):
    if len(link) > MAX_LENGHT_SHORT_LINK:
        raise InvalidAPIUsage(ERRORS_TEXTS['wrong_short_text'])
    for letter in link:
        if letter not in ALLOWED_SYMBOLS:
            raise InvalidAPIUsage(ERRORS_TEXTS['wrong_short_text'])
    return link


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is not None:
        return jsonify(urlmap.to_dict_only_url()), HTTPStatus.OK
    raise InvalidAPIUsage(ERRORS_TEXTS['not_find_id'], HTTPStatus.NOT_FOUND)


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage(ERRORS_TEXTS['no_body'])
    if 'url' not in data:
        raise InvalidAPIUsage(ERRORS_TEXTS['no_url'])

    if (
        'custom_id' not in data or
        data['custom_id'] == '' or
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
    return jsonify(urlmap.to_dict()), HTTPStatus.CREATED
