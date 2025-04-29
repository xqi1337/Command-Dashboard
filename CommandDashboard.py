from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
                             QTextEdit, QScrollArea, QFrame, QGraphicsDropShadowEffect, QApplication)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from command_data import COMMAND_DATA
from PyDraculaButton import PyDraculaButton
from SettingsDialog import SettingsDialog
from SQLSyntaxHighlighter import SQLSyntaxHighlighter
import cfg


class CommandDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.command_data = COMMAND_DATA
        self.sql_highlighter = None
        self.current_category_type = None
        self.current_state = "main"  # track navigation state
        self.current_category = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("GET GOOD GET COPYSENSE")
        self.setMinimumSize(1200, 700)
        self.setStyleSheet(f"background-color: {cfg.settings['colors']['background_color']};")

        # Create central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Create main UI elements
        self.create_sidebar()
        self.create_content_area()
        self.create_output_area()

        # Create content container
        self.content_container = QWidget()
        self.content_container.setStyleSheet("background-color: transparent;")
        self.content_container_layout = QVBoxLayout(self.content_container)
        self.content_container_layout.setContentsMargins(0, 0, 0, 0)
        self.content_container_layout.setSpacing(0)
        self.content_container_layout.addWidget(self.content_area)
        self.content_container_layout.addWidget(self.output_area)

        # Add widgets to the main layout
        self.main_layout.addWidget(self.sidebar_frame)
        self.main_layout.addWidget(self.content_container)

        # Display main menu
        self.show_main_menu()

    def create_sidebar(self):
        # Create sidebar frame
        self.sidebar_frame = QFrame()
        self.sidebar_frame.setStyleSheet(f"background-color: {cfg.settings['colors']['background_color']};")
        self.sidebar_frame.setFixedWidth(250)

        # Create sidebar layout
        self.sidebar_layout = QVBoxLayout(self.sidebar_frame)
        self.sidebar_layout.setContentsMargins(10, 20, 10, 20)
        self.sidebar_layout.setSpacing(15)

        # Add title
        self.sidebar_title = QLabel("MENU")
        self.sidebar_title.setStyleSheet(f"""
            color: {cfg.settings['colors']['title_color']};
            font-size: {cfg.settings['sizes']['title_font_size']}px;
            font-weight: bold;
            padding-bottom: 10px;
            border-bottom: 1px solid {cfg.settings['colors']['button_border_color']};
        """)
        self.sidebar_layout.addWidget(self.sidebar_title)
        self.sidebar_layout.addSpacing(20)

    def create_content_area(self):
        # Create content area
        self.content_area = QFrame()
        self.content_area.setStyleSheet(f"background-color: {cfg.settings['colors']['background_color']};")

        # Create content layout
        self.content_layout = QVBoxLayout(self.content_area)
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.content_layout.setSpacing(15)

        # Add title
        self.content_title = QLabel()
        self.content_title.setStyleSheet(f"""
            color: {cfg.settings['colors']['title_color']};
            font-size: {cfg.settings['sizes']['title_font_size']}px;
            font-weight: bold;
        """)
        self.content_layout.addWidget(self.content_title)

        # Create scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet(f"""
            QScrollArea {{
                border: none;
                background: transparent;
            }}
            QScrollBar:vertical {{
                background: {cfg.settings['colors']['background_color']};
                width: 10px;
                margin: 0px 0px 0px 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {cfg.settings['colors']['button_color']};
                min-height: 20px;
                border-radius: 5px;
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
        """)

        # Create scroll content widget
        self.scroll_content = QWidget()
        self.scroll_content.setStyleSheet("background-color: transparent;")
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setContentsMargins(0, 0, 10, 0)
        self.scroll_layout.setSpacing(20)

        # Set the widget in scroll area
        self.scroll_area.setWidget(self.scroll_content)

        # Add scroll area to content layout
        self.content_layout.addWidget(self.scroll_area)

    def create_output_area(self):
        # Create output area
        self.output_area = QFrame()
        self.output_area.setStyleSheet(f"background-color: {cfg.settings['colors']['background_color']};")
        self.output_area.setFixedHeight(250)

        # Create output layout
        self.output_layout = QHBoxLayout(self.output_area)
        self.output_layout.setContentsMargins(10, 10, 10, 10)
        self.output_layout.setSpacing(10)

        # Create text display with copy button function
        def create_text_display(is_command=True):
            container = QWidget()
            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(5)

            text_display = QTextEdit()
            text_display.setReadOnly(True)
            font_family = "Consolas" if is_command else "Segoe UI"
            text_display.setStyleSheet(f"""
                background-color: {cfg.settings['colors']['background_color']};
                color: {cfg.settings['colors']['text_color']};
                border: 1px solid {cfg.settings['colors']['button_border_color']};
                border-radius: 5px;
                padding: 10px;
                font-family: {font_family};
                font-size: {cfg.settings['sizes']['main_font_size']}px;
            """)

            copy_btn = PyDraculaButton("COPY")
            copy_btn.setFixedHeight(30)
            copy_btn.clicked.connect(lambda: self.copy_to_clipboard(text_display.toPlainText()))

            layout.addWidget(text_display)
            layout.addWidget(copy_btn)

            return container, text_display

        # Create command display
        command_container, self.command_display = create_text_display(is_command=True)

        # Create explanation display
        explanation_container, self.explanation_display = create_text_display(is_command=False)

        # Add displays to output layout
        self.output_layout.addWidget(command_container)
        self.output_layout.addWidget(explanation_container)

    def show_settings_dialog(self):
        """Show the settings dialog"""
        dialog = SettingsDialog(self)
        dialog.exec()

    def apply_settings(self):
        """Apply settings to all UI elements"""
        # Update main window style
        self.setStyleSheet(f"background-color: {cfg.settings['colors']['background_color']};")

        # Update sidebar
        self.sidebar_frame.setStyleSheet(f"background-color: {cfg.settings['colors']['background_color']};")
        self.sidebar_title.setStyleSheet(f"""
            color: {cfg.settings['colors']['title_color']};
            font-size: {cfg.settings['sizes']['title_font_size']}px;
            font-weight: bold;
            padding-bottom: 10px;
            border-bottom: 1px solid {cfg.settings['colors']['button_border_color']};
        """)

        # Update content area
        self.content_area.setStyleSheet(f"background-color: {cfg.settings['colors']['background_color']};")
        self.content_title.setStyleSheet(f"""
            color: {cfg.settings['colors']['title_color']};
            font-size: {cfg.settings['sizes']['title_font_size']}px;
            font-weight: bold;
        """)

        # Update scroll area
        self.scroll_area.setStyleSheet(f"""
            QScrollArea {{
                border: none;
                background: transparent;
            }}
            QScrollBar:vertical {{
                background: {cfg.settings['colors']['background_color']};
                width: 10px;
                margin: 0px 0px 0px 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {cfg.settings['colors']['button_color']};
                min-height: 20px;
                border-radius: 5px;
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
        """)

        # Update output area
        self.output_area.setStyleSheet(f"background-color: {cfg.settings['colors']['background_color']};")

        # Update text displays
        self.command_display.setStyleSheet(f"""
            background-color: {cfg.settings['colors']['background_color']};
            color: {cfg.settings['colors']['text_color']};
            border: 1px solid {cfg.settings['colors']['button_border_color']};
            border-radius: 5px;
            padding: 10px;
            font-family: Consolas;
            font-size: {cfg.settings['sizes']['main_font_size']}px;
        """)

        self.explanation_display.setStyleSheet(f"""
            background-color: {cfg.settings['colors']['background_color']};
            color: {cfg.settings['colors']['text_color']};
            border: 1px solid {cfg.settings['colors']['button_border_color']};
            border-radius: 5px;
            padding: 10px;
            font-family: Segoe UI;
            font-size: {cfg.settings['sizes']['main_font_size']}px;
        """)

        # Update all buttons
        for btn in self.findChildren(PyDraculaButton):
            btn.setStyleSheet(cfg.generate_button_stylesheet())
            btn.update_shadow_effect()

        # If we have a syntax highlighter, refresh it
        if self.sql_highlighter:
            text = self.command_display.toPlainText()
            self.command_display.clear()
            self.command_display.setPlainText(text)
            self.sql_highlighter = SQLSyntaxHighlighter(self.command_display.document())

    def copy_to_clipboard(self, text):
        """Copy text to clipboard"""
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)

    def clear_sidebar(self):
        """Clear all items from sidebar"""
        # Remove all widgets except the title
        while self.sidebar_layout.count() > 1:
            item = self.sidebar_layout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()

    def clear_content(self):
        """Clear content from the scroll area"""
        # Clear scroll content
        while self.scroll_layout.count():
            item = self.scroll_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Clear command and explanation displays
        self.command_display.clear()
        self.explanation_display.clear()

        # Remove any existing highlighter
        if self.sql_highlighter:
            self.sql_highlighter.setDocument(None)
            self.sql_highlighter = None

    def add_common_sidebar_buttons(self):
        """Add settings and exit buttons to sidebar"""
        self.sidebar_layout.addStretch()

        # Create settings button
        settings_btn = PyDraculaButton("EINSTELLUNGEN")
        settings_btn.setToolTip("EINSTELLUNGEN")
        settings_btn.clicked.connect(self.show_settings_dialog)
        self.sidebar_layout.addWidget(settings_btn)

        # Create exit button
        exit_btn = PyDraculaButton("BEENDEN")
        exit_btn.clicked.connect(self.close)
        self.sidebar_layout.addWidget(exit_btn)

    def show_welcome_message(self):
        """Show welcome message in content area"""
        self.content_title.setText("Willkommen im Command Dashboard von xqi")

        welcome_text = """
        <p style="color: #f8f8f2; font-size: 14px;">
            Auswahl einer Kategorie aus dem Menü auf der linken Seite.
        </p>
        <p style="color: #f8f8f2; font-size: 14px; margin-top: 10px;">
            Auf einen Befehl klicken, um eine detaillierte Erklärung anzuzeigen.
        </p>
        <p style="color: #f8f8f2; font-size: 14px; margin-top: 10px;">
            Mit "Copy" kann der Befehl oder die Erklärung kopiert werden.
        </p>
        """

        welcome_label = QLabel(welcome_text)
        welcome_label.setWordWrap(True)
        welcome_label.setStyleSheet(
            f"color: {cfg.settings['colors']['text_color']}; font-size: {cfg.settings['sizes']['main_font_size']}px; background-color: transparent;")

        self.scroll_layout.addWidget(welcome_label)
        self.scroll_layout.addStretch()

    def show_main_menu(self):
        """Display the main menu"""
        try:
            # Update state
            self.current_state = "main"
            self.current_category_type = None
            self.current_category = None

            # Clear UI
            self.clear_sidebar()
            self.clear_content()

            # Add category buttons to sidebar
            main_menu_buttons = [
                ("LINUX BEFEHLE", self.show_linux_categories),
                ("SQL BEFEHLE", self.show_sql_categories),
                ("DATEN TYPEN", self.show_datentypen_categories)
            ]

            for text, callback in main_menu_buttons:
                btn = PyDraculaButton(text)
                btn.clicked.connect(callback)
                self.sidebar_layout.addWidget(btn)

            # Add settings and exit buttons
            self.add_common_sidebar_buttons()

            # Show welcome message
            self.show_welcome_message()

        except Exception as e:
            print(f"Error in show_main_menu: {e}")
            import traceback
            traceback.print_exc()

    def show_linux_categories(self):
        """Show Linux categories"""
        self.show_categories('linux')

    def show_sql_categories(self):
        """Show SQL categories"""
        self.show_categories('sql')

    def show_datentypen_categories(self):
        """Show Datentypen categories"""
        self.show_categories('datentypen')

    def show_categories(self, category_type):
        """Show categories for the selected type"""
        try:
            # Update state
            self.current_state = "categories"
            self.current_category_type = category_type
            self.current_category = None

            # Clear UI
            self.clear_sidebar()
            self.clear_content()

            # Add return button
            return_btn = PyDraculaButton("RETURN")
            return_btn.clicked.connect(self.show_main_menu)
            self.sidebar_layout.addWidget(return_btn)
            self.sidebar_layout.addSpacing(20)

            # Set content title
            self.content_title.setText(f"{category_type.upper()} KATEGORIEN")

            # Get categories for the selected type
            categories = self.command_data[category_type]

            # Create category buttons
            for cat_name in categories:
                btn = PyDraculaButton(cat_name)

                # Create a specific callback function for this button
                def create_callback(name=cat_name):
                    return lambda: self.show_commands(self.current_category_type, name)

                # Connect the button to its callback
                btn.clicked.connect(create_callback())

                # Add button to sidebar
                self.sidebar_layout.addWidget(btn)

            # Add settings & exit buttons
            self.add_common_sidebar_buttons()

            # stretch content
            self.scroll_layout.addStretch()

        except Exception as e:
            print(f"Error in show_categories: {e}")
            import traceback
            traceback.print_exc()

    def show_commands(self, category_type, category_name):
        """Show commands for the selected category"""
        try:
            # Update state
            self.current_state = "commands"
            self.current_category_type = category_type
            self.current_category = category_name

            # Clear UI
            self.clear_sidebar()
            self.clear_content()

            # Add return to categories button
            return_btn = PyDraculaButton("RETURN")

            # Create a specific callback for return button
            def return_to_categories():
                self.show_categories(self.current_category_type)

            return_btn.clicked.connect(return_to_categories)
            self.sidebar_layout.addWidget(return_btn)
            self.sidebar_layout.addSpacing(20)

            # Set content title
            self.content_title.setText(f"{category_name} - BEFEHLE")

            # Get commands for the selected category
            commands = self.command_data[category_type][category_name]

            # Create command buttons
            for cmd_name, cmd_data in commands.items():
                # Create button
                btn = PyDraculaButton(cmd_name)

                # Get command data
                command = cmd_data['command']
                explanation = cmd_data['explanation']

                # Create a specific callback function for this button
                def create_callback(cmd=command, exp=explanation, cat_type=category_type):
                    return lambda: self.display_command(cmd, exp, cat_type)

                # Connect the button to its callback
                btn.clicked.connect(create_callback())

                # Add button to content area
                self.scroll_layout.addWidget(btn)

            # Add settings and exit buttons
            self.add_common_sidebar_buttons()

            # stretch for content
            self.scroll_layout.addStretch()

        except Exception as e:
            print(f"Error in show_commands: {e}")
            import traceback
            traceback.print_exc()

    def display_command(self, command, explanation, category_type=None):
        """Display command and explanation in the output area"""
        try:
            # Clear  highlighter
            if self.sql_highlighter:
                self.sql_highlighter.setDocument(None)
                self.sql_highlighter = None

            # Display command and explanation
            self.command_display.setPlainText(command)
            self.explanation_display.setPlainText(explanation)

            # syntax highlighting for SQL commands
            is_sql = category_type == 'sql' or self.current_category_type == 'sql'
            if is_sql and command:
                self.sql_highlighter = SQLSyntaxHighlighter(self.command_display.document())

        except Exception as e:
            print(f"Error in display_command: {e}")
            import traceback
            traceback.print_exc()