# django-securefiles
**Secure, efficient file downloads for Django using nginx internal redirects (X-Accel-Redirect).**

Inspired by django-downloadview and django-sendfile, but designed to be lighter, more modern, and Django 5+ compatible.


- Integrates with Django permissions easily
- Keeps sensitive files outside the public web root
- Very lightweight and fast (nginx serves files, not Django)
- Designed for local filesystem storage
- Safe by default (path validation to prevent traversal attacks)
-  Easily extensible for future features (e.g., cloud storage)

---

## Features

- Protect files stored outside the public static/media directories
- Serve files efficiently via nginx
- Only authenticated (or authorized) users can download files
- Simple subclassing to implement custom permission rules
- Minimal boilerplate — clean, class-based view

---

## Installation

```bash
  pip install django-securefiles
```

To use it locally for development use: 

```bash
  pip install -e /path/to/your/local/django-securefiles/
```



## Setup
#### 1. Configure nginx

Add a location block for protected files:
```nginx
    location /protected/ {
        internal;
        alias /var/www/securefiles/;
    }
```
This ensures files are only accessible via X-Accel-Redirect headers from Django.


#### 2. Configure Django settings (optional)
You can override defaults in your settings.py:
```python
SECUREFILES_PROTECTED_URL = '/protected/'
SECUREFILES_PROTECTED_ROOT = '/var/www/secure_media/'
```


#### 3. Add URL route
In your urls.py:
```python
from django.urls import path
from securefiles.views import SecureFileView

urlpatterns = [
    path('downloads/<path:file_subpath>/', SecureFileView.as_view(), name='secure_file_download'),
]
```


## Usage
By default, any authenticated user can download files.

You can customize permission logic easily:
```python
from securefiles.views import SecureFileView

class ProjectFileDownloadView(SecureFileView):
    def has_permission(self, request, file_subpath):
        return request.user.groups.filter(name='project_member').exists()
```

And wire it in urls.py:
```python
path('project-files/<path:file_subpath>/', ProjectFileDownloadView.as_view(), name='project_file_download'),
```


## Security
- Files are stored outside the static/media directory.
- Users cannot access /protected/ directly — nginx will deny.
- Path validation prevents directory traversal attacks.
- Permissions are enforced before file access is granted.

## API Reference
SecureFileView

Base class-based view for secure file downloads.


#### Methods you can override:
```python
has_permission(request, file_subpath) → returns True/False
get_file_name(file_subpath) → custom download filename

```

## Future Roadmap
- Support for cloud storage (e.g., AWS S3 signed URLs)
- Optional download logging for audit trails
- Expiring download links
- Throttling/Rate limiting (optional)

## Contributing
Pull requests and feedback are very welcome!
Please open an issue first to discuss major changes.

## License
BSD-3-Clause

