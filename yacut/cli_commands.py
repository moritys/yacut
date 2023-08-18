import csv

import click

from . import app, db
from .models import URLMap


@app.cli.command('load_links')
def load_links_command():
    """Функция загрузки ссылок в базу данных."""
    with open('links.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        counter = 0
        for row in reader:
            link = URLMap(**row)
            db.session.add(link)
            db.session.commit()
            counter += 1
    click.echo(f'Загружено ссылок: {counter}')
