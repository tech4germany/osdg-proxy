# osdg-proxy

This project provides a minimal wrapper for the osdg.ai API,
accepting requests and replaying them towards the upstream API while adding the required authentication token.

It is a Django app based on the Django REST framework.

# Deployment

Currently it is run inside a Python venv, with an nginx proxy for TLS, via

`python3 manage.py runserver`

Make sure to enter your OSDG API token in `settings.py`, and adapt the `ALLOWED_HOSTS` and `CORS_ALLOWED_ORIGINS`
to your needs.
