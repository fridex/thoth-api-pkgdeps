import os


class Configuration:
    # Please provide explicitly.
    APP_SECRET_KEY = os.environ['APP_SECRET_KEY']
    APP_SERVICE_PORT = os.getenv('APP_SERVICE_PORT', 34000)
    SWAGGER_YAML_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'swagger.yaml')
