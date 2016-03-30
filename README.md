# Vocabulary

Easy way, how to learn vocabulary

- author: Ondrej Sika <ondrej@ondrejsika.com>
- license: MIT <https://ondrejsika.com/license/mit.txt>

## Installation

Setup base project

    git clone git@github.com:ondrejsika/vocabulary.git
    cd vocabulary
    virtualenv .env
    source .env/bin/activate
    pip install -e .
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py collectstatic --noinput

Run in gunicorn

    gunicorn wsgi -b 0.0.0.0:9999


## Live version

If you want account, send me an email. Try demo account, user: `demo`, password: `demo`.

__<http://vocabulary.sikaapp.cz>__

