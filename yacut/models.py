from datetime import datetime

from . import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_link = db.Column(db.String, nullable=False)
    short_link = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            id=self.id,
            original_link=self.original_link,
            short_link=self.short_link,
            timestamp=self.timestamp
        )

    def from_dict(self, data):
        for field in ['original_link', 'short_link']:
            if field in data:
                setattr(self, field, data[field])
