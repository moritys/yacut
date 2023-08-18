# Придумайте и реализуйте в функции get_unique_short_id() алгоритм формирования коротких идентификаторов переменной длины. Логику формирования идентификатора выбирайте на своё усмотрение, мы предлагаем использовать функцию random().
# Опишите view-функцию для главной страницы и view-функцию, которая будет отвечать за переадресацию.

from random import randrange

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import LinkForm
from .models import URLMap


@app.route('/')
def index_view():
    return render_template('get_link.html')


if __name__ == '__main__':
    app.run()
