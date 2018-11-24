import json
import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'YANDEX_TRANSLATOR_KEY' not in app.config or \
            not app.config['YANDEX_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    key = app.config['YANDEX_TRANSLATOR_KEY']
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?'
                        'text={}&lang={}-{}&key={}'.format(text, source_language, dest_language, key))
    if r.status_code != 200:
        return _('Error: The translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))['text'][0]
