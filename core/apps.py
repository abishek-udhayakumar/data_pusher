# Importing the AppConfig class from django.apps module
from django.apps import AppConfig

# Defining the configuration for the core Django app
class CoreConfig(AppConfig):
    # Specifies the default primary key field for models in the app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Sets the name of the app to 'core'
    name = 'core'
