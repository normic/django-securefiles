import os

from .settings import SECUREFILES_PROTECTED_ROOT


def get_protected_file_path(file_subpath):
    """Build absolute path to protected file."""
    safe_path = os.path.normpath(os.path.join(SECUREFILES_PROTECTED_ROOT, file_subpath))
    if not safe_path.startswith(SECUREFILES_PROTECTED_ROOT):
        raise ValueError("Unsafe file path detected!")
    return safe_path
