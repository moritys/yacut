import random
import string

from flask import abort, flash, redirect, render_template

from . import app, db
from .forms import LinkForm
from .models import URLMap


def get_random_link(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = LinkForm()

    if form.validate_on_submit():
        short_link = form.custom_id.data

        if not short_link:
            short_link = get_random_link()
            exist_obj = URLMap.query.filter_by(
                short=short_link).first()
            while exist_obj is not None:
                short_link = get_random_link()

        if URLMap.query.filter_by(short=short_link).first() is not None:
            flash('Такая короткая ссылка уже существует!', 'warning')
            return render_template('get_link.html', form=form)

        urlmap = URLMap(
            original=form.original_link.data,
            short=short_link
        )
        db.session.add(urlmap)
        db.session.commit()
        flash('Ваша ссылка готова: ', 'success')
        return render_template('get_link.html', form=form, urlmap=urlmap)

    return render_template('get_link.html', form=form)


@app.route('/<string:link>/')
def redirect_to_long_link(link):
    urlmap = URLMap.query.filter_by(short=link).first()
    if not urlmap:
        abort(404)
    return redirect(urlmap.original)
