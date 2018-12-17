import os

env = 'local'
if 'SETTINGS' in os.environ:
    env = os.environ['SETTINGS']


def import_env(env):
    if env == 'development':
        import settings.development as settings
    elif env == 'staging':
        import settings.staging as settings
    elif env == 'testing':
        import settings.testing as settings
    elif env == 'production':
        import settings.production as settings
    else:
        import settings.local as settings
    return settings


settings = import_env(env)