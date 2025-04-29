from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
                             QSlider, QColorDialog, QComboBox, QTabWidget, QGridLayout,
                             QSpinBox, QGroupBox, QWidget, QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import  QColor, QTextCharFormat # , QFont
import cfg


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Settings")
        self.setMinimumSize(800, 600)

        # Set the dialog's background color
        self.setStyleSheet(f"background-color: {cfg.settings['colors']['background_color']};")

        # Create tabs
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(f"""
            QTabWidget::pane {{
                border: 1px solid {cfg.settings['colors']['button_border_color']};
                background: {cfg.settings['colors']['background_color']};
            }}
            QTabBar::tab {{
                background: {cfg.settings['colors']['button_color']};
                color: {cfg.settings['colors']['text_color']};
                border: 1px solid {cfg.settings['colors']['button_border_color']};
                padding: 8px 12px;
                margin-right: 2px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }}
            QTabBar::tab:selected {{
                background: {cfg.settings['colors']['button_hover_color']};
                border-bottom-color: {cfg.settings['colors']['background_color']};
            }}
        """)

        # Create tabs
        self.appearance_tab = QWidget()
        self.buttons_tab = QWidget()
        self.fonts_tab = QWidget()
        self.effects_tab = QWidget()

        # Setup each tab
        self.setup_appearance_tab()
        self.setup_buttons_tab()
        self.setup_fonts_tab()
        self.setup_effects_tab()

        # Add tabs to the tab widget
        self.tabs.addTab(self.appearance_tab, "Appearance")
        self.tabs.addTab(self.buttons_tab, "Buttons")
        self.tabs.addTab(self.fonts_tab, "Fonts")
        self.tabs.addTab(self.effects_tab, "Effects")

        # Create layout for the dialog
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)

        # Add buttons at the bottom
        button_layout = QHBoxLayout()

        self.apply_btn = QPushButton("Apply")
        self.apply_btn.setStyleSheet(self.get_settings_button_style())
        self.apply_btn.clicked.connect(self.apply_settings)

        self.reset_btn = QPushButton("Reset to Default")
        self.reset_btn.setStyleSheet(self.get_settings_button_style())
        self.reset_btn.clicked.connect(self.reset_to_defaults)

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.setStyleSheet(self.get_settings_button_style())
        self.cancel_btn.clicked.connect(self.reject)

        button_layout.addWidget(self.reset_btn)
        button_layout.addStretch()
        button_layout.addWidget(self.cancel_btn)
        button_layout.addWidget(self.apply_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Store original settings in case user cancels
        self.original_settings = {
            "colors": cfg.settings["colors"].copy(),
            "sizes": cfg.settings["sizes"].copy(),
            "transparency": cfg.settings["transparency"].copy(),
            "theme": cfg.settings["theme"]
        }

        # Define variables needed for syntax highlighter
        self.comment_start_expression = QRegularExpression("/\\*")
        self.comment_end_expression = QRegularExpression("\\*/")
        self.multi_line_comment_format = QTextCharFormat()
        self.multi_line_comment_format.setForeground(QColor("#6272a4"))

    def get_settings_button_style(self):
        return f"""
            QPushButton {{
                background-color: {cfg.settings['colors']['button_color']};
                color: {cfg.settings['colors']['text_color']};
                border-radius: 4px;
                padding: 8px 16px;
                font-size: {cfg.settings['sizes']['button_font_size']}px;
                border: 1px solid {cfg.settings['colors']['button_border_color']};
            }}
            QPushButton:hover {{
                background-color: {cfg.settings['colors']['button_hover_color']};
                border: 1px solid {cfg.settings['colors']['button_hover_border_color']};
            }}
            QPushButton:pressed {{
                background-color: {cfg.settings['colors']['button_pressed_color']};
                border: 1px solid {cfg.settings['colors']['button_pressed_border_color']};
            }}
        """

    def get_label_style(self):
        return f"""
            QLabel {{
                color: {cfg.settings['colors']['text_color']};
                font-size: {cfg.settings['sizes']['main_font_size']}px;
            }}
        """

    def get_spinbox_style(self):
        return f"""
            QSpinBox {{
                background-color: {cfg.settings['colors']['background_color']};
                color: {cfg.settings['colors']['text_color']};
                border: 1px solid {cfg.settings['colors']['button_border_color']};
                padding: 4px;
                border-radius: 3px;
            }}
            QSpinBox::up-button, QSpinBox::down-button {{
                background-color: {cfg.settings['colors']['button_color']};
                border: none;
                border-radius: 2px;
                width: 16px;
            }}
            QSpinBox::up-button:hover, QSpinBox::down-button:hover {{
                background-color: {cfg.settings['colors']['button_hover_color']};
            }}
        """

    def get_slider_style(self):
        return f"""
            QSlider::groove:horizontal {{
                border: 1px solid {cfg.settings['colors']['button_border_color']};
                height: 8px;
                background: {cfg.settings['colors']['background_color']};
                margin: 2px 0;
                border-radius: 4px;
            }}
            QSlider::handle:horizontal {{
                background: {cfg.settings['colors']['button_color']};
                border: 1px solid {cfg.settings['colors']['button_border_color']};
                width: 18px;
                margin: -2px 0;
                border-radius: 9px;
            }}
            QSlider::handle:horizontal:hover {{
                background: {cfg.settings['colors']['button_hover_color']};
                border: 1px solid {cfg.settings['colors']['button_hover_border_color']};
            }}
        """

    def get_combobox_style(self):
        return f"""
            QComboBox {{
                background-color: {cfg.settings['colors']['button_color']};
                color: {cfg.settings['colors']['text_color']};
                border: 1px solid {cfg.settings['colors']['button_border_color']};
                padding: 4px 8px;
                border-radius: 3px;
            }}
            QComboBox::drop-down {{
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left-width: 1px;
                border-left-color: {cfg.settings['colors']['button_border_color']};
                border-left-style: solid;
                border-top-right-radius: 3px;
                border-bottom-right-radius: 3px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {cfg.settings['colors']['background_color']};
                color: {cfg.settings['colors']['text_color']};
                border: 1px solid {cfg.settings['colors']['button_border_color']};
                selection-background-color: {cfg.settings['colors']['button_hover_color']};
                selection-color: {cfg.settings['colors']['text_color']};
            }}
        """

    def get_groupbox_style(self):
        return f"""
            QGroupBox {{
                border: 1px solid {cfg.settings['colors']['button_border_color']};
                border-radius: 5px;
                margin-top: 20px;
                padding-top: 15px;
                color: {cfg.settings['colors']['text_color']};
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 5px;
                color: {cfg.settings['colors']['title_color']};
                font-weight: bold;
            }}
        """

    def setup_appearance_tab(self):
        layout = QVBoxLayout()

        # Theme selection
        theme_group = QGroupBox("Theme")
        theme_group.setStyleSheet(self.get_groupbox_style())
        theme_layout = QVBoxLayout()

        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Dark", "Light"])
        self.theme_combo.setCurrentText(cfg.settings["theme"].capitalize())
        self.theme_combo.setStyleSheet(self.get_combobox_style())
        self.theme_combo.currentTextChanged.connect(self.theme_changed)

        theme_layout.addWidget(QLabel("Select Theme:"))
        theme_layout.addWidget(self.theme_combo)
        theme_group.setLayout(theme_layout)

        # Background colors
        colors_group = QGroupBox("Colors")
        colors_group.setStyleSheet(self.get_groupbox_style())
        colors_layout = QGridLayout()

        # Background color
        bg_label = QLabel("Background Color:")
        bg_label.setStyleSheet(self.get_label_style())
        self.bg_color_btn = QPushButton()
        self.bg_color_btn.setStyleSheet(f"background-color: {cfg.settings['colors']['background_color']};")
        self.bg_color_btn.setFixedSize(30, 30)
        self.bg_color_btn.clicked.connect(lambda: self.choose_color("background_color"))

        # Sidebar color
        sidebar_label = QLabel("Sidebar Color:")
        sidebar_label.setStyleSheet(self.get_label_style())
        self.sidebar_color_btn = QPushButton()
        self.sidebar_color_btn.setStyleSheet(f"background-color: {cfg.settings['colors']['sidebar_color']};")
        self.sidebar_color_btn.setFixedSize(30, 30)
        self.sidebar_color_btn.clicked.connect(lambda: self.choose_color("sidebar_color"))

        # Content color
        content_label = QLabel("Content Color:")
        content_label.setStyleSheet(self.get_label_style())
        self.content_color_btn = QPushButton()
        self.content_color_btn.setStyleSheet(f"background-color: {cfg.settings['colors']['content_color']};")
        self.content_color_btn.setFixedSize(30, 30)
        self.content_color_btn.clicked.connect(lambda: self.choose_color("content_color"))

        # Text color
        text_label = QLabel("Text Color:")
        text_label.setStyleSheet(self.get_label_style())
        self.text_color_btn = QPushButton()
        self.text_color_btn.setStyleSheet(f"background-color: {cfg.settings['colors']['text_color']};")
        self.text_color_btn.setFixedSize(30, 30)
        self.text_color_btn.clicked.connect(lambda: self.choose_color("text_color"))

        # Title color
        title_label = QLabel("Title Color:")
        title_label.setStyleSheet(self.get_label_style())
        self.title_color_btn = QPushButton()
        self.title_color_btn.setStyleSheet(f"background-color: {cfg.settings['colors']['title_color']};")
        self.title_color_btn.setFixedSize(30, 30)
        self.title_color_btn.clicked.connect(lambda: self.choose_color("title_color"))

        # Add widgets to the layout
        colors_layout.addWidget(bg_label, 0, 0)
        colors_layout.addWidget(self.bg_color_btn, 0, 1)
        colors_layout.addWidget(sidebar_label, 1, 0)
        colors_layout.addWidget(self.sidebar_color_btn, 1, 1)
        colors_layout.addWidget(content_label, 2, 0)
        colors_layout.addWidget(self.content_color_btn, 2, 1)
        colors_layout.addWidget(text_label, 3, 0)
        colors_layout.addWidget(self.text_color_btn, 3, 1)
        colors_layout.addWidget(title_label, 4, 0)
        colors_layout.addWidget(self.title_color_btn, 4, 1)

        colors_group.setLayout(colors_layout)

        # Transparency
        transparency_group = QGroupBox("Transparency")
        transparency_group.setStyleSheet(self.get_groupbox_style())
        transparency_layout = QGridLayout()

        # Background transparency
        bg_trans_label = QLabel("Background Transparency:")
        bg_trans_label.setStyleSheet(self.get_label_style())
        self.bg_trans_slider = QSlider(Qt.Orientation.Horizontal)
        self.bg_trans_slider.setRange(0, 100)
        self.bg_trans_slider.setValue(cfg.settings["transparency"]["background_transparency"])
        self.bg_trans_slider.setStyleSheet(self.get_slider_style())
        self.bg_trans_value = QLabel(f"{cfg.settings['transparency']['background_transparency']}%")
        self.bg_trans_value.setStyleSheet(self.get_label_style())
        self.bg_trans_slider.valueChanged.connect(
            lambda v: self.update_transparency("background_transparency", v)
        )

        # Sidebar transparency
        sidebar_trans_label = QLabel("Sidebar Transparency:")
        sidebar_trans_label.setStyleSheet(self.get_label_style())
        self.sidebar_trans_slider = QSlider(Qt.Orientation.Horizontal)
        self.sidebar_trans_slider.setRange(0, 100)
        self.sidebar_trans_slider.setValue(cfg.settings["transparency"]["sidebar_transparency"])
        self.sidebar_trans_slider.setStyleSheet(self.get_slider_style())
        self.sidebar_trans_value = QLabel(f"{cfg.settings['transparency']['sidebar_transparency']}%")
        self.sidebar_trans_value.setStyleSheet(self.get_label_style())
        self.sidebar_trans_slider.valueChanged.connect(
            lambda v: self.update_transparency("sidebar_transparency", v)
        )

        # Add widgets to the layout
        transparency_layout.addWidget(bg_trans_label, 0, 0)
        transparency_layout.addWidget(self.bg_trans_slider, 0, 1)
        transparency_layout.addWidget(self.bg_trans_value, 0, 2)
        transparency_layout.addWidget(sidebar_trans_label, 1, 0)
        transparency_layout.addWidget(self.sidebar_trans_slider, 1, 1)
        transparency_layout.addWidget(self.sidebar_trans_value, 1, 2)

        transparency_group.setLayout(transparency_layout)

        # Add groups to the main layout
        layout.addWidget(theme_group)
        layout.addWidget(colors_group)
        layout.addWidget(transparency_group)
        layout.addStretch()

        self.appearance_tab.setLayout(layout)

    def setup_buttons_tab(self):
        layout = QVBoxLayout()

        # Button Colors
        btn_colors_group = QGroupBox("Button Colors")
        btn_colors_group.setStyleSheet(self.get_groupbox_style())
        btn_colors_layout = QGridLayout()

        # Button color
        btn_color_label = QLabel("Button Color:")
        btn_color_label.setStyleSheet(self.get_label_style())
        self.btn_color_btn = QPushButton()
        self.btn_color_btn.setStyleSheet(f"background-color: {cfg.settings['colors']['button_color']};")
        self.btn_color_btn.setFixedSize(30, 30)
        self.btn_color_btn.clicked.connect(lambda: self.choose_color("button_color"))

        # Button hover color
        btn_hover_label = QLabel("Button Hover Color:")
        btn_hover_label.setStyleSheet(self.get_label_style())
        self.btn_hover_color_btn = QPushButton()
        self.btn_hover_color_btn.setStyleSheet(f"background-color: {cfg.settings['colors']['button_hover_color']};")
        self.btn_hover_color_btn.setFixedSize(30, 30)
        self.btn_hover_color_btn.clicked.connect(lambda: self.choose_color("button_hover_color"))

        # Button pressed color
        btn_pressed_label = QLabel("Button Pressed Color:")
        btn_pressed_label.setStyleSheet(self.get_label_style())
        self.btn_pressed_color_btn = QPushButton()
        self.btn_pressed_color_btn.setStyleSheet(f"background-color: {cfg.settings['colors']['button_pressed_color']};")
        self.btn_pressed_color_btn.setFixedSize(30, 30)
        self.btn_pressed_color_btn.clicked.connect(lambda: self.choose_color("button_pressed_color"))

        # Button border color
        btn_border_label = QLabel("Button Border Color:")
        btn_border_label.setStyleSheet(self.get_label_style())
        self.btn_border_color_btn = QPushButton()
        self.btn_border_color_btn.setStyleSheet(f"background-color: {cfg.settings['colors']['button_border_color']};")
        self.btn_border_color_btn.setFixedSize(30, 30)
        self.btn_border_color_btn.clicked.connect(lambda: self.choose_color("button_border_color"))

        # Button hover border color
        btn_hover_border_label = QLabel("Button Hover Border Color:")
        btn_hover_border_label.setStyleSheet(self.get_label_style())
        self.btn_hover_border_color_btn = QPushButton()
        self.btn_hover_border_color_btn.setStyleSheet(
            f"background-color: {cfg.settings['colors']['button_hover_border_color']};")
        self.btn_hover_border_color_btn.setFixedSize(30, 30)
        self.btn_hover_border_color_btn.clicked.connect(lambda: self.choose_color("button_hover_border_color"))

        # Button pressed border color
        btn_pressed_border_label = QLabel("Button Pressed Border Color:")
        btn_pressed_border_label.setStyleSheet(self.get_label_style())
        self.btn_pressed_border_color_btn = QPushButton()
        self.btn_pressed_border_color_btn.setStyleSheet(
            f"background-color: {cfg.settings['colors']['button_pressed_border_color']};")
        self.btn_pressed_border_color_btn.setFixedSize(30, 30)
        self.btn_pressed_border_color_btn.clicked.connect(lambda: self.choose_color("button_pressed_border_color"))

        # Add widgets to the layout
        btn_colors_layout.addWidget(btn_color_label, 0, 0)
        btn_colors_layout.addWidget(self.btn_color_btn, 0, 1)
        btn_colors_layout.addWidget(btn_hover_label, 1, 0)
        btn_colors_layout.addWidget(self.btn_hover_color_btn, 1, 1)
        btn_colors_layout.addWidget(btn_pressed_label, 2, 0)
        btn_colors_layout.addWidget(self.btn_pressed_color_btn, 2, 1)
        btn_colors_layout.addWidget(btn_border_label, 3, 0)
        btn_colors_layout.addWidget(self.btn_border_color_btn, 3, 1)
        btn_colors_layout.addWidget(btn_hover_border_label, 4, 0)
        btn_colors_layout.addWidget(self.btn_hover_border_color_btn, 4, 1)
        btn_colors_layout.addWidget(btn_pressed_border_label, 5, 0)
        btn_colors_layout.addWidget(self.btn_pressed_border_color_btn, 5, 1)

        btn_colors_group.setLayout(btn_colors_layout)

        # Button Sizes
        btn_sizes_group = QGroupBox("Button Sizes and Shapes")
        btn_sizes_group.setStyleSheet(self.get_groupbox_style())
        btn_sizes_layout = QGridLayout()

        # Button min height
        btn_height_label = QLabel("Button Min Height:")
        btn_height_label.setStyleSheet(self.get_label_style())
        self.btn_height_spin = QSpinBox()
        self.btn_height_spin.setRange(20, 100)
        self.btn_height_spin.setValue(cfg.settings["sizes"]["button_min_height"])
        self.btn_height_spin.setStyleSheet(self.get_spinbox_style())
        self.btn_height_spin.valueChanged.connect(
            lambda v: self.update_size("button_min_height", v)
        )

        # Button padding
        btn_padding_top_label = QLabel("Button Padding Top:")
        btn_padding_top_label.setStyleSheet(self.get_label_style())
        self.btn_padding_top_spin = QSpinBox()
        self.btn_padding_top_spin.setRange(0, 30)
        self.btn_padding_top_spin.setValue(cfg.settings["sizes"]["button_padding_top"])
        self.btn_padding_top_spin.setStyleSheet(self.get_spinbox_style())
        self.btn_padding_top_spin.valueChanged.connect(
            lambda v: self.update_size("button_padding_top", v)
        )

        btn_padding_right_label = QLabel("Button Padding Right:")
        btn_padding_right_label.setStyleSheet(self.get_label_style())
        self.btn_padding_right_spin = QSpinBox()
        self.btn_padding_right_spin.setRange(0, 50)
        self.btn_padding_right_spin.setValue(cfg.settings["sizes"]["button_padding_right"])
        self.btn_padding_right_spin.setStyleSheet(self.get_spinbox_style())
        self.btn_padding_right_spin.valueChanged.connect(
            lambda v: self.update_size("button_padding_right", v)
        )

        # Button padding bottom
        btn_padding_bottom_label = QLabel("Button Padding Bottom:")
        btn_padding_bottom_label.setStyleSheet(self.get_label_style())
        self.btn_padding_bottom_spin = QSpinBox()
        self.btn_padding_bottom_spin.setRange(0, 30)
        self.btn_padding_bottom_spin.setValue(cfg.settings["sizes"]["button_padding_bottom"])
        self.btn_padding_bottom_spin.setStyleSheet(self.get_spinbox_style())
        self.btn_padding_bottom_spin.valueChanged.connect(
            lambda v: self.update_size("button_padding_bottom", v)
        )

        btn_padding_left_label = QLabel("Button Padding Left:")
        btn_padding_left_label.setStyleSheet(self.get_label_style())
        self.btn_padding_left_spin = QSpinBox()
        self.btn_padding_left_spin.setRange(0, 50)
        self.btn_padding_left_spin.setValue(cfg.settings["sizes"]["button_padding_left"])
        self.btn_padding_left_spin.setStyleSheet(self.get_spinbox_style())
        self.btn_padding_left_spin.valueChanged.connect(
            lambda v: self.update_size("button_padding_left", v)
        )

        # Button border radius
        btn_radius_label = QLabel("Button Border Radius:")
        btn_radius_label.setStyleSheet(self.get_label_style())
        self.btn_radius_spin = QSpinBox()
        self.btn_radius_spin.setRange(0, 30)
        self.btn_radius_spin.setValue(cfg.settings["sizes"]["button_border_radius"])
        self.btn_radius_spin.setStyleSheet(self.get_spinbox_style())
        self.btn_radius_spin.valueChanged.connect(
            lambda v: self.update_size("button_border_radius", v)
        )

        # Button transparency
        btn_trans_label = QLabel("Button Transparency:")
        btn_trans_label.setStyleSheet(self.get_label_style())
        self.btn_trans_slider = QSlider(Qt.Orientation.Horizontal)
        self.btn_trans_slider.setRange(0, 100)
        self.btn_trans_slider.setValue(cfg.settings["transparency"]["button_transparency"])
        self.btn_trans_slider.setStyleSheet(self.get_slider_style())
        self.btn_trans_value = QLabel(f"{cfg.settings['transparency']['button_transparency']}%")
        self.btn_trans_value.setStyleSheet(self.get_label_style())
        self.btn_trans_slider.valueChanged.connect(
            lambda v: self.update_transparency("button_transparency", v)
        )

        # Add widgets to the layout
        btn_sizes_layout.addWidget(btn_height_label, 0, 0)
        btn_sizes_layout.addWidget(self.btn_height_spin, 0, 1)

        btn_sizes_layout.addWidget(btn_padding_top_label, 1, 0)
        btn_sizes_layout.addWidget(self.btn_padding_top_spin, 1, 1)
        btn_sizes_layout.addWidget(btn_padding_right_label, 2, 0)
        btn_sizes_layout.addWidget(self.btn_padding_right_spin, 2, 1)
        btn_sizes_layout.addWidget(btn_padding_bottom_label, 3, 0)
        btn_sizes_layout.addWidget(self.btn_padding_bottom_spin, 3, 1)
        btn_sizes_layout.addWidget(btn_padding_left_label, 4, 0)
        btn_sizes_layout.addWidget(self.btn_padding_left_spin, 4, 1)

        btn_sizes_layout.addWidget(btn_radius_label, 5, 0)
        btn_sizes_layout.addWidget(self.btn_radius_spin, 5, 1)

        btn_sizes_layout.addWidget(btn_trans_label, 6, 0)
        btn_sizes_layout.addWidget(self.btn_trans_slider, 6, 1)
        btn_sizes_layout.addWidget(self.btn_trans_value, 6, 2)

        btn_sizes_group.setLayout(btn_sizes_layout)

        # Add groups to the main layout
        layout.addWidget(btn_colors_group)
        layout.addWidget(btn_sizes_group)
        layout.addStretch()

        self.buttons_tab.setLayout(layout)

    def setup_fonts_tab(self):
        layout = QVBoxLayout()

        # Font sizes
        font_sizes_group = QGroupBox("Font Sizes")
        font_sizes_group.setStyleSheet(self.get_groupbox_style())
        font_sizes_layout = QGridLayout()

        # Main font size
        main_font_label = QLabel("Main Font Size:")
        main_font_label.setStyleSheet(self.get_label_style())
        self.main_font_spin:QSpinBox = QSpinBox()
        self.main_font_spin.setRange(8, 24)
        self.main_font_spin.setValue(cfg.settings["sizes"]["main_font_size"])
        self.main_font_spin.setStyleSheet(self.get_spinbox_style())
        self.main_font_spin.valueChanged.connect(
            lambda v: self.update_size("main_font_size", v)
        )

        # Title font size
        title_font_label = QLabel("Title Font Size:")
        title_font_label.setStyleSheet(self.get_label_style())
        self.title_font_spin = QSpinBox()
        self.title_font_spin.setRange(12, 36)
        self.title_font_spin.setValue(cfg.settings["sizes"]["title_font_size"])
        self.title_font_spin.setStyleSheet(self.get_spinbox_style())
        self.title_font_spin.valueChanged.connect(
            lambda v: self.update_size("title_font_size", v)
        )

        # Button font size
        button_font_label = QLabel("Button Font Size:")
        button_font_label.setStyleSheet(self.get_label_style())
        self.button_font_spin = QSpinBox()
        self.button_font_spin.setRange(8, 24)
        self.button_font_spin.setValue(cfg.settings["sizes"]["button_font_size"])
        self.button_font_spin.setStyleSheet(self.get_spinbox_style())
        self.button_font_spin.valueChanged.connect(
            lambda v: self.update_size("button_font_size", v)
        )

        # Add widgets to the layout
        font_sizes_layout.addWidget(main_font_label, 0, 0)
        font_sizes_layout.addWidget(self.main_font_spin, 0, 1)
        font_sizes_layout.addWidget(title_font_label, 1, 0)
        font_sizes_layout.addWidget(self.title_font_spin, 1, 1)
        font_sizes_layout.addWidget(button_font_label, 2, 0)
        font_sizes_layout.addWidget(self.button_font_spin, 2, 1)

        # Sample text display
        sample_text_group = QGroupBox("Sample Text")
        sample_text_group.setStyleSheet(self.get_groupbox_style())
        sample_text_layout = QVBoxLayout()

        self.sample_title = QLabel("Sample Title")
        self.sample_title.setStyleSheet(f"""
                    color: {cfg.settings['colors']['title_color']};
                    font-size: {cfg.settings['sizes']['title_font_size']}px;
                    font-weight: bold;
                """)

        self.sample_text = QLabel("This is an example of the main text.\nAdjust the font sizes to see how it looks.")
        self.sample_text.setStyleSheet(f"""
                    color: {cfg.settings['colors']['text_color']};
                    font-size: {cfg.settings['sizes']['main_font_size']}px;
                """)

        self.sample_button = QPushButton("Sample Button")
        self.sample_button.setStyleSheet(cfg.generate_button_stylesheet())

        sample_text_layout.addWidget(self.sample_title)
        sample_text_layout.addWidget(self.sample_text)
        sample_text_layout.addWidget(self.sample_button)
        sample_text_group.setLayout(sample_text_layout)

        font_sizes_group.setLayout(font_sizes_layout)

        # Add groups to the main layout
        layout.addWidget(font_sizes_group)
        layout.addWidget(sample_text_group)
        layout.addStretch()

        self.fonts_tab.setLayout(layout)

    def setup_effects_tab(self):
        layout = QVBoxLayout()

        # Shadow effects
        shadow_group = QGroupBox("Shadow Effects")
        shadow_group.setStyleSheet(self.get_groupbox_style())
        shadow_layout = QGridLayout()

        # Shadow color
        shadow_color_label = QLabel("Shadow Color:")
        shadow_color_label.setStyleSheet(self.get_label_style())
        self.shadow_color_btn = QPushButton()
        self.shadow_color_btn.setStyleSheet(f"background-color: {cfg.settings['colors']['button_shadow_color']};")
        self.shadow_color_btn.setFixedSize(30, 30)
        self.shadow_color_btn.clicked.connect(lambda: self.choose_color("button_shadow_color"))

        # Shadow opacity
        shadow_opacity_label = QLabel("Shadow Opacity:")
        shadow_opacity_label.setStyleSheet(self.get_label_style())
        self.shadow_opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.shadow_opacity_slider.setRange(0, 255)
        self.shadow_opacity_slider.setValue(cfg.settings["colors"]["button_shadow_opacity"])
        self.shadow_opacity_slider.setStyleSheet(self.get_slider_style())
        self.shadow_opacity_value = QLabel(f"{cfg.settings['colors']['button_shadow_opacity'] / 255:.0%}")
        self.shadow_opacity_value.setStyleSheet(self.get_label_style())
        self.shadow_opacity_slider.valueChanged.connect(self.update_shadow_opacity)

        # Shadow blur
        shadow_blur_label = QLabel("Shadow Blur:")
        shadow_blur_label.setStyleSheet(self.get_label_style())
        self.shadow_blur_slider = QSlider(Qt.Orientation.Horizontal)
        self.shadow_blur_slider.setRange(0, 50)
        self.shadow_blur_slider.setValue(cfg.settings["colors"]["button_shadow_blur"])
        self.shadow_blur_slider.setStyleSheet(self.get_slider_style())
        self.shadow_blur_value = QLabel(f"{cfg.settings['colors']['button_shadow_blur']}px")
        self.shadow_blur_value.setStyleSheet(self.get_label_style())
        self.shadow_blur_slider.valueChanged.connect(self.update_shadow_blur)

        # Hover effects
        hover_shadow_color_label = QLabel("Hover Shadow Color:")
        hover_shadow_color_label.setStyleSheet(self.get_label_style())
        self.hover_shadow_color_btn = QPushButton()
        self.hover_shadow_color_btn.setStyleSheet(
            f"background-color: {cfg.settings['colors']['button_shadow_hover_color']};")
        self.hover_shadow_color_btn.setFixedSize(30, 30)
        self.hover_shadow_color_btn.clicked.connect(lambda: self.choose_color("button_shadow_hover_color"))

        hover_shadow_opacity_label = QLabel("Hover Shadow Opacity:")
        hover_shadow_opacity_label.setStyleSheet(self.get_label_style())
        self.hover_shadow_opacity_slider = QSlider(Qt.Orientation.Horizontal)
        self.hover_shadow_opacity_slider.setRange(0, 255)
        self.hover_shadow_opacity_slider.setValue(cfg.settings["colors"]["button_shadow_hover_opacity"])
        self.hover_shadow_opacity_slider.setStyleSheet(self.get_slider_style())
        self.hover_shadow_opacity_value = QLabel(f"{cfg.settings['colors']['button_shadow_hover_opacity'] / 255:.0%}")
        self.hover_shadow_opacity_value.setStyleSheet(self.get_label_style())
        self.hover_shadow_opacity_slider.valueChanged.connect(self.update_hover_shadow_opacity)

        hover_shadow_blur_label = QLabel("Hover Shadow Blur:")
        hover_shadow_blur_label.setStyleSheet(self.get_label_style())
        self.hover_shadow_blur_slider = QSlider(Qt.Orientation.Horizontal)
        self.hover_shadow_blur_slider.setRange(0, 50)
        self.hover_shadow_blur_slider.setValue(cfg.settings["colors"]["button_shadow_hover_blur"])
        self.hover_shadow_blur_slider.setStyleSheet(self.get_slider_style())
        self.hover_shadow_blur_value = QLabel(f"{cfg.settings['colors']['button_shadow_hover_blur']}px")
        self.hover_shadow_blur_value.setStyleSheet(self.get_label_style())
        self.hover_shadow_blur_slider.valueChanged.connect(self.update_hover_shadow_blur)

        # Add widgets to the layout
        shadow_layout.addWidget(shadow_color_label, 0, 0)
        shadow_layout.addWidget(self.shadow_color_btn, 0, 1)
        shadow_layout.addWidget(shadow_opacity_label, 1, 0)
        shadow_layout.addWidget(self.shadow_opacity_slider, 1, 1)
        shadow_layout.addWidget(self.shadow_opacity_value, 1, 2)
        shadow_layout.addWidget(shadow_blur_label, 2, 0)
        shadow_layout.addWidget(self.shadow_blur_slider, 2, 1)
        shadow_layout.addWidget(self.shadow_blur_value, 2, 2)

        shadow_layout.addWidget(hover_shadow_color_label, 3, 0)
        shadow_layout.addWidget(self.hover_shadow_color_btn, 3, 1)
        shadow_layout.addWidget(hover_shadow_opacity_label, 4, 0)
        shadow_layout.addWidget(self.hover_shadow_opacity_slider, 4, 1)
        shadow_layout.addWidget(self.hover_shadow_opacity_value, 4, 2)
        shadow_layout.addWidget(hover_shadow_blur_label, 5, 0)
        shadow_layout.addWidget(self.hover_shadow_blur_slider, 5, 1)
        shadow_layout.addWidget(self.hover_shadow_blur_value, 5, 2)

        # Sample button with effects
        effect_sample_group = QGroupBox("Effect Preview")
        effect_sample_group.setStyleSheet(self.get_groupbox_style())
        effect_sample_layout = QVBoxLayout()

        self.effect_sample_button = QPushButton("Sample Button with Effect")
        self.effect_sample_button.setStyleSheet(cfg.generate_button_stylesheet())
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(cfg.settings["colors"]["button_shadow_blur"])
        shadow_effect.setColor(QColor(
            cfg.settings["colors"]["button_shadow_color"] +
            format(cfg.settings["colors"]["button_shadow_opacity"], '02x')
        ))
        shadow_effect.setOffset(0, 0)
        self.effect_sample_button.setGraphicsEffect(shadow_effect)

        effect_sample_layout.addWidget(self.effect_sample_button)
        effect_sample_group.setLayout(effect_sample_layout)

        shadow_group.setLayout(shadow_layout)

        # Add groups to the main layout
        layout.addWidget(shadow_group)
        layout.addWidget(effect_sample_group)
        layout.addStretch()

        self.effects_tab.setLayout(layout)

    # Method to handle color selection
    def choose_color(self, color_key):
        current_color = QColor(cfg.settings["colors"][color_key])
        color = QColorDialog.getColor(current_color, self, f"Select {color_key.replace('_', ' ').title()}")

        if color.isValid():
            hex_color = color.name()
            cfg.settings["colors"][color_key] = hex_color

            # Update the color button
            button_name = f"{color_key}_btn"
            if hasattr(self, button_name):
                getattr(self, button_name).setStyleSheet(f"background-color: {hex_color};")

            self.update_sample_elements()

    # Method to handle transparency updates
    def update_transparency(self, trans_key, value):
        cfg.settings["transparency"][trans_key] = value

        # Update the label
        value_label_name = f"{trans_key.replace('transparency', 'trans')}_value"
        if hasattr(self, value_label_name):
            getattr(self, value_label_name).setText(f"{value}%")

        self.update_sample_elements()

    # Method to handle size updates
    def update_size(self, size_key, value):
        cfg.settings["sizes"][size_key] = value
        self.update_sample_elements()

    # Method to handle shadow opacity updates
    def update_shadow_opacity(self, value):
        cfg.settings["colors"]["button_shadow_opacity"] = value
        self.shadow_opacity_value.setText(f"{value / 255:.0%}")
        self.update_sample_effects()

    # Method to handle shadow blur updates
    def update_shadow_blur(self, value):
        cfg.settings["colors"]["button_shadow_blur"] = value
        self.shadow_blur_value.setText(f"{value}px")
        self.update_sample_effects()

    # Method to handle hover shadow opacity updates
    def update_hover_shadow_opacity(self, value):
        cfg.settings["colors"]["button_shadow_hover_opacity"] = value
        self.hover_shadow_opacity_value.setText(f"{value / 255:.0%}")

    # Method to handle hover shadow blur updates
    def update_hover_shadow_blur(self, value):
        cfg.settings["colors"]["button_shadow_hover_blur"] = value
        self.hover_shadow_blur_value.setText(f"{value}px")

    # Method to update sample effects
    def update_sample_effects(self):
        # Update sample button effects
        if hasattr(self, "effect_sample_button"):
            shadow_effect = QGraphicsDropShadowEffect()
            shadow_effect.setBlurRadius(cfg.settings["colors"]["button_shadow_blur"])
            shadow_effect.setColor(QColor(
                cfg.settings["colors"]["button_shadow_color"] +
                format(cfg.settings["colors"]["button_shadow_opacity"], '02x')
            ))
            shadow_effect.setOffset(0, 0)
            self.effect_sample_button.setGraphicsEffect(shadow_effect)
            self.effect_sample_button.setStyleSheet(cfg.generate_button_stylesheet())

    # Method to handle theme changes
    def theme_changed(self, theme_name):
        cfg.apply_theme(theme_name.lower())
        self.update_all_color_buttons()
        self.update_sample_elements()

    # Method to update all color buttons
    def update_all_color_buttons(self):
        # Update all color buttons to reflect current settings
        for color_key in cfg.settings["colors"]:
            button_name = f"{color_key}_btn"
            if hasattr(self, button_name):
                getattr(self, button_name).setStyleSheet(f"background-color: {cfg.settings['colors'][color_key]};")

    # Method to update sample elements
    def update_sample_elements(self):
        # Update sample text and button styles
        if hasattr(self, "sample_title"):
            self.sample_title.setStyleSheet(f"""
                color: {cfg.settings['colors']['title_color']};
                font-size: {cfg.settings['sizes']['title_font_size']}px;
                font-weight: bold;
            """)

        if hasattr(self, "sample_text"):
            self.sample_text.setStyleSheet(f"""
                color: {cfg.settings['colors']['text_color']};
                font-size: {cfg.settings['sizes']['main_font_size']}px;
            """)

        if hasattr(self, "sample_button"):
            self.sample_button.setStyleSheet(cfg.generate_button_stylesheet())

        self.update_sample_effects()

    # Method to reset settings to defaults
    def reset_to_defaults(self):
        cfg.reset_to_defaults()

        # Update all UI elements
        self.theme_combo.setCurrentText(cfg.settings["theme"].capitalize())

        # Update sliders
        self.bg_trans_slider.setValue(cfg.settings["transparency"]["background_transparency"])
        self.sidebar_trans_slider.setValue(cfg.settings["transparency"]["sidebar_transparency"])
        self.btn_trans_slider.setValue(cfg.settings["transparency"]["button_transparency"])

        # Update spinboxes
        self.btn_height_spin.setValue(cfg.settings["sizes"]["button_min_height"])
        self.btn_padding_top_spin.setValue(cfg.settings["sizes"]["button_padding_top"])
        self.btn_padding_right_spin.setValue(cfg.settings["sizes"]["button_padding_right"])
        self.btn_padding_bottom_spin.setValue(cfg.settings["sizes"]["button_padding_bottom"])
        self.btn_padding_left_spin.setValue(cfg.settings["sizes"]["button_padding_left"])
        self.btn_radius_spin.setValue(cfg.settings["sizes"]["button_border_radius"])

        self.main_font_spin.setValue(cfg.settings["sizes"]["main_font_size"])
        self.title_font_spin.setValue(cfg.settings["sizes"]["title_font_size"])
        self.button_font_spin.setValue(cfg.settings["sizes"]["button_font_size"])

        # Update shadow sliders
        self.shadow_opacity_slider.setValue(cfg.settings["colors"]["button_shadow_opacity"])
        self.shadow_blur_slider.setValue(cfg.settings["colors"]["button_shadow_blur"])
        self.hover_shadow_opacity_slider.setValue(cfg.settings["colors"]["button_shadow_hover_opacity"])
        self.hover_shadow_blur_slider.setValue(cfg.settings["colors"]["button_shadow_hover_blur"])

        # Update color buttons
        self.update_all_color_buttons()

        # Update sample elements
        self.update_sample_elements()

    # Method to apply settings
    def apply_settings(self):
        # Save current settings for next time
        self.original_settings = {
            "colors": cfg.settings["colors"].copy(),
            "sizes": cfg.settings["sizes"].copy(),
            "transparency": cfg.settings["transparency"].copy(),
            "theme": cfg.settings["theme"]
        }

        # Apply settings to the main window
        if self.parent:
            self.parent.apply_settings()

        self.accept()