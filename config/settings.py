"""Application settings and configuration"""

import os


class Config:
    """Base configuration"""

    # Application
    APP_NAME = "Navigation System"
    APP_VERSION = "1.0.0"

    # Map settings
    MAP_DEFAULT_LAT = 48.860381  # Paris
    MAP_DEFAULT_LON = 2.338594
    MAP_DEFAULT_ZOOM = 15
    MAP_GRAPH_DISTANCE = 5000  # meters
    MAP_NETWORK_TYPE = 'drive'  # 'drive', 'walk', 'bike', 'all'

    # UI settings
    WINDOW_WIDTH = 1000
    WINDOW_HEIGHT = 900

    # Suggestion settings
    MAX_SUGGESTIONS = 5

    @staticmethod
    def get_settings():
        """Get all settings as a dictionary"""
        return {
            'app_name': Config.APP_NAME,
            'app_version': Config.APP_VERSION,
            'map_default_location': (Config.MAP_DEFAULT_LAT, Config.MAP_DEFAULT_LON),
            'map_default_zoom': Config.MAP_DEFAULT_ZOOM,
            'map_graph_distance': Config.MAP_GRAPH_DISTANCE,
            'map_network_type': Config.MAP_NETWORK_TYPE,
            'window_size': (Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT),
            'max_suggestions': Config.MAX_SUGGESTIONS,
        }


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False


def get_config():
    """Get the appropriate configuration based on environment"""
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig()
    return DevelopmentConfig()
