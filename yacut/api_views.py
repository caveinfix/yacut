import re

from flask import jsonify, request

from yacut.utils import get_unique_short_id

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route("/api/id/<string:short_url>/", methods=["GET"])
def get_url(short_url):
    short_url = URLMap.query.filter_by(short=short_url).first()
    if short_url is None:
        raise InvalidAPIUsage("Указанный id не найден", 404)
    return jsonify(url=short_url.original), 200


@app.route("/api/id/", methods=["POST"])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage("Отсутствует тело запроса")
    if "url" not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    short_id = data.get("custom_id")
    if not short_id:
        data["custom_id"] = get_unique_short_id()
    if not re.match(r"^[a-zA-Z0-9]{1,16}$", data["custom_id"]):
        raise InvalidAPIUsage("Указано недопустимое имя для короткой ссылки")
    if URLMap.query.filter_by(short=short_id).first():
        raise InvalidAPIUsage(f'Имя "{short_id}" уже занято.')
    add_url = URLMap()
    add_url.from_dict(data)
    db.session.add(add_url)
    db.session.commit()
    return jsonify(add_url.to_dict()), 201
