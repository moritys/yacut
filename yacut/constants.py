from string import ascii_lowercase, digits


ALLOWED_SYMBOLS = ascii_lowercase + digits
MAX_LENGHT_SHORT_LINK = 16
DOMAIN_PART = 'http://localhost/'

ERRORS_TEXTS = {
    'wrong_short_text': 'Указано недопустимое имя для короткой ссылки',
    'not_find_id': 'Указанный id не найден',
    'no_body': 'Отсутствует тело запроса',
    'no_url': '"url" является обязательным полем!',
}
