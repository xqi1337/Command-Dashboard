import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
                             QTextEdit, QScrollArea, QFrame, QGraphicsDropShadowEffect)
from PyQt6.QtCore import Qt, QRegularExpression
from PyQt6.QtGui import QFont, QColor, QSyntaxHighlighter, QTextCharFormat
from command_data import COMMAND_DATA


class SQLSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)
        self.highlighting_rules = []

        # Format für SQL-Schlüsselwörter (pink, fett)
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#ff79c6"))
        keyword_format.setFontWeight(QFont.Weight.Bold)
        keywords = [
            "SELECT", "FROM", "WHERE", "INSERT", "UPDATE", "DELETE", "DROP", "CREATE", "ALTER",
            "TABLE", "JOIN", "LEFT", "RIGHT", "INNER", "OUTER", "FULL", "ON", "AS", "ORDER BY",
            "GROUP BY", "HAVING", "LIMIT", "OFFSET", "UNION", "ALL", "DISTINCT", "INTO", "VALUES",
            "SET", "INDEX", "PRIMARY", "KEY", "FOREIGN", "REFERENCES", "NOT", "NULL", "DEFAULT",
            "AUTO_INCREMENT", "UNIQUE", "CHECK", "CONSTRAINT", "USE", "SHOW", "DESCRIBE"
        ]

        # Highlighting-Regeln für Schlüsselwörter
        for word in keywords:
            pattern = QRegularExpression(r'\b' + word + r'\b', QRegularExpression.PatternOption.CaseInsensitiveOption)
            self.highlighting_rules.append((pattern, keyword_format))

        # Format für Zahlen (lila)
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#bd93f9"))
        self.highlighting_rules.append((QRegularExpression(r'\b\d+\b'), number_format))

        # Format für Strings (gelb)
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#f1fa8c"))
        self.highlighting_rules.append((QRegularExpression(r"'[^']*'"), string_format))
        self.highlighting_rules.append((QRegularExpression(r'"[^"]*"'), string_format))

        # Format für Funktionen (cyan)
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#8be9fd"))
        self.highlighting_rules.append((QRegularExpression(r'\b[A-Za-z0-9_]+(?=\s*\()'), function_format))

        # Format für Kommentare (graublau)
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6272a4"))
        self.highlighting_rules.append((QRegularExpression(r'--.*$'), comment_format))

        # Format für mehrzeilige Kommentare
        self.comment_start_expression = QRegularExpression(r'/\*')
        self.comment_end_expression = QRegularExpression(r'\*/')
        self.multi_line_comment_format = QTextCharFormat()
        self.multi_line_comment_format.setForeground(QColor("#6272a4"))

    def highlightBlock(self, text):
        # Anwenden der Highlighting-Regeln
        for pattern, format in self.highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)

        # Behandlung mehrzeiliger Kommentare
        self.setCurrentBlockState(0)

        start_index = 0
        if self.previousBlockState() != 1:
            match = self.comment_start_expression.match(text)
            if match.hasMatch():
                start_index = match.capturedStart()
            else:
                start_index = -1

        while start_index >= 0:
            match = self.comment_end_expression.match(text, start_index)
            end_index = -1
            if match.hasMatch():
                end_index = match.capturedStart()

            comment_length = 0
            if end_index == -1:
                self.setCurrentBlockState(1)
                comment_length = len(text) - start_index
            else:
                comment_length = end_index - start_index + match.capturedLength()

            self.setFormat(start_index, comment_length, self.multi_line_comment_format)

            match = self.comment_start_expression.match(text, start_index + comment_length)
            if match.hasMatch():
                start_index = match.capturedStart()
            else:
                start_index = -1


class PyDraculaButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(40)
        self.setStyleSheet("""
            QPushButton {
                background-color: #6272a4;
                color: #f8f8f2;
                border-radius: 5px;
                padding: 8px 16px;
                text-align: left;
                font-size: 12px;
                border: 1px solid #6272a4;
                margin: 2px;
            }
            QPushButton:hover {
                background-color: #44475a;
                border: 1px solid #bd93f9;
                margin: 0px;
                padding: 10px 18px;
            }
            QPushButton:pressed {
                background-color: #44475a;
                color: #f8f8f2;
                border: 1px solid #ff79c6;
            }
        """)
        self.setGraphicsEffect(self.create_shadow_effect())

    def create_shadow_effect(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(189, 147, 249, 150))
        shadow.setOffset(0, 0)
        return shadow

    def enterEvent(self, event):
        if self.graphicsEffect():
            effect = self.graphicsEffect()
            effect.setBlurRadius(25)
            effect.setColor(QColor(189, 147, 249, 200))
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.graphicsEffect():
            effect = self.graphicsEffect()
            effect.setBlurRadius(15)
            effect.setColor(QColor(189, 147, 249, 150))
        super().leaveEvent(event)


class CommandDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.command_data = COMMAND_DATA
        self.sql_highlighter = None
        self.current_category_type = None
        self.initUI()
        self.create_main_menu()

    def initUI(self):
        self.setWindowTitle("GET GOOD GET COPYSENSE")
        self.setMinimumSize(1200, 700)
        self.setStyleSheet("background-color: #282a36;")

        # Haupt-Widget und Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # UI-Komponenten initialisieren
        self.setup_sidebar()
        self.setup_content_and_output_areas()

    def create_shadow_effect(self):
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(189, 147, 249, 150))
        shadow.setOffset(0, 0)
        return shadow

    def setup_sidebar(self):
        # Sidebar mit Menüoptionen
        self.sidebar = QFrame()
        self.sidebar.setStyleSheet("background-color: #282a36;")
        self.sidebar.setFixedWidth(250)
        self.sidebar_layout = QVBoxLayout(self.sidebar)
        self.sidebar_layout.setContentsMargins(10, 20, 10, 20)
        self.sidebar_layout.setSpacing(15)
        self.sidebar_title = QLabel("MENU")
        self.sidebar_title.setStyleSheet("""
            QLabel {
                color: #f8f8f2;
                font-size: 16px;
                font-weight: bold;
                padding-bottom: 10px;
                border-bottom: 1px solid #44475a;
            }
        """)
        self.sidebar_layout.addWidget(self.sidebar_title)
        self.sidebar_layout.addSpacing(20)
        self.main_layout.addWidget(self.sidebar)

    def setup_content_and_output_areas(self):
        self.content_area = self.create_content_area()
        self.output_area = self.create_output_area()
        self.output_container = QWidget()
        self.output_container.setStyleSheet("background-color: transparent;")
        self.output_container_layout = QVBoxLayout(self.output_container)
        self.output_container_layout.addWidget(self.content_area)
        self.output_container_layout.addWidget(self.output_area)
        self.main_layout.addWidget(self.output_container)

    def create_content_area(self):
        # Bereich für die Befehlsanzeige
        content_area = QFrame()
        content_area.setStyleSheet("background-color: #282a36;")
        self.content_layout = QVBoxLayout(content_area)
        self.content_layout.setContentsMargins(20, 20, 20, 20)
        self.content_layout.setSpacing(15)
        self.content_title = QLabel()
        self.content_title.setStyleSheet("""
            QLabel {
                color: #f8f8f2;
                font-size: 18px;
                font-weight: bold;
            }
        """)
        self.content_layout.addWidget(self.content_title)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background: transparent;
            }
            QScrollBar:vertical {
                background: #282a36;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #6272a4;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)

        self.scroll_widget = QWidget()
        self.scroll_widget.setStyleSheet("background-color: transparent;")
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setContentsMargins(0, 0, 10, 0)
        self.scroll_layout.setSpacing(20)
        self.scroll_area.setWidget(self.scroll_widget)
        self.content_layout.addWidget(self.scroll_area)

        return content_area

    def create_output_area(self):
        # Bereich für die Ausgabe (Befehl und Erklärung)
        output_area = QFrame()
        output_area.setStyleSheet("background-color: #282a36;")
        output_area.setFixedHeight(250)

        self.output_layout = QHBoxLayout(output_area)
        self.output_layout.setContentsMargins(10, 10, 10, 10)
        self.output_layout.setSpacing(10)
        self.command_container = self.create_display_container(
            is_command=True,
            copy_callback=lambda: self.copy_to_clipboard(self.command_display.toPlainText(), "Command")
        )

        self.explanation_container = self.create_display_container(
            is_command=False,
            copy_callback=lambda: self.copy_to_clipboard(self.explanation_display.toPlainText(), "Explanation")
        )

        self.output_layout.addWidget(self.command_container)
        self.output_layout.addWidget(self.explanation_container)

        return output_area

    def create_display_container(self, is_command=True, copy_callback=None):
        # Container für Befehl oder Erklärung
        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(5)

        display = QTextEdit()
        display.setReadOnly(True)
        font_family = "Consolas" if is_command else "Segoe UI"
        display.setStyleSheet(f"""
            QTextEdit {{
                background-color: #282a36;
                color: #f8f8f2;
                border: 1px solid #6272a4;
                border-radius: 5px;
                padding: 10px;
                font-family: {font_family};
                font-size: 12px;
            }}
        """)

        if is_command:
            self.command_display = display
        else:
            self.explanation_display = display

        # Kopieren-Button
        copy_btn = QPushButton("COPY")
        copy_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        copy_btn.setStyleSheet("""
            QPushButton {
                background-color: #6272a4;
                color: #f8f8f2;
                border-radius: 3px;
                padding: 5px;
                font-size: 12px;
                border: 1px solid #6272a4;
                margin: 2px;
            }
            QPushButton:hover {
                background-color: #44475a;
                border: 1px solid #bd93f9;
                margin: 0px;
                padding: 7px;
            }
            QPushButton:pressed {
                background-color: #44475a;
                color: #f8f8f2;
                border: 1px solid #ff79c6;
            }
        """)
        copy_btn.setGraphicsEffect(self.create_shadow_effect())

        if copy_callback:
            copy_btn.clicked.connect(copy_callback)

        container_layout.addWidget(display)
        container_layout.addWidget(copy_btn)

        return container

    def copy_to_clipboard(self, text, text_type):
        # Text in die Zwischenablage kopieren
        if text:
            clipboard = QApplication.clipboard()
            clipboard.setText(text)

    def create_main_menu(self):
        # Hauptmenü erstellen
        self.clear_sidebar_except_title()

        menu_buttons = [
            ("LINUX COMMANDS", lambda: self.show_categories('linux')),
            ("SQL COMMANDS", lambda: self.show_categories('sql')),
            ("DATENTYPEN", lambda: self.show_categories('datentypen')),
            ("Exit", self.close)
        ]

        for text, command in menu_buttons:
            btn = PyDraculaButton(text)
            btn.clicked.connect(command)
            self.sidebar_layout.addWidget(btn)

        self.sidebar_layout.addStretch()
        self.show_welcome_message()

    def clear_sidebar_except_title(self):
        # Sidebar bereinigen (außer Titel)
        while self.sidebar_layout.count() > 1:
            item = self.sidebar_layout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()

    def clear_layout(self, layout):
        # Layout komplett leeren
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def clear_output(self):
        # Ausgabebereiche leeren
        self.command_display.clear()
        self.explanation_display.clear()

        if self.sql_highlighter:
            self.sql_highlighter.setDocument(None)
            self.sql_highlighter = None

    def show_welcome_message(self):
        # Willkommensnachricht anzeigen
        self.clear_layout(self.scroll_layout)
        self.content_title.setText("Willkommen im Command Dashboard von xqi")
        self.clear_output()

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
        welcome_label.setStyleSheet("color: #f8f8f2; font-size: 14px; background-color: transparent;")
        self.scroll_layout.addWidget(welcome_label)
        self.scroll_layout.addStretch()

    def show_categories(self, category_type):
        try:
            # Kategorien anzeigen
            self.clear_layout(self.scroll_layout)
            self.clear_output()
            self.clear_sidebar_except_title()
            self.current_category_type = category_type

            # Zurück-Button hinzufügen
            return_btn = PyDraculaButton("RETURN")
            return_btn.clicked.connect(self.create_main_menu)
            self.sidebar_layout.insertWidget(1, return_btn)
            self.sidebar_layout.addSpacing(20)

            self.content_title.setText(f"{category_type.upper()} KATEGORIEN")

            # Kategorie-Buttons hinzufügen
            categories = self.command_data[category_type]
            for category_name in categories:
                if category_name != 'categories' and category_name != 'commands':
                    category_btn = PyDraculaButton(category_name)
                    category_btn.clicked.connect(
                        lambda checked=False, cat_name=category_name:
                        self.show_commands(self.current_category_type, cat_name)
                    )
                    self.sidebar_layout.addWidget(category_btn)

            self.sidebar_layout.addStretch()

        except Exception as e:
            print(f"Error in show_categories: {e}")
            import traceback
            traceback.print_exc()

    def show_commands(self, category_type, category_name):
        try:
            # Befehle einer Kategorie anzeigen
            self.clear_layout(self.scroll_layout)

            self.content_title.setText(f"{category_name} - BEFEHLE")
            commands = self.command_data[category_type][category_name]

            # Befehls-Buttons hinzufügen
            for cmd_name, cmd_data in commands.items():
                cmd_btn = PyDraculaButton(cmd_name)
                command = cmd_data['command']
                explanation = cmd_data['explanation']

                cmd_btn.clicked.connect(
                    lambda checked=False, cmd=command, exp=explanation, cat=category_type:
                    self.display_command(cmd, exp, cat)
                )
                self.scroll_layout.addWidget(cmd_btn)

            self.scroll_layout.addStretch()

        except Exception as e:
            print(f"Error in show_commands: {e}")
            import traceback
            traceback.print_exc()

    def display_command(self, command, explanation, category_type=None):
        try:
            # Befehl und Erklärung anzeigen
            if self.sql_highlighter:
                self.sql_highlighter.setDocument(None)
                self.sql_highlighter = None

            self.command_display.setPlainText(command)
            self.explanation_display.setPlainText(explanation)

            # SQL-Syntax-Highlighting bei SQL-Befehlen
            is_sql = category_type == 'sql' or self.current_category_type == 'sql'
            if is_sql:
                self.sql_highlighter = SQLSyntaxHighlighter(self.command_display.document())

        except Exception as e:
            print(f"Error in display_command: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        app.setStyle("Fusion")

        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        app.setFont(font)

        window = CommandDashboard()
        window.show()

        sys.exit(app.exec())
    except Exception as e:
        print(f"Application error: {e}")
        sys.exit(1)
