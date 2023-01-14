from datetime import datetime

from flask import url_for

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256))
    short = db.Column(db.String(256), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for("redirect_view", custom_id=self.short, _external=True),
        )

    def from_dict(self, data):
        key_for_api = {"url": "original", "custom_id": "short"}
        for field in key_for_api:
            if field in data:
                setattr(self, key_for_api[field], data[field])
