if IN_DOCKER:  # type: ignore  # noqa: F821 # Ignoring "type" coz import is not required & flake8 NO-QA for the later
    assert MIDDLEWARE[:1] == [  # type: ignore # noqa: F821
        'django.middleware.security.SecurityMiddleware'
    ]
