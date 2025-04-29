import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont
from CommandDashboard import CommandDashboard

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        app.setStyle("Fusion")

        #  Set font
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        app.setFont(font)

        # Create and show main window
        window = CommandDashboard()
        window.show()

        sys.exit(app.exec())
    except Exception as e:
        print(f"Application error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)