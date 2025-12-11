"""Theme and styling configuration"""


class Theme:
    """Application theme constants"""

    # Colors
    PRIMARY_COLOR = '#007BFF'
    PRIMARY_HOVER = '#0056b3'
    BACKGROUND_COLOR = '#f0f0f0'
    SURFACE_COLOR = 'white'
    TEXT_COLOR = 'black'
    LIGHT_TEXT = 'gray'

    # Fonts
    FONT_FAMILY = 'Arial'
    FONT_SIZE_SMALL = 10
    FONT_SIZE_NORMAL = 12
    FONT_SIZE_LARGE = 14
    FONT_SIZE_TITLE = 16

    # Spacing
    PADDING_SMALL = 5
    PADDING_NORMAL = 10
    PADDING_LARGE = 20

    # Borders
    BORDER_RADIUS = 10
    BORDER_WIDTH = 1

    @staticmethod
    def get_button_style():
        """Get default button style configuration"""
        return {
            'bg': Theme.PRIMARY_COLOR,
            'fg': Theme.SURFACE_COLOR,
            'font': (Theme.FONT_FAMILY, Theme.FONT_SIZE_NORMAL, 'bold'),
            'relief': 'flat',
            'padx': Theme.PADDING_NORMAL,
            'pady': Theme.PADDING_SMALL,
        }

    @staticmethod
    def get_entry_style():
        """Get default entry style configuration"""
        return {
            'font': (Theme.FONT_FAMILY, Theme.FONT_SIZE_NORMAL),
            'width': 30,
        }

    @staticmethod
    def get_label_style():
        """Get default label style configuration"""
        return {
            'bg': Theme.SURFACE_COLOR,
            'fg': Theme.TEXT_COLOR,
            'font': (Theme.FONT_FAMILY, Theme.FONT_SIZE_NORMAL),
        }
