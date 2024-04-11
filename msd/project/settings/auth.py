import os

from dotenv import load_dotenv

load_dotenv()

AUTH_COOKIE = 'access'
AUTH_COOKIE_MAX_AGE = 60 * 60 * 24
AUTH_COOKIE_SECURE = True
AUTH_COOKIE_HTTP_ONLY = True
AUTH_COOKIE_PATH = '/'
AUTH_COOKIE_SAMESITE = 'None'

# Djoser Settings

DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL':
        'forgot-password-reset/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL':
        True,
    'SEND_CONFIRMATION_EMAIL':
        True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':
        True,
    'ACTIVATION_URL':
        'activation/{uid}/{token}',
    'USER_CREATE_PASSWORD_RETYPE':
        True,
    'SET_PASSWORD_RETYPE':
        True,
    'PASSWORD_RESET_CONFIRM_RETYPE':
        True,
    'TOKEN_MODEL':
        None,
    'SOCIAL_AUTH_ALLOWED_REDIRECT_URIS': [
        'https://mysillydreams.com/auth/google', 'https://mysillydreams.com/auth/facebook'
    ]
}

# Google Authentication

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile', 'openid'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']

# Facebook Authentication

SOCIAL_AUTH_FACEBOOK_KEY = os.getenv('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.getenv('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'email, first_name, last_name'}
