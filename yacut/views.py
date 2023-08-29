import random
import string

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import LinkForm
from .models import URLMap


def get_unique_short_id(size=6, chars=string.ascii_lowercase + string.digits):
    random_link = ''.join(random.choice(chars) for _ in range(size))
    while URLMap.query.filter_by(short=random_link).first() is not None:
        random_link = ''.join(random.choice(chars) for _ in range(size))
    return random_link


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = LinkForm()

    if form.validate_on_submit():
        short_link = form.custom_id.data

        if not short_link:
            short_link = get_unique_short_id()

        if URLMap.query.filter_by(short=short_link).first() is not None:
            flash(f'Имя {short_link} уже занято!', 'warning')
            return render_template('index.html', form=form)

        urlmap = URLMap(
            original=form.original_link.data,
            short=short_link
        )
        db.session.add(urlmap)
        db.session.commit()
        flash('Ваша ссылка готова: ', 'success')
        return render_template(
            'index.html', form=form,
            result_url=url_for('index_view', _external=True) + urlmap.short
        )

    return render_template('index.html', form=form)


@app.route('/<short_id>', methods=['GET'])
def redirect_to_long_link(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap:
        return redirect(urlmap.original)
    abort(404)
