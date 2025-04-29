class PermissionDeniedError(Exception):
    """Raised when a user is not allowed to download a file."""
    pass

class FileNotFoundError(Exception):
    """Raised when the requested file does not exist."""
    pass
