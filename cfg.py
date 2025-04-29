# cfg.py - Configuration file

# Default colors
DEFAULT_COLORS = {
    # Background colors
    "background_color": "#282a36",
    "sidebar_color": "#282a36",
    "content_color": "#282a36",

    # Button colors
    "button_color": "#6272a4",
    "button_hover_color": "#44475a",
    "button_pressed_color": "#44475a",
    "button_border_color": "#6272a4",
    "button_hover_border_color": "#bd93f9",
    "button_pressed_border_color": "#ff79c6",

    # Text colors
    "text_color": "#f8f8f2",
    "title_color": "#f8f8f2",

    # Glow effects
    "button_shadow_color": "#bd93f9",
    "button_shadow_opacity": 150,  # 0-255
    "button_shadow_blur": 15,

    # Shadow hover effect
    "button_shadow_hover_color": "#bd93f9",
    "button_shadow_hover_opacity": 200,  # 0-255
    "button_shadow_hover_blur": 25,
}

# Default sizes
DEFAULT_SIZES = {
    # Font sizes
    "main_font_size": 12,
    "title_font_size": 16,
    "button_font_size": 12,

    # Button sizes
    "button_min_height": 40,
    "button_padding_top": 8,
    "button_padding_right": 16,
    "button_padding_bottom": 8,
    "button_padding_left": 16,

    # Border radius
    "button_border_radius": 5,
}

# Transparency levels (0-100%)
DEFAULT_TRANSPARENCY = {
    "background_transparency": 100,  # 100% means no transparency
    "sidebar_transparency": 100,
    "button_transparency": 100,
}

# Default settings
settings = {
    "colors": DEFAULT_COLORS.copy(),
    "sizes": DEFAULT_SIZES.copy(),
    "transparency": DEFAULT_TRANSPARENCY.copy(),
    "theme": "dark"  # dark or light
}


# Helper function to get RGBA with transparency
def get_rgba(hex_color, opacity=255):
    """
    Convert HEX color to RGBA tuple with opacity
    """
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r}, {g}, {b}, {opacity / 255:.2f})"


# Helper function to apply transparency to a hex color (returns HEX)
def apply_transparency_to_hex(hex_color, transparency_percent):
    """
    Apply transparency to HEX color and return another HEX color
    """
    opacity = int(255 * transparency_percent / 100)
    return hex_color + format(opacity, '02x')  # Add alpha component


# Apply a theme
def apply_theme(theme_name):
    global settings

    if theme_name == "light":
        # Light theme colors
        settings["colors"] = {
            "background_color": "#f8f8f2",
            "sidebar_color": "#f5f5f5",
            "content_color": "#ffffff",

            "button_color": "#8be9fd",
            "button_hover_color": "#6dc7da",
            "button_pressed_color": "#50a9bc",
            "button_border_color": "#8be9fd",
            "button_hover_border_color": "#6272a4",
            "button_pressed_border_color": "#bd93f9",

            "text_color": "#282a36",
            "title_color": "#282a36",

            "button_shadow_color": "#6272a4",
            "button_shadow_opacity": 100,
            "button_shadow_blur": 10,

            "button_shadow_hover_color": "#6272a4",
            "button_shadow_hover_opacity": 150,
            "button_shadow_hover_blur": 20,
        }
    else:  # dark theme (default)
        settings["colors"] = DEFAULT_COLORS.copy()

    settings["theme"] = theme_name
    return settings


# Reset to defaults
def reset_to_defaults():
    global settings
    settings = {
        "colors": DEFAULT_COLORS.copy(),
        "sizes": DEFAULT_SIZES.copy(),
        "transparency": DEFAULT_TRANSPARENCY.copy(),
        "theme": "dark"
    }
    return settings


# Generate button stylesheet based on the current settings
def generate_button_stylesheet():
    colors = settings["colors"]
    sizes = settings["sizes"]
    transparency = settings["transparency"]

    # Apply transparency to colors
    btn_color = get_rgba(colors["button_color"],
                         int(255 * transparency["button_transparency"] / 100))
    btn_hover_color = get_rgba(colors["button_hover_color"],
                               int(255 * transparency["button_transparency"] / 100))
    btn_pressed_color = get_rgba(colors["button_pressed_color"],
                                 int(255 * transparency["button_transparency"] / 100))

    return f"""
        QPushButton {{
            background-color: {btn_color};
            color: {colors["text_color"]};
            border-radius: {sizes["button_border_radius"]}px;
            padding: {sizes["button_padding_top"]}px {sizes["button_padding_right"]}px 
                    {sizes["button_padding_bottom"]}px {sizes["button_padding_left"]}px;
            text-align: left;
            font-size: {sizes["button_font_size"]}px;
            border: 1px solid {colors["button_border_color"]};
            margin: 2px;
        }}
        QPushButton:hover {{
            background-color: {btn_hover_color};
            border: 1px solid {colors["button_hover_border_color"]};
            margin: 0px;
            padding: {sizes["button_padding_top"] + 2}px {sizes["button_padding_right"] + 2}px 
                    {sizes["button_padding_bottom"] + 2}px {sizes["button_padding_left"] + 2}px;
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed_color};
            color: {colors["text_color"]};
            border: 1px solid {colors["button_pressed_border_color"]};
        }}
    """


# Generate main application stylesheet
def generate_app_stylesheet():
    colors = settings["colors"]
    transparency = settings["transparency"]

    bg_color = get_rgba(colors["background_color"],
                        int(255 * transparency["background_transparency"] / 100))
    sidebar_color = get_rgba(colors["sidebar_color"],
                             int(255 * transparency["sidebar_transparency"] / 100))

    return f"""
        QMainWindow, QWidget {{
            background-color: {bg_color};
        }}
        #sidebar {{
            background-color: {sidebar_color};
        }}
    """