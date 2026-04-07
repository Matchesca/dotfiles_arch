from PIL import Image
from material_color_utilities import (
    theme_from_color,
    theme_from_image,
)


def get_colors(img):
    image = Image.open(img)
    theme = theme_from_image(image)
    return {
        "background": theme.schemes.dark.surface_container,
        "primary-container": theme.schemes.dark.primary_container,
        "primary": theme.schemes.dark.primary,
        "on-surface": theme.schemes.dark.on_surface
    }
