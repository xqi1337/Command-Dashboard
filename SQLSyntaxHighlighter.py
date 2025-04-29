from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont

class SQLSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, document):
        super().__init__(document)

        self.highlighting_rules = []

        # SQL Keywords - Pink and bold
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

        # Setup highlighting rules for each syntax element
        for word in keywords:
            pattern = QRegularExpression(r'\b' + word + r'\b',
                                         QRegularExpression.PatternOption.CaseInsensitiveOption)
            self.highlighting_rules.append((pattern, keyword_format))

        # Numbers - Purple
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#bd93f9"))
        self.highlighting_rules.append((QRegularExpression(r'\b\d+\b'), number_format))

        # Strings - Yellow (both single and double quotes)
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#f1fa8c"))
        self.highlighting_rules.append((QRegularExpression(r"'[^']*'"), string_format))
        self.highlighting_rules.append((QRegularExpression(r'"[^"]*"'), string_format))

        # Functions - Cyan
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#8be9fd"))
        self.highlighting_rules.append((QRegularExpression(r'\b[A-Za-z0-9_]+(?=\s*\()'), function_format))

        # Comments - Grayish blue
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6272a4"))
        self.highlighting_rules.append((QRegularExpression(r'--.*'), comment_format))

        # For multiline comments
        self.comment_start_expression = QRegularExpression(r'/\*')
        self.comment_end_expression = QRegularExpression(r'\*/')
        self.multi_line_comment_format = QTextCharFormat()
        self.multi_line_comment_format.setForeground(QColor("#6272a4"))

    def highlightBlock(self, text):
        # Apply regular expression highlighting rules
        for pattern, format in self.highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)

        # Handle multi-line comments
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
            if match.hasMatch():
                end_index = match.capturedStart() + match.capturedLength()
                comment_length = end_index - start_index
                self.setFormat(start_index, comment_length, self.multi_line_comment_format)
                # Find the next comment start
                match = self.comment_start_expression.match(text, start_index + comment_length)
                if match.hasMatch():
                    start_index = match.capturedStart()
                else:
                    start_index = -1
            else:
                # No end found, format until the end of the block and mark the state
                self.setCurrentBlockState(1)
                comment_length = len(text) - start_index
                self.setFormat(start_index, comment_length, self.multi_line_comment_format)
                break