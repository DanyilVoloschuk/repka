from datetime import timedelta

from .environment import env


REPKS_FEATURES = env.list("REPKS_FEATURES", default=[])

REPKS_EMAIL_FROM = env.str("REPKS_EMAIL_FROM", default="no-reply@example.com")

REPKS_AUTH_COOKIE_NAME = env.str("REPKS_AUTH_COOKIE_NAME", default="a")

# Reset password link lifetime interval (in seconds). By default: 1 hour.
REPKS_RESET_PASSWORD_EXPIRATION_DELTA = timedelta(seconds=env.int("REPKS_RESET_PASSWORD_EXPIRATION_DELTA", default=3600))

if "LOG_SQL" in REPKS_FEATURES:  # pragma: no cover
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {"require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}},
        "formatters": {
            "simple": {"format": "[%(asctime)s] %(levelname)s %(message)s"},
            "verbose": {"format": "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"},
            "sql": {"()": "repks.loggers.SQLFormatter", "format": "[%(duration).3f] %(statement)s"},
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "verbose", "level": "DEBUG"},
            "sql": {"class": "logging.StreamHandler", "formatter": "sql", "level": "DEBUG"},
        },
        "loggers": {
            "django.db.backends": {
                "handlers": ["sql"],
                "level": "DEBUG",
                "filters": ["require_debug_true"],
                "propagate": False,
            },
            "django.db.backends.schema": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        },
    }
