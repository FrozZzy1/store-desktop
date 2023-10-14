from PyQt6.QtGui import QWindow


class TemplateWindow(QWindow):
    window_width = 1280
    window_height = 720

    def __init__(self):
        super().__init__()

        self.resize(self.window_width, self.window_height)

