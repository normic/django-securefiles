from django.conf import settings

SECUREFILES_PROTECTED_URL = getattr(settings, 'SECUREFILES_PROTECTED_URL', '/protected/')
SECUREFILES_PROTECTED_ROOT = getattr(settings, 'SECUREFILES_PROTECTED_ROOT', '/var/www/secure_files/')
