from __future__ import absolute_import

from django.apps import AppConfig


class Config(AppConfig):
    name = "sentry_auth_saml2.generic"

    def ready(self):
        from sentry.auth import register

        from .provider import GenericSAML2Provider

        register('saml2', GenericSAML2Provider)
