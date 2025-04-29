from PyQt6.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor #, QGraphicsDropShadowEffect
import cfg

class PyDraculaButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMinimumHeight(cfg.settings["sizes"]["button_min_height"])
        self.setStyleSheet(cfg.generate_button_stylesheet())
        self.update_shadow_effect()

    def update_shadow_effect(self):
        # shadow effect
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(cfg.settings["colors"]["button_shadow_blur"])
        shadow.setColor(QColor(
            cfg.settings["colors"]["button_shadow_color"] +
            format(cfg.settings["colors"]["button_shadow_opacity"], '02x')
        ))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)

    def enterEvent(self, event):
        if self.graphicsEffect():
            effect = self.graphicsEffect()
            effect.setBlurRadius(cfg.settings["colors"]["button_shadow_hover_blur"])
            effect.setColor(QColor(
                cfg.settings["colors"]["button_shadow_hover_color"] +
                format(cfg.settings["colors"]["button_shadow_hover_opacity"], '02x')
            ))
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.graphicsEffect():
            effect = self.graphicsEffect()
            effect.setBlurRadius(cfg.settings["colors"]["button_shadow_blur"])
            effect.setColor(QColor(
                cfg.settings["colors"]["button_shadow_color"] +
                format(cfg.settings["colors"]["button_shadow_opacity"], '02x')
            ))
        super().leaveEvent(event)