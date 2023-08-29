from datetime import datetime

from . import db
from .constants import DOMAIN_PART


API_TO_MODEL = {
    'url': 'original',
    'custom_id': 'short'
}


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=DOMAIN_PART + self.short
        )

    def to_dict_only_url(self):
        return dict(
            url=self.original
        )

    def from_dict(self, data):
        for field in API_TO_MODEL.keys():
            if field in data:
                setattr(self, API_TO_MODEL[field], data[field])
