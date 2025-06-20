"""
Django settings for divegob project.

Generated by 'django-admin startproject' using Django 3.2.25.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

if os.path.exists("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEVELOPMENT' in os.environ

ALLOWED_HOSTS = [
    'dive-goblin-30c473dd6e64.herokuapp.com',
    'localhost',
    '127.0.0.1',
    '8000-kimatron-divegoblin1-r3dva5yy76r.ws.codeinstitute-ide.net',
    '8000-kimatron-divegoblin1-xdp538qeiuh.ws.codeinstitute-ide.net',
]

CSRF_TRUSTED_ORIGINS = [
    'https://8000-kimatron-divegoblin1-xdp538qeiuh.ws.codeinstitute-ide.net',
    'https://dive-goblin-30c473dd6e64.herokuapp.com',
]

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google', 
    'home',
    'products',
    'bag',
    'checkout',
    'profiles',
    'crispy_forms',
    'django_countries',
    'newsletter',
    'pages',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'divegob.urls'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'bag.contexts.bag_contents',
            ],
            'builtins': [
                'crispy_forms.templatetags.crispy_forms_tags',
                'crispy_forms.templatetags.crispy_forms_field',
            ]
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# Email Configuration - FIXED LOGIC
if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'webmaster@localhost'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    BASE_URL = 'https://dive-goblin-30c473dd6e64.herokuapp.com'
    DOMAIN = 'dive-goblin-30c473dd6e64.herokuapp.com'

# Allauth settings
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'divegob.wsgi.application'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


# Database
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
    # Add connection pooling for production
    DATABASES['default']['CONN_MAX_AGE'] = 600
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
            'CONN_MAX_AGE': 300,  # 5 minutes for local development
        }
    }

# Add caching configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'dive-goblin-cache',
        'TIMEOUT': 300,  # 5 minutes default
        'OPTIONS': {
            'MAX_ENTRIES': 1000,
        }
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# AWS Configuration - FIXED FOR DJANGO 5.1
if 'USE_AWS' in os.environ:
    print("🚀 Using AWS S3 for static and media files")
    
    # AWS Settings
    AWS_STORAGE_BUCKET_NAME = 'dive-goblin'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    
    # S3 Object Parameters
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }
    
    # ✅ NEW STORAGES FORMAT (Required for Django 5.1)
    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "access_key": AWS_ACCESS_KEY_ID,
                "secret_key": AWS_SECRET_ACCESS_KEY,
                "bucket_name": AWS_STORAGE_BUCKET_NAME,
                "region_name": AWS_S3_REGION_NAME,
                "default_acl": "public-read",
                "custom_domain": AWS_S3_CUSTOM_DOMAIN,
                "object_parameters": AWS_S3_OBJECT_PARAMETERS,
                "file_overwrite": False,
                "location": "media",  # Files go in media/ folder
            },
        },
        "staticfiles": {
            "BACKEND": "storages.backends.s3.S3Storage",
            "OPTIONS": {
                "access_key": AWS_ACCESS_KEY_ID,
                "secret_key": AWS_SECRET_ACCESS_KEY,
                "bucket_name": AWS_STORAGE_BUCKET_NAME,
                "region_name": AWS_S3_REGION_NAME,
                "default_acl": "public-read",
                "custom_domain": AWS_S3_CUSTOM_DOMAIN,
                "object_parameters": AWS_S3_OBJECT_PARAMETERS,
                "location": "static",  # Files go in static/ folder
            },
        },
    }
    
    # Override static and media URLs
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
    
else:
    print("🔧 Using local static files")
    
    # ✅ LOCAL STORAGES FORMAT (Also required for Django 5.1)
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
    
# Other settings
FREE_DELIVERY_THRESHOLD = 100
STANDARD_DELIVERY_PERCENTAGE = 10
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Stripe Settings
STRIPE_CURRENCY = 'eur'
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', 'pk_test_default_value')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', 'sk_test_default_value')
STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET', 'whsec_default_value')

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}

JAZZMIN_SETTINGS = {
    # Site Title & Branding
    "site_title": "Dive Goblin Admin",
    "site_header": "🌊 Dive Goblin Control Center 🤿",
    "site_brand": "Dive Goblin",
    "site_logo": "images/divegoblogo.png",
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "site_icon": None,
    
    # Search Configuration
    "search_model": ["auth.User", "products.Product", "newsletter.NewsletterSubscriber"],
    
    # Top Navigation Menu
    "topmenu_links": [
        {
            "name": "🏠 Home", 
            "url": "/", 
            "new_window": True,
            "permissions": []
        },
        {
            "name": "🌊 Shop", 
            "url": "/products/", 
            "new_window": True,
            "permissions": []
        },
        {
            "name": "📧 Contact Support", 
            "url": "mailto:divegoblin@gmail.com", 
            "new_window": True,
            "permissions": []
        },
        {
            "name": "📊 Dashboard Stats", 
            "url": "admin:index", 
            "permissions": ["auth.view_user"]
        },
    ],
    
    # User Menu (right side dropdown)
    "usermenu_links": [
        {
            "name": "🌊 View Dive Goblin Site", 
            "url": "/", 
            "new_window": True
        },
        {
            "name": "📧 Email Support", 
            "url": "mailto:divegoblin@gmail.com", 
            "new_window": True
        },
        {
            "model": "auth.user"
        }
    ],
    
    # App and Model Organization
    "order_with_respect_to": [
        "auth", 
        "products", 
        "checkout", 
        "newsletter", 
        "profiles"
    ],
    
    # Custom Icons
    "icons": {
        # Auth & Users
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-swimmer",
        "auth.Group": "fas fa-users",
        
        # Products (Diving Equipment)
        "products": "fas fa-fish",
        "products.Product": "fas fa-mask",
        "products.Category": "fas fa-water",
        "products.Wishlist": "fas fa-heart",
        
        # Orders & Checkout
        "checkout": "fas fa-credit-card",
        "checkout.Order": "fas fa-shopping-cart",
        "checkout.OrderLineItem": "fas fa-list",
        
        # Newsletter & Marketing
        "newsletter": "fas fa-paper-plane",
        "newsletter.NewsletterSubscriber": "fas fa-envelope-open-text",
        "newsletter.Newsletter": "fas fa-newspaper",
        
        # User Profiles
        "profiles": "fas fa-id-card",
        "profiles.UserProfile": "fas fa-user-circle",
        
        # Other useful diving-themed icons
        "pages": "fas fa-file-alt",
        "bag": "fas fa-shopping-bag",
    },
    
    # Layout & Navigation
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    
    # Form Layout Options
    "changeform_format": "horizontal_tabs",  # Default form layout
    "changeform_format_overrides": {
        "auth.user": "vertical_tabs",          # User forms with side tabs
        "products.product": "horizontal_tabs", # Product forms with top tabs
        "checkout.order": "collapsible",       # Order forms as accordion
        "newsletter.newsletter": "carousel",   # Newsletter as carousel
    },
    
    # Advanced Features
    "related_modal_active": True,    # Popups instead of new pages
    "use_google_fonts_cdn": True,    # Better fonts
    "show_ui_builder": True,         # LIVE CUSTOMIZER BUTTON!
    
    # Language & Localization
    "language_chooser": False,
    
    # Custom CSS & JS
    "custom_css": "admin/css/dive_goblin_admin.css",
    "custom_js": "admin/js/dive_goblin_admin.js",
    
    # Advanced Menu Configuration
    "show_required_asterisk": True,
    "confirm_unsaved_changes": True,
    
    # Custom Links in Different Sections
    "model_links": {
        "auth.User": {
            "name": "👥 All Divers",
            "icon": "fas fa-swimmers",
        }
    },
}

# UI Theme Configuration 
JAZZMIN_UI_TWEAKS = {
    # Text Sizes
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    
    # Color Scheme (Ocean Theme)
    "brand_colour": "navbar-info",
    "accent": "accent-info",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    
    # Layout Options
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    
    # Sidebar Configuration
    "sidebar": "sidebar-dark-info",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    
    # Theme Selection
    "theme": "cosmo",
    "dark_mode_theme": "darkly", 
    
    # Button Styling
    "button_classes": {
        "primary": "btn-info",
        "secondary": "btn-outline-info",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    },
    
    # Advanced UI Options
    "actions_sticky_top": True,          # Keep actions visible when scrolling
}

JAZZMIN_SETTINGS.update({
    # Dashboard customization
    "show_recent_actions": True,
    "show_log_entries": 10,
    
    # Advanced form features
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "products.product": "horizontal_tabs",
        "checkout.order": "vertical_tabs",
        "newsletter.newsletter": "carousel",
        "profiles.userprofile": "horizontal_tabs",
    },
    
})
