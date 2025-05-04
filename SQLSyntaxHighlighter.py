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

        # Umfangreiche Liste von SQL-Befehlen
        keywords = [
            # DDL - Data Definition Language
            "CREATE", "ALTER", "DROP", "TRUNCATE", "COMMENT", "RENAME", "DESCRIBE",

            # DML - Data Manipulation Language
            "SELECT", "INSERT", "UPDATE", "DELETE", "REPLACE", "MERGE", "CALL", "EXPLAIN", "LOCK",

            # DCL - Data Control Language
            "GRANT", "REVOKE", "COMMIT", "ROLLBACK", "SAVEPOINT", "SET", "START", "BEGIN", "END",

            # Tabellenstrukturen und -modifikatoren
            "TABLE","TABLES", "VIEW", "INDEX", "TRIGGER", "PROCEDURE", "FUNCTION", "SCHEMA", "DATABASE",
            "SEQUENCE", "PARTITION", "TEMPORARY", "TEMP", "COLUMN", "USE", "SHOW", "DATABASES",

            # Datentypen
            "INT", "INTEGER", "SMALLINT", "TINYINT", "MEDIUMINT", "BIGINT", "DECIMAL",
            "NUMERIC", "FLOAT", "DOUBLE", "REAL", "BIT", "BOOLEAN", "SERIAL", "DATE",
            "DATETIME", "TIMESTAMP", "TIME", "YEAR", "CHAR", "VARCHAR", "BINARY",
            "VARBINARY", "BLOB", "TEXT", "ENUM", "SET", "JSON", "CHARACTER",

            # Join-Typen
            "JOIN", "INNER", "OUTER", "LEFT", "RIGHT", "FULL", "CROSS", "NATURAL", "STRAIGHT_JOIN",

            # Bedingungen und Operatoren
            "ON", "WHERE", "AND", "OR", "NOT", "IS", "IN", "BETWEEN", "LIKE", "REGEXP", "SIMILAR",
            "TO", "EXISTS", "ALL", "ANY", "SOME", "HAVING", "AS", "WITH", "RECURSIVE", "CASE",
            "WHEN", "THEN", "ELSE", "END", "NULLIF", "COALESCE",

            # Aggregation und Gruppierung
            "GROUP", "BY", "ORDER", "ASC", "DESC", "LIMIT", "OFFSET", "TOP", "FETCH", "FIRST", "NEXT",
            "ROWS", "ONLY", "PERCENT", "DISTINCT", "UNION", "UNION ALL", "EXCEPT", "INTERSECT",
            "MINUS", "OVERLAPS", "INTO", "VALUES", "FROM",

            # Schlüssel und Constraints
            "PRIMARY", "KEY", "FOREIGN", "UNIQUE", "CHECK", "DEFAULT", "CONSTRAINT", "REFERENCES",
            "NULL", "NOT", "AUTO_INCREMENT", "IDENTITY", "GENERATED", "ALWAYS", "NEVER", "ADD"
        ]

        # Setup highlighting rules for each syntax element
        for word in keywords:
            pattern = QRegularExpression(r'\b' + word + r'\b',
                                         QRegularExpression.PatternOption.CaseInsensitiveOption)
            self.highlighting_rules.append((pattern, keyword_format))

        # Tabellen und Spalten in eckigen Klammern - Türkis
        bracket_format = QTextCharFormat()
        bracket_format.setForeground(QColor("#8be9fd"))
        bracket_pattern = QRegularExpression(r'\[\w+\]')
        self.highlighting_rules.append((bracket_pattern, bracket_format))

        # SQL-Funktionen - Cyan und kursiv
        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#8be9fd"))
        function_format.setFontItalic(True)

        # Häufig verwendete SQL-Funktionen
        functions = [
            # Aggregatfunktionen
            "COUNT", "SUM", "AVG", "MIN", "MAX", "GROUP_CONCAT", "STDDEV", "VARIANCE",

            # String-Funktionen
            "CONCAT", "SUBSTRING", "TRIM", "LTRIM", "RTRIM", "UPPER", "LOWER", "REPLACE",
            "INSTR", "LENGTH", "CHAR_LENGTH", "LEFT", "RIGHT", "REVERSE", "FORMAT", "REPEAT",

            # Datumsfunktionen
            "NOW", "CURDATE", "CURTIME", "DATE", "EXTRACT", "YEAR", "MONTH", "DAY",
            "HOUR", "MINUTE", "SECOND", "DATEDIFF", "DATE_ADD", "DATE_SUB", "STR_TO_DATE",
            "DATE_FORMAT", "FROM_UNIXTIME", "UNIX_TIMESTAMP",

            # Mathematische Funktionen
            "ABS", "ROUND", "CEIL", "CEILING", "FLOOR", "SIGN", "SQRT", "POW", "POWER",
            "EXP", "LOG", "LOG10", "LOG2", "PI", "SIN", "COS", "TAN", "RAND",

            # Kontrollfunktionen
            "IF", "IFNULL", "NULLIF", "CASE", "COALESCE", "GREATEST", "LEAST"
        ]

        for func in functions:
            pattern = QRegularExpression(r'\b' + func + r'\b(?=\s*\()?',
                                         QRegularExpression.PatternOption.CaseInsensitiveOption)
            self.highlighting_rules.append((pattern, function_format))

        # Generische Funktion - alles was direkt vor einer Klammer steht
        self.highlighting_rules.append(
            (QRegularExpression(r'\b[A-Za-z0-9_]+(?=\s*\()'), function_format)
        )

        # Numbers - Purple
        number_format = QTextCharFormat()
        number_format.setForeground(QColor("#bd93f9"))
        # Verbesserte Zahlenerkennung (inkl. Dezimalzahlen)
        self.highlighting_rules.append(
            (QRegularExpression(r'\b[-+]?\d*\.?\d+([eE][-+]?\d+)?\b'), number_format)
        )

        # Strings - Yellow
        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#ccff66"))
        self.highlighting_rules.append((QRegularExpression(r"'[^']*'"), string_format))
        self.highlighting_rules.append((QRegularExpression(r'"[^"]*"'), string_format))
        self.highlighting_rules.append((QRegularExpression(r'`[^`]*`'), string_format))  # Backticks für Bezeichner

        # Database- und Tabellennamen nach Schlüsselwörtern - Orange
        identifier_format = QTextCharFormat()
        identifier_format.setForeground(QColor("#ffb86c"))

        # Pattern für Namen nach bestimmten Schlüsselwörtern
        identifiers_after = [
            r'(?<=\bUSE\s)\w+',
            r'(?<=\bDATABASE\s)\w+',
            r'(?<=\bTABLE\s)[\w.]+',
            r'(?<=\bFROM\s)[\w.]+',
            r'(?<=\bJOIN\s)[\w.]+'
        ]

        for pattern in identifiers_after:
            self.highlighting_rules.append(
                (QRegularExpression(pattern, QRegularExpression.PatternOption.CaseInsensitiveOption),
                 identifier_format)
            )

        # Kommentare - Grayish blue
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6272a4"))
        comment_format.setFontItalic(True)
        self.highlighting_rules.append((QRegularExpression(r'--.*'), comment_format))
        self.highlighting_rules.append((QRegularExpression(r'#.*'), comment_format))

        # Spezielle SQL-Operatoren - green
        operator_format = QTextCharFormat()
        operator_format.setForeground(QColor("#66ff99"))
        operators = [r'=', r'<>', r'!=', r'<', r'>', r'<=', r'>=', r'\+', r'-', r'\*', r'/', r'%']
        for op in operators:
            self.highlighting_rules.append((QRegularExpression(op), operator_format))

        # Für mehrzeilige Kommentare
        self.comment_start_expression = QRegularExpression(r'/\*')
        self.comment_end_expression = QRegularExpression(r'\*/')
        self.multi_line_comment_format = comment_format

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