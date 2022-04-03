An example twitter-like website made from following a tutorial describing API creation, database tables, relations and schemas, deployment and various glue code needed to have a fully working application.


# Starting up:

To create venv:
py venv venv

To activate venv:
venv/scripts/activate

To install requirements:
pip install -r "requirements.txt"



Languages:


Long story:

To extract all the texts to the .pot file, you can use the following command:
(venv) $ pybabel extract -F babel.cfg -k _l -o messages.pot .

Adding Spanish (language code es), this is the command that does that:
(venv) $ pybabel init -i messages.pot -d app/translations -l es

To compile all the translations for the application, you can use the pybabel compile command as follows:
(venv) $ pybabel compile -d app/translations
compiling catalog app/translations/es/LC_MESSAGES/messages.po to
app/translations/es/LC_MESSAGES/messages.mo

Do an update procedure, which involves two steps:
(venv) $ pybabel extract -F babel.cfg -k _l -o messages.pot .
(venv) $ pybabel update -i messages.pot -d app/translations


Short Story:

To add a new language, you use:
(venv) $ flask translate init <language-code>

To update all the languages after making changes to the _() and _l() language markers:
(venv) $ flask translate update

And to compile all languages after updating the translation files:
(venv) $ flask translate compile
